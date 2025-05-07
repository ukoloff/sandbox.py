#
# https://stepik.org/lesson/732062/step/4?unit=733595
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/6/6.3.3/index.html")

    browser.add_cookie({"name": "secretKey", "value": "selenium123"})
    browser.refresh()

    out = browser.find_element(By.ID, "password")
    print(out.text)
