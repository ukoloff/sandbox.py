#
# https://stepik.org/lesson/732069/step/5?unit=733602
#
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.7/1/index.html")

    for b in browser.find_elements(By.TAG_NAME, 'button'):
      b.click()

    ans = browser.switch_to.alert.text

    print(ans)
