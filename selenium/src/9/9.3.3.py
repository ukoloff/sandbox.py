#
# https://stepik.org/lesson/1121328/step/3?unit=1132816
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(7)
    browser.get("http://parsinger.ru/selenium/9/9.3.1/index.html")

    browser.find_element(By.ID, 'startButton').click()

    for i in range(5):
      browser.find_element(By.ID, 'dynamicButton').click()

    ans = browser.find_element(By.ID, "secretPassword")
    print(ans.text)
