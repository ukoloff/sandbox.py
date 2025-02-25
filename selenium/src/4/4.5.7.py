#
# https://stepik.org/lesson/731861/step/7?unit=733396
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/selenium/7/7.html")

    oz = browser.find_elements(By.TAG_NAME, "option")
    res = sum(int(o.text) for o in oz)

    out = browser.find_element(By.ID, "input_result")
    out.clear()
    out.send_keys(str(res))

    btn = browser.find_element(By.ID, "sendbutton")
    btn.click()

    out = browser.find_element(By.ID, "result")
    txt = out.text

    print(txt)
