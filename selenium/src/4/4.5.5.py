#
# https://stepik.org/lesson/731861/step/5?unit=733396
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/selenium/4/4.html")

    cbs = browser.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
    for cb in cbs:
        cb.click()

    btn = browser.find_element(By.CSS_SELECTOR, "input[type=button]")
    btn.click()

    out = browser.find_element(By.ID, "result")
    txt = out.text

    print(txt)
