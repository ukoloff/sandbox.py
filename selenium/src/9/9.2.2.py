#
# https://stepik.org/lesson/732087/step/2?unit=733620
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.2.1/index.html")

    browser.find_element(By.TAG_NAME, 'button').click()

    WebDriverWait(browser, 100).until(EC.title_is("Access Granted"))

    ans = browser.find_element(By.CLASS_NAME, "highlight")
    print(ans.text)
