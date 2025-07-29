from os.path import join, dirname
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


load_dotenv(join(dirname(__file__), ".env"))


def tel(ip):
    chrome_options = Options()
    chrome_options.add_argument("--disable-auto-update")
    with webdriver.Chrome(options=chrome_options) as browser:
      browser.get(f"https://{ip}")

def main():
   tel('10.172.202.31')


if __name__ == "__main__":
    main()
