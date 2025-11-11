#
# Выключение ручной настройки VLAN и переход на DHCP/132
#
import os
import re
import ipaddress
import datetime
from os.path import join, dirname
import socket
from multiprocessing import Process, Queue
import queue
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

load_dotenv(join(dirname(__file__), ".env"))
start = datetime.datetime.now()


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


aLabels = "AccountUserName AccountRegisterName AccountLabel AccountDisplayName".split()


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

    result = {
        "m": "std",
        "title": browser.title,
        "label": browser.find_element(By.NAME, "AccountLabel").get_attribute("value"),
    }

    browser.find_elements(By.CSS_SELECTOR, "#Network, #network")[0].click()
    browser.find_elements(By.CSS_SELECTOR, "#network-adv, #network-advanced")[0].click()

    result["vlan"] = (
        browser.find_element(By.NAME, "VlanWanSwitch").get_attribute("selectedIndex")
        != "0"
    )
    result["vlanID"] = browser.find_element(By.NAME, "VlanWanVid").get_attribute(
        "value"
    )
    result["dhcp"] = (
        browser.find_element(By.NAME, "VlanDhcpSwitch").get_attribute("selectedIndex")
        != "0"
    )
    result["dhcpOption"] = browser.find_element(
        By.NAME, "VlanDhcpOption"
    ).get_attribute("value")

    if not result["vlan"] and result["dhcp"] and result["dhcpOption"] == "132":
        return result

    Select(browser.find_element(By.NAME, "VlanWanSwitch")).select_by_index(0)
    Select(browser.find_element(By.NAME, "VlanDhcpSwitch")).select_by_index(1)
    Select(browser.find_element(By.NAME, "LLDPSwitch")).select_by_index(0)
    Select(browser.find_element(By.NAME, "CDPEnable")).select_by_index(0)
    z = browser.find_element(By.NAME, "VlanDhcpOption")
    z.clear()
    z.send_keys("132")

    return result


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

    result = {
        "m": "adv",
        "title": browser.title,
        "label": browser.find_element(
            By.CSS_SELECTOR, "[name=AccountLabel] input"
        ).get_attribute("value"),
    }

    browser.find_element(By.ID, "Network").click()
    browser.find_element(By.ID, "NetworkAdvanced").click()

    result["vlan"] = (
        browser.find_element(
            By.CSS_SELECTOR, "[name=VlanWanSwitch] input"
        ).get_attribute("value")
        != "0"
    )
    result["vlanID"] = browser.find_element(
        By.CSS_SELECTOR, "[name=VlanWanVid] input"
    ).get_attribute("value")
    result["dhcp"] = (
        browser.find_element(
            By.CSS_SELECTOR, "[name=VlanDhcpSwitch] input"
        ).get_attribute("value")
        != "0"
    )
    result["dhcpOption"] = browser.find_element(
        By.CSS_SELECTOR, "[name=VlanDhcpOption] input"
    ).get_attribute("value")

    if not result["vlan"] and result["dhcp"] and result["dhcpOption"] == "132":
        return result

    return result


def testNC(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        res = s.connect_ex((ip, 443))
        return res == 0


def IP(ip):
    if not testNC(ip):
        return "Not responding"
    return tel(ip)


def wrapIP(ip):
    print(ip, end="\t", flush=True)
    now = datetime.datetime.now()
    try:
        res = IP(str(ip))
    except Exception as e:
        res = str(e).splitlines()[0]
    return f"{ip}<+{tdelta(now - start)}>:\t{res}"


def main(network="10.172.200.0/22"):
    qi = Queue()
    qo = Queue()
    logfile = join(
        dirname(__file__),
        "logs",
        "vlan",
        f"{start.strftime('vlan-%Y-%m-%d-%H-%M-%S')}.log",
    )
    with open(logfile, "a", encoding="utf-8") as log:
        print("Start:", start.isoformat(" "), file=log)
        for ip in ipaddress.ip_network(network).hosts():
            qi.put_nowait(str(ip))

        ps = [Process(target=child, args=(qi, qo)) for i in range(5)]
        for p in ps:
            p.start()
        N = len(ps)
        while N:
            res = qo.get()
            if res is None:
                N -= 1
                continue
            print(res, file=log, flush=True)
        stop = datetime.datetime.now()
        print(f"End<+{tdelta(stop - start)}>:", stop.isoformat(" "), file=log)


def child(qi: Queue, qo: Queue):
    while True:
        try:
            ip = qi.get_nowait()
            qo.put_nowait(wrapIP(ip))
        except queue.Empty:
            qo.put_nowait(None)
            break


if __name__ == "__main__":
    # main("10.172.201.167/32")
    main("10.172.202.133/32")
    # main("10.172.200.0/22")
