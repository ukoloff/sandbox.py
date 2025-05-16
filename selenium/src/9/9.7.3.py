#
# https://stepik.org/lesson/1121333/step/3?unit=1132821
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.7.1/index.html")

    addr = browser.find_element(By.TAG_NAME, "input")
    addr.clear()
    addr.send_keys('USSR!')

    meth = Select(browser.find_element(By.TAG_NAME, "select"))
    meth.select_by_index(1)

    browser.find_element(By.TAG_NAME, 'button').click()

    WebDriverWait(browser, 15).until(EC.invisibility_of_element_located((By.ID, 'spinner')))

    browser.find_element(By.ID, 'confirm-address').click()

    WebDriverWait(browser, 5).until(EC.invisibility_of_element_located((By.ID, 'modal')))

    browser.find_element(By.ID, 'get-code').click()

    ans = browser.find_element(By.ID, 'result')
    print(ans.text)
