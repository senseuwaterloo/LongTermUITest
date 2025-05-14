import os
import re
from util.website_config import website_dict


def convert_class_name(class_name):
    if class_name.startswith("Test"):
        class_name = class_name[4:]

    domain_name = re.findall(r'[A-Z][a-z]*', class_name)
    result = ''.join(domain_name).lower()
    return result


def get_website_url(website_name):
    if website_name in website_dict:
        confirmed_website_url = website_dict[website_name]
    elif (website_name.endswith('.gov') or website_name.endswith('.edu') or website_name.endswith('.org') or
          website_name.endswith('.uk') or website_name.endswith('.fm') or website_name.endswith('.info')):
        confirmed_website_url = "https://" + website_name
    else:
        confirmed_website_url = "https://" + website_name + ".com"

    return confirmed_website_url


def get_next_execution_number():
    testoutput_dir = "testoutput"
    if not os.path.exists(testoutput_dir):
        os.makedirs(testoutput_dir)
        return 1
    existing_folders = [name for name in os.listdir(testoutput_dir) if os.path.isdir(os.path.join(testoutput_dir, name))]
    execution_numbers = [int(folder.replace("execution", "").split('_')[0]) for folder in existing_folders if folder.startswith("execution")]
    if execution_numbers:
        return max(execution_numbers) + 1
    return 1
