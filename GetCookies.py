import logging
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from AllFunction import GetCookies, CheckCookies

if __name__ == "__main__":
    x = CheckCookies()
    GetCookies()
    print(x)

