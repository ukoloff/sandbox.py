import os
from os.path import join, dirname
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


load_dotenv(join(dirname(__file__), ".env"))


def tel(ip):
    chrome_options = Options()
    chrome_options.add_argument("--disable-auto-update")
    chrome_options.add_argument("--ignore-certificate-errors")
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.implicitly_wait(3)
        browser.get(f"https://{ip}")

        login = browser.find_elements(By.ID, 'idUsername')
        if len(login) != 1:
            print("Authorization form not found")
        login[0].send_keys(os.getenv('SIP_USER'))
        browser.find_element(By.ID, 'idPassword').send_keys(os.getenv('SIP_PASS'))
        browser.find_element(By.ID, 'idConfirm').click()

def main():
    tel("10.172.202.31")


if __name__ == "__main__":
    main()
