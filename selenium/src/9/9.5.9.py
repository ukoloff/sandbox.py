#
# https://stepik.org/lesson/1121331/step/9?unit=1132819
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.5.3/index.html")

    browser.find_element(By.ID, 'showProducts').click()

    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product")))
    summa = 0
    for price in browser.find_elements(By.CLASS_NAME, 'price'):
        summa += int(price.text[1:])

    ans = browser.find_element(By.ID, 'sumInput')
    ans.clear()
    ans.send_keys(summa)
    browser.find_element(By.ID, 'checkSum').click()
    sleep(1)

    ans = browser.find_element(By.ID, 'secretMessage')
    print(ans.text)

