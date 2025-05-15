#
# https://stepik.org/lesson/1121331/step/5?unit=1132819
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
    browser.get("https://parsinger.ru/selenium/9/9.5.2/index.html")

    btn = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "button")))
    btn.click()

    ans = browser.find_element(By.ID, 'password-display')
    print(ans.text)

