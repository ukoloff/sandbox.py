import os
import re
import csv
import ipaddress
import datetime
from os.path import join, dirname
import socket
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


load_dotenv(join(dirname(__file__), ".env"))


def tdelta(delta):
    """
    Format timedelta
    """
    res = re.sub(r"^[0:]+", "", str(delta).split(".")[0])
    if not res:
        res = "0"
    return res


reportLabels = "AccountUserName AccountRegisterName AccountLabel AccountDisplayName".split()


def tel(ip):
    chrome_options = Options()
    chrome_options.add_argument("--disable-auto-update")
    chrome_options.add_argument("--ignore-certificate-errors")
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.implicitly_wait(5)
        browser.get(f"https://{ip}")

        btns = browser.find_elements(By.ID, "idConfirm")
        if len(btns) != 1:
            return "Authorization form not found"

        browser.find_element(By.CSS_SELECTOR, "#idUsername, [name=username]").send_keys(
            os.getenv("SIP_USER")
        )
        browser.find_element(By.CSS_SELECTOR, "#idPassword, [name=pwd]").send_keys(
            os.getenv("SIP_PASS")
        )
        btns[0].click()

        tabs = browser.find_elements(By.CSS_SELECTOR, "#Account, #account")
        if len(tabs) != 1:
            return "Authorization failed"
        tabs[0].click()

        res = []
        for name in reportLabels:
            txt = browser.find_element(By.NAME, name).get_attribute("value")
            res.append(txt)
        return res


def testNC(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        res = s.connect_ex((ip, 443))
        return res == 0


def IP(ip):
    if not testNC(ip):
        return "Not responding"
    return tel(ip)


def walkIPs(network="10.172.200.0/22"):
    start = datetime.datetime.now()
    logfile = join(
        dirname(__file__),
        "logs",
        f"{start.strftime('sip-%Y-%m-%d-%H-%M-%S')}.log",
    )
    with open(logfile, "a", encoding="utf-8") as log:
        print("Start:", start.isoformat(" "), file=log)
        for ip in ipaddress.ip_network(network).hosts():
            now = datetime.datetime.now()
            print(ip, end="\t", flush=True)
            try:
                res = IP(str(ip))
            except Exception as e:
                res = str(e).splitlines()[0]
            print(f"{ip}<+{tdelta(now - start)}>:\t{res}", file=log, flush=True)
        stop = datetime.datetime.now()
        print(f"End<+{tdelta(stop - start)}>:", stop.isoformat(" "), file=log)


def main():
    global exts
    exts = readCSV()
    walkIPs()
    # tel("10.172.202.31")


def readCSV():
    src = join(dirname(__file__), "data", "omz2sinara.csv")
    with open(src) as f:
        reader = csv.DictReader(f, delimiter=";")
        return dict((row["Внутр. Номер"], row) for row in reader)


if __name__ == "__main__":
    main()
