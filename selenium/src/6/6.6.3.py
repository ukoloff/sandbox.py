#
# https://stepik.org/lesson/732063/step/3?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/methods/3/index.html")

    result = 0
    for ck in browser.get_cookies():
        name = ck['name'][-1]
        if name.isnumeric() and int(name) % 2 == 0:
            result += int(ck['value'])
    print(result)
