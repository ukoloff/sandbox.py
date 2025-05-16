#
# https://stepik.org/lesson/732069/step/2?unit=733602
#
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("http://parsinger.ru/infiniti_scroll_1/")

    d = browser.find_element(By.ID, 'scroll-container')
    while not len(browser.find_elements(By.CLASS_NAME, 'last-of-list')):
      d.send_keys(Keys.END)

    summa = sum(int(s.text) for s in d.find_elements(By.TAG_NAME, 'span'))

    print(summa)
