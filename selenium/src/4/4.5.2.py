#
# https://stepik.org/lesson/731861/step/2?unit=733396
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/selenium/2/2.html")

    link = browser.find_element(By.LINK_TEXT, "16243162441624")
    link.click()

    out = browser.find_element(By.ID, "result")
    txt = out.text

    print(txt)
