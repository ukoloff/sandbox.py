#
# https://stepik.org/lesson/732083/step/4?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.9/2/index.html")

    el = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'qQm9y1rk')))
    el.click()
    ans = browser.switch_to.alert.text
    print(ans)
