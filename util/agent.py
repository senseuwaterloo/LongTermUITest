import os
import logging
from openai import OpenAI
from util.llm_helper import encode_image, call_gpt_api


def call_gpt_for_candidate_fixes(
    test_name: str,
    class_name: str,
    failing_url: str,
    screenshot_path: str,
    web_elements_text: str,
    traceback_text: str,
    logging_output: str,
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

    # "IMPORTANT: Do not use ellipsis ('...') to indicate omitted code. Always provide the full, exact code lines before and after the change without abbreviation."
    # task_description = "finding the lowest travel time flight for 1 traveler from JFK, NYC to Heathrow, London on 04/19/2025, then from Heathrow, London to CDG, Paris on 04/21/2025 and then from CDG, Paris to JFK, NYC on 04/23/2025"
    system_msg = {
        "role": "system",
        "content": (
            "You are a helpful assistant for debugging Selenium test failures. "
            "At each stage, imagine you have the webpage screenshot where the test case fails (like a human looking at the browser), "
            "the output of the test execution, the failing test line, and the entire test method code. "
            "Your goal is to propose multiple short, concise, and actionable code or configuration changes that might fix the test. "
            "For each suggestion, provide the following in the exact format:\n"
            "-------------------------------------------------------\n"
            "Potential fix (X): [brief description of suggestion]\n"
            "Original code line/lines: [exact original code line(s) that should be replaced]\n"
            "Fixed code line/lines: [replacement code line(s) or patch/diff with sufficient context]\n"
            "-------------------------------------------------------\n"
            "Limit your output to a maximum of 5 suggestions (it doesn't have to always be five) and terminate your answer after listing them. "
            "Each suggestion must be a short, direct, concise, and actionable code change, not vague commentary, redundant fixes or pseudo answers. "
            "If you believe the issue is with an element locator, and if the broken element appears in the provided HTML textual list of interactable elements "
            "(each element corresponds to the one annotated with numbered boxes in the screenshot), generate a new robust locator using that information. "
            "Keep your commentary minimal—just enough to clarify each solution. "
            "Note: The find_element and click methods have already been overridden to implement "
            "dynamic waiting and to ignore most exceptions within the assigned timeout. Please do not suggest changes that duplicate "
            "this behavior unless absolutely necessary.\n\n"
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
                    f"URL at failure: {failing_url},\n"
                    f"Logs from the test execution:\n"
                    f"{logging_output}\n\n"
                    "Below is the screenshot of the page where the test case fails, with interactable elements annotated. "
                    "You also have a textual list of those elements.\n\n"
                    "Apart from the annotated elements, please pay attention to any warning or error messages on the page "
                    "that might indicate the root cause. Note that the root cause may not always lie in the code line where the test failed; "
                    "it could also stem from previous steps in the test.\n\n"
                    "Additionally, here is the entire test method code and the specific failing line:\n\n"
                    f"--- Test Method Source ---\n{test_method_source}\n\n"
                    f"--- Failing Line ---\n{failing_line_code}\n\n"
                    "Please propose UP TO 5 possible code or configuration fixes that might solve the test failure.\n\n"
                    f"Textual list of clickable HTML elements annotated in the screenshot:\n{web_elements_text}\n"
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
