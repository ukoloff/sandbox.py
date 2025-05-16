#
# https://stepik.org/lesson/732061/step/5?unit=733594
#
from selenium import webdriver
from selenium.webdriver.common.by import By

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/6/6.3/index.html")

    for cookie in browser.get_cookies():
        if cookie["value"] == "true":
            song = cookie["name"]

    input = browser.find_element(By.ID, "phraseInput")
    input.clear()
    input.send_keys(song)

    browser.find_element(By.TAG_NAME, "button").click()

    out = browser.find_element(By.ID, "result")
    print(out.text)
