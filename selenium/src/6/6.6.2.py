#
# https://stepik.org/lesson/732063/step/2?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/5.5/1/1.html")

    for i in browser.find_elements(By.CLASS_NAME, 'text-field'):
        i.clear()

    browser.find_element(By.TAG_NAME, 'button').click()

    answer = browser.switch_to.alert.text
    print(answer)
