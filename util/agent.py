import os
import logging
from openai import OpenAI
from util.llm_helper import encode_image, call_gpt_api


def call_gpt_for_candidate_fixes(
    test_name: str,
    class_name: str,
    screenshot_path: str,
    web_eles_text: str,
    traceback_text: str,
    test_method_source: str,
    failing_line_code: str,
    openai_api_key: str = None
) -> str:
    """
    Calls GPT with the screenshot and clickable elements to propose candidate fixes.
    Returns a string with GPT's suggestions or None if the call fails.
    """
    if not openai_api_key:
        openai_api_key = os.getenv("OPENAI_API_KEY")

    task_description = "finding the lowest travel time flight for 1 traveler from JFK, NYC to Heathrow, London on 04/19/2025, then from Heathrow, London to CDG, Paris on 04/21/2025 and then from CDG, Paris to JFK, NYC on 04/23/2025"
    system_msg = {
        "role": "system",
        "content": (
            "You are a helpful assistant for debugging Selenium test failures. "
            "At each stage, imagine you have the webpage screenshot where the test case fails (like a human looking at the browser), "
            "the output of the test execution, the failing test line, and the entire test method code. "
            "Your goal is to propose multiple short code changes or configuration steps that might fix the test. "
            "Please keep your commentary minimal—just enough to clarify each solution. "
            "Enumerate your suggestions as (1), (2), (3), etc. and maximum give 5 candidate suggestions. "
            "Terminate your answer once you have given these candidate fixes."
        )
    }

    screenshot_b64 = encode_image(screenshot_path)
    user_msg = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": (
                    f"Test {test_name} in class {class_name} failed.\n"
                    f"Traceback:\n{traceback_text}\n\n"
                    f"This test is about {task_description}\n\n"
                    "Below is the screenshot of the page where the test case fails, with interactable elements annotated. "
                    "You also have a textual list of those elements.\n\n"
                    "Apart from the annotated elements, you may also pay attention to the warning or error messages on the page to identify the root causes,  "
                    "and sometimes the root cause may not arise from the code line where test case fails, it may also arise from the previous steps.\n\n"
                    "Additionally, here is the entire test method code and the specific failing line:\n\n"
                    f"--- Test Method Source ---\n{test_method_source}\n\n"
                    f"--- Failing Line ---\n{failing_line_code}\n\n"
                    "Please propose a few possible code or configuration fixes that might solve the test failure. "
                    "Give me multiple candidate suggestions, enumerated as (1), (2), (3), etc.\n\n"
                    f"List of clickable elements:\n{web_eles_text}\n"
                ),
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{screenshot_b64}"}
            }
        ]
    }

    messages = [system_msg, user_msg]

    client = OpenAI(api_key=openai_api_key)
    prompt_tokens, completion_tokens, gpt_call_error, openai_response = call_gpt_api(
        args=None,
        openai_client=client,
        messages=messages
    )

    # 4) Return GPT's response or None if there was an error
    if gpt_call_error or not openai_response:
        logging.error("GPT call failed or returned error.")
        return ""
    else:
        return openai_response.choices[0].message.content
