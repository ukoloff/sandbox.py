#
# https://stepik.org/lesson/1121332/step/5?unit=1132820
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/9/9.6.2/index.html")

    browser.find_element(By.TAG_NAME, 'button').click()

    WebDriverWait(browser, 100).until(EC.text_to_be_present_in_element_value((By.ID, 'recipe_field'), "Селениумий"))

    ans = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'password')))
    print(ans.text)

