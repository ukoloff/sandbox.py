#
# https://stepik.org/lesson/732063/step/4?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/5.5/2/1.html")

    for i in browser.find_elements(By.CSS_SELECTOR, "input:not([disabled])"):
        i.clear()

    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer)
