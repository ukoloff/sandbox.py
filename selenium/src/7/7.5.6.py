#
# https://stepik.org/lesson/732069/step/6?unit=733602
#
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.7/5/index.html")

    for b in browser.find_elements(By.TAG_NAME, "button"):
        ActionChains(browser).click_and_hold(b).pause(float(b.text) + 0.1).release(
            b
        ).perform()

    ans = browser.switch_to.alert.text

    print(ans)
