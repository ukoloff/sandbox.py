#
# https://stepik.org/lesson/732061/step/6?unit=733594
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/6/6.3.2/index.html")

    browser.delete_all_cookies()

    out = browser.find_element(By.ID, "password")
    print(out.text)
