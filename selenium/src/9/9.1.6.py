#
# https://stepik.org/lesson/732080/step/6?unit=733613
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
    browser.get("https://parsinger.ru/selenium/9/9.1.1/index.html")

    for b in browser.find_elements(By.TAG_NAME, 'button'):
        WebDriverWait(b, 10).until(EC.element_to_be_clickable(b)).click()

    ans = browser.find_element(By.ID, "message")
    print(ans.text)
