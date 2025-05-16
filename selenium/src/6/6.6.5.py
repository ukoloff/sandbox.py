#
# https://stepik.org/lesson/732063/step/5?unit=733596
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/methods/5/index.html")

    hrefs = [i.get_attribute('href') for i in browser.find_elements(By.TAG_NAME, "a")]

    max_exp = None
    max_value = None

    for url in hrefs:
        browser.get(url)
        exp = max(cookie['expiry'] for cookie in browser.get_cookies() if cookie.get('expiry'))
        if max_exp is None or exp > max_exp:
            max_exp = exp
            max_value = browser.find_element(By.ID, 'result').text
    print(max_value)
