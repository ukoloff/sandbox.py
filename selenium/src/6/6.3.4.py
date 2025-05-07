#
# https://stepik.org/lesson/732061/step/4?unit=733594
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/6/6.3.1/index.html")

    cookie = browser.get_cookie('token_22')['value']
    print(cookie)
