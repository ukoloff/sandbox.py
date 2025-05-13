#
# https://stepik.org/lesson/732067/step/6?unit=733600
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/7/7.3.2/index.html")

    src = browser.find_element(By.ID, "dblclick-area")
    ActionChains(browser).double_click(src).perform()

    ans = browser.find_element(By.ID, 'password').text
    print(ans)
