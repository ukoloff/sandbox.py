#
# https://stepik.org/lesson/732063/step/7?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("http://parsinger.ru/scroll/4/index.html")

    res = browser.find_element(By.ID, 'result')

    summa = 0

    for b in browser.find_elements(By.TAG_NAME, "button"):
        browser.execute_script('arguments[0].scrollIntoView(true)', b)
        b.click()
        summa += int(res.text)
    print(summa)
