#
# https://stepik.org/lesson/732069/step/3?unit=733602
#
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("http://parsinger.ru/infiniti_scroll_2/")

    d = browser.find_element(By.ID, 'scroll-container')
    while not len(browser.find_elements(By.CLASS_NAME, 'last-of-list')):
      ActionChains(browser).send_keys_to_element(d, Keys.END).perform()

    summa = sum(int(s.text) for s in d.find_elements(By.TAG_NAME, 'p'))

    print(summa)
