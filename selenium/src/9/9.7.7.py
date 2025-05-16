#
# https://stepik.org/lesson/1121333/step/7?unit=1132821
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.7.3/index.html")

    browser.find_element(By.TAG_NAME, "button").click()

    WebDriverWait(browser, 20).until(EC.number_of_windows_to_be(5))

    browser.find_element(By.CLASS_NAME, 'password-btn').click()

    WebDriverWait(browser, 20).until(EC.alert_is_present())

    ans = browser.switch_to.alert.text
    print(ans)
