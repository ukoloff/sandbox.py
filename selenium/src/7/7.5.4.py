#
# https://stepik.org/lesson/732069/step/4?unit=733602
#
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/infiniti_scroll_3/")

    for d in browser.find_elements(By.CSS_SELECTOR, '[class^=scroll-container_]'):
      cnt = None
      while True:
        ActionChains(browser).send_keys_to_element(d, Keys.END).pause(0.1).perform()
        num = len(d.find_elements(By.TAG_NAME, 'span'))
        if num == cnt:
           break
        cnt = num


    summa = sum(int(s.text) for s in browser.find_elements(By.TAG_NAME, 'span'))

    print(summa)
