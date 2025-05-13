#
# https://stepik.org/lesson/732069/step/1?unit=733602
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/scroll/2/index.html")

    for b in browser.find_elements(By.TAG_NAME, 'input'):
        b.click()

    summa = sum(int(s.text) for s in browser.find_elements(By.TAG_NAME, 'span') if s.text)

    print(summa)
