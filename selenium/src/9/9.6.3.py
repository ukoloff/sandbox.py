#
# https://stepik.org/lesson/1121332/step/3?unit=1132820
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.6.1/index.html")

    WebDriverWait(browser, 100).until(EC.text_to_be_present_in_element((By.ID, 'usd-rate'), "75.50 ₽"))
    ans = browser.find_element(By.ID, 'secret-code')
    print(ans.text)

