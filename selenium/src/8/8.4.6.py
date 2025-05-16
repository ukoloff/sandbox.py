#
# https://stepik.org/lesson/1121307/step/6?unit=1132795
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/8/8.4.3/index.html")

    for n in range(4):
        i = browser.find_element(By.TAG_NAME, "iframe")
        browser.switch_to.frame(i)
        browser.find_element(By.TAG_NAME, "button").click()

    ans = browser.find_element(By.CLASS_NAME, "password-container")
    print(ans.text)
