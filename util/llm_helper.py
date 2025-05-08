import base64
import inspect
import logging
import re
import time

logging.basicConfig(level=logging.INFO)


def get_web_element_rect(browser, fix_color=True):
    if fix_color:
        selected_function = "getFixedColor"
        # color_you_like = '#5210da'
    else:
        selected_function = "getRandomColor"

    js_script = r"""
        let labels = [];

        function markPage() {
            var bodyRect = document.body.getBoundingClientRect();

            var items = Array.prototype.slice.call(
                document.querySelectorAll('*')
            ).map(function(element) {
                var vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
                var vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);

                var rects = [...element.getClientRects()].filter(bb => {
                var center_x = bb.left + bb.width / 2;
                var center_y = bb.top + bb.height / 2;
                var elAtCenter = document.elementFromPoint(center_x, center_y);

                return elAtCenter === element || element.contains(elAtCenter) 
                }).map(bb => {
                const rect = {
                    left: Math.max(0, bb.left),
                    top: Math.max(0, bb.top),
                    right: Math.min(vw, bb.right),
                    bottom: Math.min(vh, bb.bottom)
                };
                return {
                    ...rect,
                    width: rect.right - rect.left,
                    height: rect.bottom - rect.top
                }
                });

                var area = rects.reduce((acc, rect) => acc + rect.width * rect.height, 0);

                return {
                element: element,
                include: 
                    (element.tagName === "INPUT" || element.tagName === "TEXTAREA" || element.tagName === "SELECT") ||
                    (element.tagName === "BUTTON" || element.tagName === "A" || (element.onclick != null) || window.getComputedStyle(element).cursor == "pointer") ||
                    (element.tagName === "IFRAME" || element.tagName === "VIDEO" || element.tagName === "LI" || element.tagName === "TD" || element.tagName === "OPTION")
                ,
                area,
                rects,
                text: element.textContent.trim().replace(/\s{2,}/g, ' ')
                };
            }).filter(item =>
                item.include && (item.area >= 20)
            );

            // Only keep inner clickable items
            // first delete button inner clickable items
            const buttons = Array.from(document.querySelectorAll('button, a, input[type="button"], div[role="button"]'));

            //items = items.filter(x => !buttons.some(y => y.contains(x.element) && !(x.element === y) ));
            items = items.filter(x => !buttons.some(y => items.some(z => z.element === y) && y.contains(x.element) && !(x.element === y) ));
            items = items.filter(x => 
                !(x.element.parentNode && 
                x.element.parentNode.tagName === 'SPAN' && 
                x.element.parentNode.children.length === 1 && 
                x.element.parentNode.getAttribute('role') &&
                items.some(y => y.element === x.element.parentNode)));

            items = items.filter(x => !items.some(y => x.element.contains(y.element) && !(x == y)))

            // Function to generate random colors
            function getRandomColor(index) {
                var letters = '0123456789ABCDEF';
                var color = '#';
                for (var i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
                }
                return color;
            }

            function getFixedColor(index) {
                var color = '#000000'
                return color
            }
            //function getFixedColor(index){
            //    var colors = ['#FF0000', '#00FF00', '#0000FF', '#000000']; // Red, Green, Blue, Black
            //    return colors[index % 4];
            //}


            // Lets create a floating border on top of these elements that will always be visible
            items.forEach(function(item, index) {
                item.rects.forEach((bbox) => {
                newElement = document.createElement("div");
                var borderColor = COLOR_FUNCTION(index);
                newElement.style.outline = `2px dashed ${borderColor}`;
                newElement.style.position = "fixed";
                newElement.style.left = bbox.left + "px";
                newElement.style.top = bbox.top + "px";
                newElement.style.width = bbox.width + "px";
                newElement.style.height = bbox.height + "px";
                newElement.style.pointerEvents = "none";
                newElement.style.boxSizing = "border-box";
                newElement.style.zIndex = 2147483647;
                // newElement.style.background = `${borderColor}80`;

                // Add floating label at the corner
                var label = document.createElement("span");
                label.textContent = index;
                label.style.position = "absolute";
                //label.style.top = "-19px";
                label.style.top = Math.max(-19, -bbox.top) + "px";
                //label.style.left = "0px";
                label.style.left = Math.min(Math.floor(bbox.width / 5), 2) + "px";
                label.style.background = borderColor;
                label.style.color = "white";
                label.style.padding = "2px 4px";
                label.style.fontSize = "12px";
                label.style.borderRadius = "2px";
                newElement.appendChild(label);

                document.body.appendChild(newElement);
                labels.push(newElement);
                // item.element.setAttribute("-ai-label", label.textContent);
                });
            })

            // For the first way
            // return [labels, items.map(item => ({
            //     rect: item.rects[0] // assuming there's at least one rect
            // }))];

            // For the second way
            return [labels, items]
        }
        return markPage();""".replace("COLOR_FUNCTION", selected_function)
    rects, items_raw = browser.execute_script(js_script)

    # format_ele_text = [f"[{web_ele_id}]: \"{items_raw[web_ele_id]['text']}\";" for web_ele_id in range(len(items_raw)) if items_raw[web_ele_id]['text'] ]
    format_ele_text = []
    for web_ele_id in range(len(items_raw)):
        element_html = items_raw[web_ele_id]['element'].get_attribute("outerHTML")
        label_text = items_raw[web_ele_id]['text']
        ele_tag_name = items_raw[web_ele_id]['element'].tag_name
        ele_type = items_raw[web_ele_id]['element'].get_attribute("type")
        ele_aria_label = items_raw[web_ele_id]['element'].get_attribute("aria-label")
        input_attr_types = ['text', 'search', 'password', 'email', 'tel']

        format_ele_text.append(f"[{web_ele_id}]: {element_html}")
        # if not label_text:
        #     if (ele_tag_name.lower() == 'input' and ele_type in input_attr_types) or ele_tag_name.lower() == 'textarea' or (ele_tag_name.lower() == 'button' and ele_type in ['submit', 'button']):
        #         if ele_aria_label:
        #             format_ele_text.append(f"[{web_ele_id}]: <{ele_tag_name}> \"{ele_aria_label}\";")
        #         else:
        #             format_ele_text.append(f"[{web_ele_id}]: <{ele_tag_name}> \"{label_text}\";")
        #
        # elif label_text and len(label_text) < 200:
        #     if not ("<img" in label_text and "src=" in label_text):
        #         if ele_tag_name in ["button", "input", "textarea", "a", "select"]:
        #             if ele_aria_label and (ele_aria_label != label_text):
        #                 format_ele_text.append(f"[{web_ele_id}]: <{ele_tag_name}> \"{label_text}\", \"{ele_aria_label}\";")
        #             else:
        #                 format_ele_text.append(f"[{web_ele_id}]: <{ele_tag_name}> \"{label_text}\";")
        #         else:
        #             if ele_aria_label and (ele_aria_label != label_text):
        #                 format_ele_text.append(f"[{web_ele_id}]: \"{label_text}\", \"{ele_aria_label}\";")
        #             else:
        #                 format_ele_text.append(f"[{web_ele_id}]: \"{label_text}\";")

    format_ele_text = '\n'.join(format_ele_text)
    return rects, [web_ele['element'].get_attribute("outerHTML") for web_ele in items_raw], format_ele_text


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def gather_test_code_and_failing_line(request):
    """
    Returns (test_method_source, failing_line_code) for the test that just failed.
    - test_method_source: the entire Python source of the failing test method
    - failing_line_code: the exact line from the traceback
    """
    test_method_obj = getattr(request.node.cls, request.node.name, None)
    test_method_source = None
    if test_method_obj:
        try:
            test_method_source = inspect.getsource(test_method_obj)
        except OSError:
            test_method_source = "Could not retrieve test method source."

    traceback_str = request.node.rep_call.longreprtext
    # Typical line pattern in the traceback: 'File "/path/to/test_file.py", line 15, in test_aa_6c28458c'
    pattern = r"(?m)^(test/test_.*?\.py):(\d+):\s*(.*)$"
    match = re.search(pattern, traceback_str)
    failing_line_code = "Unknown"
    if match:
        failing_file, failing_line, _ = match.groups()
        try:
            failing_line = int(failing_line)
            with open(failing_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            # Lines are 1-based in traceback, so subtract 1
            failing_line_code = lines[failing_line - 1].strip()
        except (FileNotFoundError, IndexError):
            pass

    return test_method_source, failing_line_code


def call_gpt_api(args, openai_client, messages):
    retry_times = 0
    max_retries = 3

    model_name = "o3"
    if args and hasattr(args, "api_model"):
        model_name = args.api_model

    while True:
        try:
            logging.info("Calling GPT API...")
            openai_response = openai_client.chat.completions.create(
                model=model_name,
                messages=messages,
                max_completion_tokens=100000,
                # temperature=0.5,
            )

            # Extract token usage if available
            prompt_tokens = openai_response.usage.prompt_tokens
            completion_tokens = openai_response.usage.completion_tokens

            logging.info(
                f"GPT call successful. Prompt tokens: {prompt_tokens}, "
                f"Completion tokens: {completion_tokens}"
            )

            gpt_call_error = False
            return prompt_tokens, completion_tokens, gpt_call_error, openai_response

        except Exception as e:
            logging.error(f"Error calling GPT: {e}")
            retry_times += 1
            if retry_times >= max_retries:
                logging.error("Max retries exceeded. Returning error.")
                gpt_call_error = True
                return None, None, gpt_call_error, None
            # Wait a bit before retrying
            time.sleep(5)

