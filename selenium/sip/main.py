from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), ".env"))


def main():
    print("Hello from sip!")


if __name__ == "__main__":
    main()
