#
# https://stepik.org/lesson/732078/step/5?unit=733611
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/8/8.3.1/index.html")

    bs = browser.find_elements(By.TAG_NAME, "button")

    bs[0].click()
    sleep(0.3)
    browser.switch_to.alert.accept()

    bs[1].click()
    sleep(0.3)
    browser.switch_to.alert.send_keys("Alert")
    browser.switch_to.alert.accept()

    bs[2].click()
    sleep(0.3)
    browser.switch_to.alert.accept()

    sleep(1)

    ans = browser.find_element(By.ID, "secretKey").text
    print(ans)
