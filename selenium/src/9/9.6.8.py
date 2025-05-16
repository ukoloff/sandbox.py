#
# https://stepik.org/lesson/1121332/step/8?unit=1132820
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.6.4/index.html")

    img = WebDriverWait(browser, 100).until(
        EC.element_attribute_to_include((By.ID, "booking-number"), "confirmed")
    )
    n = browser.find_element(By.ID, "booking-number").text

    inp = browser.find_element(By.TAG_NAME, 'input')
    inp.clear()
    inp.send_keys(n)
    browser.find_element(By.TAG_NAME, 'button').click()

    ans = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "password-value"))
    )
    print(ans.text)
