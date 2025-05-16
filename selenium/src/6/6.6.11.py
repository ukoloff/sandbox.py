#
# https://stepik.org/lesson/732063/step/11?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/methods/3/index.html")

    summa = 0
    for c in browser.get_cookies():
        if not c["name"].startswith("secret_cookie_"):
            continue
        summa += int(c["value"])
    print(summa)
