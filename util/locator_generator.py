import re
import json
from bs4 import BeautifulSoup
from typing import Optional
from lxml import etree, html
from lxml.etree import XPathEvalError


def attribute_value(attr_value: str) -> str:
    # Check for simple cases first.
    if "'" not in attr_value:
        return f"'{attr_value}'"
    elif "\"" not in attr_value:
        return f"\"{attr_value}\""
    else:
        result = "concat("
        mutable_value = attr_value
        did_reach_end_of_value = False

        while not did_reach_end_of_value:
            apos = mutable_value.find("'")
            quot = mutable_value.find("\"")

            if apos < 0:
                result += f"'{mutable_value}'"
                did_reach_end_of_value = True
            elif quot < 0:
                result += f"\"{mutable_value}\""
                did_reach_end_of_value = True
            else:
                # Determine the earliest quote in the string and split accordingly.
                if quot < apos:
                    part = mutable_value[:quot]
                    result += f"\"{part}\""
                    mutable_value = mutable_value[quot + 1:]
                else:
                    part = mutable_value[:apos]
                    result += f"'{part}'"
                    mutable_value = mutable_value[apos + 1:]

            # Add a comma between parts unless it's the end of the string.
            if not did_reach_end_of_value:
                result += ","

        result += ")"
        return result


def get_node_nbr(current) -> int:
    parent_node = current.getparent()
    if parent_node is None:
        return -1
    child_nodes = parent_node.getchildren()
    total = 0
    index = -1
    for i, child in enumerate(child_nodes):
        if child.tag == current.tag:
            if child == current:
                index = total
            total += 1
    return index


def relative_xpath_from_parent(current_element):
    """Generate the relative XPath from the parent to the current element."""
    index = get_node_nbr(current_element)
    current_path = f"/{current_element.tag.lower()}"
    if index >= 0:
        current_path += f"[{index + 1}]"
    return current_path


class LocatorGenerator:

    def __init__(self, document: str):
        # Parse the document with BeautifulSoup
        self.soup = BeautifulSoup(document, 'lxml')
        # Convert the BeautifulSoup object to a string and then parse it with lxml
        self.document = etree.fromstring(str(self.soup), etree.HTMLParser())

    def find_element(self, path: str) -> Optional[etree._Element]:
        # print("In find_element")
        # print(path)
        try:
            elements = self.document.xpath(path)
            if elements:
                return elements[0]
            else:
                print("No elements found for the given XPath.")
                return None
        except XPathEvalError as e:
            # if this error then do not use this locator
            print("Error evaluating XPath:", e)
            return None

    def precise_xpath(self, xpath: str, el: etree._Element) -> str:
        if self.find_element(xpath) != el:
            elements = self.document.xpath(xpath)
            for i, element in enumerate(elements):
                # In lxml, the XPath index is 1-based, not 0-based.
                new_path = f"({xpath})[{i + 1}]"
                matched_elements = self.find_element(new_path)
                if len(matched_elements) != 0 and matched_elements[0].get("data-pw-testid-buckeye") == el.get("data-pw-testid-buckeye"):
                    return new_path
        return xpath

    # Example method to generate a simple locator based on an element's ID
    def id_locator(self, el: etree._Element) -> Optional[str]:
        element_id = el.get('id')
        if element_id:
            elements_by_id = self.document.xpath(f"//*[@id='{element_id}']")
            if len(elements_by_id) == 1:
                return f"id={element_id}"
        return ""

    def xpath_link(self, element: etree._Element) -> str:
        if element.tag.lower() == "a":
            text_content = element.text.strip() if element.text else ""
            # Check if text_content is not just whitespace
            if text_content and not re.match("^\\s*$", text_content):
                return self.precise_xpath(f"//a[contains(text(),{attribute_value(text_content)})]", element)
        return ""

    def name_locator(self, el: etree._Element) -> str:
        name_attr = el.get('name')
        if name_attr:
            return f"name={name_attr}"
        return ""

    def link_text(self, el: etree._Element) -> str:
        if el.tag.lower() == "a":
            text = el.text.strip()
            if text and not text.isspace():
                cleaned_text = text.replace('\u00A0', ' ').strip()
                return f"linkText={cleaned_text}"
        return ""

    def xpath_img(self, el: etree._Element) -> str:
        if el.tag.lower() == "img":
            alt = el.get('alt')
            title = el.get('title')
            if alt:
                return self.precise_xpath(f"//img[@alt={attribute_value(alt)}]", el)
            elif title:
                return self.precise_xpath(f"//img[@title={attribute_value(title)}]", el)
            else:
                return self.xpath_position(el)
        return ""

    def xpath_attr(self, el: etree._Element) -> str:
        preferred_attributes = ["role", "name", "value", "type", "action", "placeholder", "title", "data-selenium"]
        attrs_map = {attr: el.get(attr) for attr in el.keys() if attr in preferred_attributes}
        names = [name for name in preferred_attributes if name in attrs_map]
        for name in names:
            if name in attrs_map:
                locator = self.attributes_xpath(el.tag, names, attrs_map, el)
                if self.find_element(locator).get("data-pw-testid-buckeye") == el.get("data-pw-testid-buckeye"):
                    return locator
        return ""

    def attributes_xpath(self, tag_name: str, att_names: list, attributes: dict, el: etree._Element) -> str:
        locator = f"//{tag_name.lower()}["
        conditions = [f"@{att}={attribute_value(attributes[att])}" for att in att_names]
        locator += " and ".join(conditions)
        locator += "]"
        return self.precise_xpath(locator, el)

    def xpath_id_relative(self, el: etree._Element) -> str:
        path = ""
        current = el
        while current is not None:
            parent = current.getparent()
            if parent is not None:
                path = relative_xpath_from_parent(current) + path
                parent_id = parent.get('id')
                if parent_id:
                    return self.precise_xpath(f"//{parent.tag.lower()}[@id={attribute_value(parent_id)}]{path}", el)
            current = parent
        return ""

    def xpath_href(self, el: etree._Element) -> str:
        href = el.get('href', '')
        if href:
            if href.startswith(('http://', 'https://')):
                return self.precise_xpath(f"//a[@href={attribute_value(href)}]", el)
            else:
                return self.precise_xpath(f"//a[contains(@href, {attribute_value(href)})]", el)
        return ""

    def xpath_position(self, el: etree._Element) -> str:
        components = []
        current = el
        while current is not None and not isinstance(current, html.HtmlElement):
            components.append(relative_xpath_from_parent(current))
            current = current.getparent()
        components.reverse()  # Reverse to get the order from root to the element
        xpath = "".join(components)
        if self.find_element(xpath) is not None and self.find_element(xpath).get("data-pw-testid-buckeye") == el.get("data-pw-testid-buckeye"):
            return f"xpath={xpath}"

        return ""

    def xpath_inner_text(self, el: etree._Element) -> str:
        inner_text = el.text
        if inner_text and not re.match("^\\s*$", inner_text):
            return f"//{el.tag.lower()}[contains(.,{attribute_value(inner_text.strip())})]"
        return ""

    def get_all_locator(self, el: etree._Element) -> str:
        locator = {}
        id_locator = self.id_locator(el)
        if id_locator != "":
            locator['id_locator'] = id_locator
        xpath_link = self.xpath_link(el)
        if xpath_link != "":
            locator['xpath_link'] = xpath_link
        xpath_attribute = self.xpath_attr(el)
        if xpath_attribute != "":
            locator['xpath_attribute'] = xpath_attribute
        xpath_id_relative = self.xpath_id_relative(el)
        if xpath_id_relative != "":
            locator['xpath_id_relative'] = xpath_id_relative
        xpath_img = self.xpath_img(el)
        if xpath_img != "":
            locator['xpath_img'] = xpath_img
        xpath_href = self.xpath_href(el)
        if xpath_href != "":
            locator['xpath_href'] = xpath_href
        xpath_inner_text = self.xpath_inner_text(el)
        if xpath_inner_text != "":
            locator['xpath_inner_text'] = xpath_inner_text
        name_locator = self.name_locator(el)
        if name_locator != "":
            locator['name_locator'] = name_locator
        xpath_position = self.xpath_position(el)
        if xpath_position != "":
            locator['xpath_position'] = xpath_position

        # use neighbour and/or parent child text based locator and neighbour/parent/child attribute based locator

        return json.dumps(locator)

