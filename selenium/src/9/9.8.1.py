#
# https://stepik.org/lesson/732083/step/1?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("http://parsinger.ru/expectations/3/index.html")

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
    WebDriverWait(browser, 100, poll_frequency=0.1).until(EC.title_is("345FDG3245SFD"))

    ans = browser.find_element(By.ID, "result")
    print(ans.text)
