import json
import re
from email.parser import Parser
from pathlib import Path
from lxml import etree
from locator_generator import LocatorGenerator

task_json_obj = {"task": []}
# element_in_iframe_num = 97
# element_in_iframe_and_from_task_json_num = 0
# none_ground_truth = 0


def clean_part_headers(part_content):
    # Define the headers to remove
    headers_to_remove = [
        r'^Content-Type: text/html.*?\n',
        r'^Content-ID: <frame-.*?>@mhtml\.blink.*?\n',
        r'^Content-Transfer-Encoding: quoted-printable.*?\n',
        r'^Content-Location: https://trace\.playwright\.dev/snapshot/.*?\n'
    ]

    # Remove each specified header from the part content
    for header_pattern in headers_to_remove:
        part_content = re.sub(header_pattern, '', part_content, flags=re.MULTILINE | re.IGNORECASE)

    return part_content


def extract_mhtml_contents(mhtml_path):
    with open(mhtml_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Parse the MHTML into its constituent parts
    parser = Parser()
    mime_message = parser.parsestr(content)

    main_html = None
    iframes = {}

    for part in mime_message.walk():
        content_type = part.get_content_type()
        content_location: str = part.get('Content-Location')
        content_id: str = part.get('Content-ID')
        # decode=True automatically decodes from base64 or quoted-printable
        payload = part.get_payload(decode=True)

        if content_type == 'text/html':
            decoded_payload = payload.decode('utf-8', errors='replace') if payload else ''
            cleaned_payload = clean_part_headers(decoded_payload)
            # Assuming the first HTML part is the main content
            if main_html is None and "frame@" not in content_location:
                main_html = cleaned_payload
            elif cleaned_payload != '':
                iframes[content_id] = cleaned_payload
    filtered_iframes = {k: v for k, v in iframes.items() if k is not None and v is not None}
    return main_html, filtered_iframes


def search_ground_truth_element(content_dict, action_uid, sources=None, current_index=0):
    if sources is None:
        sources = list(content_dict.keys())
    # Base case: if we've searched all sources without finding the element
    if current_index >= len(sources):
        return None, None
    source = sources[current_index]
    parsed_content = etree.fromstring(content_dict[source], etree.HTMLParser(recover=True))
    ground_truth_element = parsed_content.xpath(f"//*[@data-pw-testid-buckeye='{action_uid}']")
    # ground_truth_element = parsed_content.xpath(f"//*[@data-pw-testid-buckeye='360a4b82-5666-4d87-8b10-2ea3b37f78ef']")
    if ground_truth_element:
        return ground_truth_element, source

    # If not found, recursively search the next source in the list
    return search_ground_truth_element(content_dict, action_uid, sources, current_index + 1)


def get_ground_truth_element(main_content, iframe_dict, action):
    iframe_dict["main"] = main_content
    # let main be the first to speed up the process
    # print(iframe_dict)
    # return search_ground_truth_element(iframe_dict, action['action_uid'])
    return search_ground_truth_element(dict(reversed(iframe_dict.items())), action['action_uid'])  # 360a4b82-5666-4d87-8b10-2ea3b37f78ef_before
    # return search_ground_truth_element(dict(reversed(iframe_dict.items())), "90670a38-3871-4600-954c-f1c33049539b")


def get_info_from_task_json(task_file_path, task_annotation_id, each_action_id):
    # use the information from tasks json when ground truth element is not available in mhtml
    with open(task_file_path, 'r') as file:
        tasks = json.load(file)['task']
        for task in tasks:
            if task["annotation_id"] == task_annotation_id:
                for action in task["actions"]:
                    action_target_element = action["target_element"]
                    if each_action_id in action_target_element:
                        return action
                    # parsed_action_target_element = etree.fromstring(action_target_element, etree.HTMLParser(recover=True))
                    # if parsed_action_target_element.get("data_pw_testid_buckeye") == each_action_id:
                    #     return action

        return None


def deep_merge(dict1, dict2):
    for key in dict2:
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            deep_merge(dict1[key], dict2[key])
        else:
            dict1[key] = dict2[key]


def analyze_task_actions(actions, annotation_id):
    # "/Volumes/seagate/Mind2Web/data/raw_dump/task/" + each_scenario["annotation_id"] + "/processed/snapshots/"
    if_deep_merge = True
    each_task_action_list_json = {"actions": []}
    for each_action in actions:
        before_action_snapshot = "/Volumes/seagate/Mind2Web/data/raw_dump/task/" + annotation_id + "/processed/snapshots/" + each_action["action_uid"] + "_before.mhtml"
        # before_action_snapshot = "/Volumes/seagate/Mind2Web/data/raw_dump/task/277e3468-f8cb-45c6-9e4b-0328066c42d3/processed/snapshots/90670a38-3871-4600-954c-f1c33049539b_before.mhtml"
        print(before_action_snapshot)
        temp_each_action_json = {"operation": each_action["operation"]}

        main_html_content, iframes = extract_mhtml_contents(before_action_snapshot)
        ground_truth_element, iframe_id = get_ground_truth_element(main_html_content, iframes, each_action)

        if ground_truth_element is None:
            action = get_info_from_task_json("../resource/tasks.json", annotation_id, each_action["action_uid"])
            if action:
                action["generated_from"] = "tasks_json"
                print(action["target_element"])
                print(action["locators"])
                # print(action)
                # print(type(action))
                # print(action["locators"])
                # if "/iframe[" in action["locators"]:
                #     globals()["element_in_iframe_and_from_task_json_num"] += 1
                each_task_action_list_json["actions"].append(action)
            else:
                if_deep_merge = False
                # globals()["none_ground_truth"] += 1
                # print("In deep merge false") # none_ground_truth
                break
        else:
            element_string_pretty = etree.tostring(ground_truth_element[0], pretty_print=True).decode('utf-8')
            print("ground truth element: " + element_string_pretty)
            if iframe_id == "main":
                generator = LocatorGenerator(main_html_content)
            else:
                # based on one trial, there is no actions that don't have ground truth element, and there is no actions performed in an iframe from tasks.json.
                # so we can only consider this situation for iframe related actions.
                generator = LocatorGenerator(iframes[iframe_id])
                # globals()["element_in_iframe_num"] += 1
            locator = generator.get_all_locator(ground_truth_element[0])
            temp_each_action_json["target_element"] = element_string_pretty
            temp_each_action_json["locators"] = json.loads(locator)
            temp_each_action_json["generated_from"] = "mhtml"
            temp_each_action_json["iframe_id"] = iframe_id
            # print(element_string_pretty)
            print(locator)
            # print(temp_each_action_json)
            each_task_action_list_json["actions"].append(temp_each_action_json)

    return each_task_action_list_json, if_deep_merge


# def analyze_action_reprs(action_reprs):
#     print(type(action_reprs))
#     print(action_reprs)
#     each_task_action_reprs = {"action_reprs": {}}
#     for i, action_repr in enumerate(action_reprs):
#         # print(f"\t{i}. {action_repr}")
#         pass


def analyze_scenario(each_scenario):
    each_task_json = {}
    for key, value in each_scenario.items():
        # snapshot_path = "/Volumes/seagate/Mind2Web/data/raw_dump/task/" + each_scenario["annotation_id"] + "/processed/snapshots/"
        # snapshot_path = "/Volumes/seagate/Mind2Web/data/raw_dump/task/" + "cf8b2846-ac33-46aa-887c-174de6184057" + "/processed/snapshots/"
        if key != 'actions':
            # print(f"{key}: {value}")
            each_task_json[key] = value
        else:
            json_obj, if_merge = analyze_task_actions(value, each_scenario["annotation_id"])
            # for item in json_obj_list:
            if if_merge:
                deep_merge(each_task_json, json_obj)
            else:
                return None

    return each_task_json


def process_json_file(file_path):
    with file_path.open('r') as f:
        scenarios = json.load(f)
        for each_scenario in scenarios:
            json_obj = analyze_scenario(each_scenario)
            # Only append this task when every ground truth element is available
            if json_obj is not None:
                task_json_obj["task"].append(json_obj)


def trace_analyzer(data_path):
    data_path = Path(data_path)
    for file_path in data_path.glob('**/*.json'):
        process_json_file(file_path)


if __name__ == '__main__':
    train_data_dir = "Mind2Web/data"
    trace_analyzer(train_data_dir)
    with open('../resource/tests_to_execute.json', 'w', encoding='utf-8') as f:
        json.dump(task_json_obj, f, ensure_ascii=False, indent=4)
