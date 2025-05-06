#
# https://stepik.org/lesson/732059/step/5?unit=733592
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/6/6.2.1/index.html")

    box = browser.find_element(By.ID, "this_pic")
    box.screenshot("c:\\temp\\6.1.5.png")
