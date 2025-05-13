#
# https://stepik.org/lesson/732065/step/6?unit=733598
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/7/7.1/index.html")

    h = browser.execute_script("return document.body.scrollHeight")
    browser.execute_script("scrollTo(0, arguments[0])", h)

    sleep(1)
    ans = browser.find_element(By.ID, 'secret-container').text
    print(ans)
