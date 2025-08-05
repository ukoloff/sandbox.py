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
from selenium.webdriver.common.action_chains import ActionChains


load_dotenv(join(dirname(__file__), ".env"))


def tdelta(delta):
    """
    Format timedelta
    """
    res = re.sub(r"^[0:]+", "", str(delta).split(".")[0])
    if not res:
        res = "0"
    return res


def tel(ip):
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--ignore-certificate-errors")
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.implicitly_wait(5)
        browser.get(f"https://{ip}")

        btns = browser.find_elements(By.CSS_SELECTOR, "#idConfirm, #idLogin")
        if len(btns):
            match btns[0].get_attribute("id"):
                case "idConfirm":
                    return telDef(browser)
                case "idLogin":
                    return telAdv(browser)
        return "Authorization form not found"


reportLabels = (
    "AccountUserName AccountRegisterName AccountLabel AccountDisplayName".split()
)


def telDef(browser):
    browser.find_element(By.CSS_SELECTOR, "#idUsername, [name=username]").send_keys(
        os.getenv("SIP_USER")
    )
    browser.find_element(By.CSS_SELECTOR, "#idPassword, [name=pwd]").send_keys(
        os.getenv("SIP_PASS")
    )
    browser.find_element(By.ID, "idConfirm").click()

    tabs = browser.find_elements(By.CSS_SELECTOR, "#Account, #account")
    if len(tabs) != 1:
        return "Authorization failed"
    tabs[0].click()

    return telProcess(
        [browser.find_element(By.NAME, name) for name in reportLabels],
        browser.find_element(By.CSS_SELECTOR, "#btn_confirm1, [name=btnSubmit]"),
    )


def telAdv(browser):
    browser.find_element(By.ID, "idUsername").send_keys(os.getenv("SIP_USER"))
    browser.find_element(By.ID, "idPassword").send_keys(os.getenv("SIP_PASS"))
    browser.find_element(By.ID, "idLogin").click()

    tabs = browser.find_elements(By.ID, "Account")
    if len(tabs) != 1:
        return "Authorization failed"
    tabs[0].click()

    browser.find_element(By.ID, "AccountRegister").click()

    ActionChains(browser).pause(1).perform()

    return telProcess(
        [
            browser.find_element(By.CSS_SELECTOR, f"[name={name}] input")
            for name in reportLabels
        ],
        browser.find_element(By.CSS_SELECTOR, "#y-submit-confirm button"),
    )


def telProcess(inputs, button):
    ext = inputs[0].get_attribute("value")
    if ext not in exts:
        return f"Skipped:\t{[el.get_attribute('value') for el in inputs]}"
    extension = exts[ext]
    num = extension["extension new"]
    fio = extension["name"]
    data = [num, num, f"{num} {fio}", fio]
    for i, v in zip(inputs, data):
        i.clear()
        i.send_keys(v)
    if 0:
      button.click()
      ActionChains(button.parent).pause(1).perform()
    return f"Patch:\t {ext} -> {data}"


def testNC(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
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
        return dict((row["extension"], row) for row in reader)


if __name__ == "__main__":
    main()
