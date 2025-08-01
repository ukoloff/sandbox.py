import os
import csv
import ipaddress
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

        login = browser.find_elements(By.ID, "idUsername")
        if len(login) != 1:
            print("Authorization form not found")
        login[0].send_keys(os.getenv("SIP_USER"))
        browser.find_element(By.ID, "idPassword").send_keys(os.getenv("SIP_PASS"))
        browser.find_element(By.ID, "idConfirm").click()

        browser.find_element(By.ID, "Account").click()

        for name in "AccountLabel AccountRegisterName AccountUserName".split():
            txt = browser.find_element(By.NAME, name).get_attribute("value")
            print(txt)


def readCSV():
    global exts
    exts = readCSV()


def walkIPs(network="10.172.200.0/22"):
    for ip in ipaddress.ip_network(network).hosts():
        print(ip)


def main():
    readCSV()
    walkIPs()
    tel("10.172.202.31")


def readCSV():
    src = join(dirname(__file__), "data", "omz2sinara.csv")
    with open(src) as f:
        reader = csv.DictReader(f, delimiter=";")
        return dict((row["Внутр. Номер"], row) for row in reader)


if __name__ == "__main__":
    main()
