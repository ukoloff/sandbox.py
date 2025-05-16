#
# https://stepik.org/lesson/1121307/step/5?unit=1132795
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/8/8.4.2/index.html")

    for n in range(3):
        i = browser.find_elements(By.TAG_NAME, "iframe")[-1]
        browser.switch_to.frame(i)
        browser.find_element(By.TAG_NAME, "button").click()
        browser.switch_to.default_content()

    i = browser.find_elements(By.TAG_NAME, "iframe")[-1]
    browser.switch_to.frame(i)

    ans = browser.find_element(By.TAG_NAME, "h2")
    print(ans.text)
