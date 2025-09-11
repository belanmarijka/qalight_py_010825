# xpath
import re
import requests
from lxml import html

text1 = "Телефонний номер: (123) 456-7890"
text2 = "Телефонний номер: (123) 456-78-90"
text3 = "Телефонний номер: (123)456-78-90"

pattern_0 = r"\(\d{3}\)\s\d{3}-\d{4}"
pattern = r"\(\d{3}\)\s?\d{3}-?\d{2}-?\d{2}"


def find_by_reg(*texts, pattern=pattern):
    for t in texts:
        match = re.search(pattern, t)
        if match:
            phone_number = match.group()
            print("Знайдено номер телефону:", phone_number)


def get_html_content(url:str) -> str:
    response = requests.get(url)
    return response.text


def get_tree(html_text:str):
    return html.fromstring(html_text)


def find_by(tree, locator, by_text=True):
    if by_text:
        return tree.findtext(locator)
    else:
        return tree.xpath(locator)


if __name__ == "__main__":
    url = "https://lxml.de/"
    content = get_html_content(url)
    print(content)
    tree = get_tree(content)
    title = find_by(tree, './/title', False)
    print("Заголовок сторінки:", title[0].text)
    link = find_by(tree, './/a/@href', False)
    print("Посилання:", len(link))

    find_by_reg(text1, text2, text3)
