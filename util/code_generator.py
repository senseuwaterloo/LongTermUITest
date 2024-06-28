import json
import re
from collections import defaultdict
from jinja2 import FileSystemLoader, Environment
from website_config import website_dict


def test_code_generator(json_path):
    with open(json_path, 'r') as task_json_file:
        loaded_json_data = json.load(task_json_file)

    grouped_task_data = group_tasks_by_website(loaded_json_data)

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('TestTemplate.j2')

    for each_website, task_list in grouped_task_data.items():
        website_url, file_name, class_name, method_list = get_template_variables(each_website, task_list)
        output = template.render(website_url=website_url, class_name=class_name, method_list=method_list)
        with open("../resource/output/" + file_name, 'w') as f:
            f.write(output)


def get_template_variables(each_website, task_list):
    website_url = get_website_url(each_website)
    file_name = f"test_{split_merge_string(each_website)}.py"
    class_name = f"Test{split_capitalize_merge_string(each_website)}"
    method_list = []
    for each_task in task_list:
        annotation_id_prefix = each_task['annotation_id'].split('-')[0]
        method_name = f"test_{split_merge_string(each_website)}_{annotation_id_prefix}"
        action_list = []
        for action in each_task['actions']:
            operation = action['operation']['op']
            action_value = action['operation']['value']
            locator_type, first_locator = get_first_locator(action)
            if '"' in first_locator:
                first_locator = first_locator.replace('"', '\\"')
            if operation.lower() == "type":
                operation = "send_keys"
            if len(action_value) > 0:
                operation_code = f"self.driver.find_element(By.{locator_type.upper()}, \"{first_locator}\").{operation.lower()}(\"{action_value}\")"
                action_list.append(f"self.driver.find_element(By.{locator_type.upper()}, \"{first_locator}\").clear()")
                action_list.append(operation_code)
            else:
                operation_code = f"self.driver.find_element(By.{locator_type.upper()}, \"{first_locator}\").{operation.lower()}()"
                action_list.append(operation_code)

        method_list.append({
            "method_name": method_name,
            "operations": "\n        ".join(action_list)
        })

    return website_url, file_name, class_name, method_list


def get_website_url(website_name):
    if website_name in website_dict:
        confirmed_website_url = website_dict[website_name]
    elif (website_name.endswith('.gov') or website_name.endswith('.edu') or website_name.endswith('.org') or
          website_name.endswith('.uk') or website_name.endswith('.fm') or website_name.endswith('.info')):
        confirmed_website_url = "https://" + website_name
    else:
        confirmed_website_url = "https://" + website_name + ".com"

    return confirmed_website_url


def get_first_locator(action):
    locators = action['locators']
    # first_key = next(iter(locators))
    # first_locator = locators[first_key]
    locator_iterator = iter(locators.items())
    first_key, first_locator = next(locator_iterator)
    # Check and skip locators containing "link:///"
    while "link:///" in first_locator or "::" in first_locator:
        first_key, first_locator = next(locator_iterator, (None, None))
        if first_locator is None:
            raise ValueError("No valid locator found")

    if first_key == "id_locator":
        by_locator_type = "ID"
        if first_locator.startswith("id="):
            first_locator = first_locator[len("id="):]
    elif first_key == "name_locator":
        by_locator_type = "NAME"
        if first_locator.startswith("name="):
            first_locator = first_locator[len("name="):]
    else:
        by_locator_type = "XPATH"
        if first_locator.startswith("xpath="):
            first_locator = first_locator[len("xpath="):]

    return by_locator_type, first_locator


def group_tasks_by_website(json_data_to_group):
    tasks = json_data_to_group.get("task", [])
    grouped_tasks = defaultdict(list)

    # Group tasks by website
    for task in tasks:
        website = task.get("website")
        if website:  # Ensure the website is not None or empty
            grouped_tasks[website].append(task)

    return grouped_tasks


def split_capitalize_merge_string(website_url):
    parts = re.split(r'[.-]', website_url)
    capitalized_parts = [part.capitalize() for part in parts]
    merged_string = ''.join(capitalized_parts)

    return merged_string


def split_merge_string(website_url):
    parts = re.split(r'[.-]', website_url)
    merged_string = ''.join(parts)

    return merged_string


task_file = '../resource/tests_to_execute.json'
test_code_generator(task_file)
