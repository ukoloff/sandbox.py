#
# https://stepik.org/lesson/1121333/step/5?unit=1132821
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.7.2/index.html")

    addr = browser.find_element(By.TAG_NAME, "input")
    addr.clear()
    addr.send_keys('test')

    browser.find_element(By.TAG_NAME, "button").click()

    browser.find_element(By.TAG_NAME, 'button').click()

    res = browser.find_element(By.ID, 'old-result')

    WebDriverWait(browser, 6).until(EC.staleness_of(res))

    browser.find_element(By.ID, 'secret-button').click()

    ans = browser.find_element(By.ID, 'result')
    print(ans.text)
