#
# https://stepik.org/lesson/732076/step/3?unit=733609
#
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("about:blank")

    browser.switch_to.new_window("site1")
    browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
    t1 = re.sub("[439]", "", browser.title)
    browser.switch_to.new_window("site2")
    browser.get("https://parsinger.ru/selenium/8/8.1/site2/")
    t2 = re.sub("[780]", "", browser.title)

    ans = int(t1) + int(t2)
    print(ans)
