import json
import logging
import time

from AllFunction import GetStatus, CheckCookies, DanMu, Login, MyUrl, HeadLessLogin, GuanZhu, url, EveryDay1, EveryDay2, \
    EveryDay3
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    logging.basicConfig(filename='HonKai_DouYu.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #driver = Login(url)
    # # 模拟鼠标滚轮
    # js = "window.scrollTo(0,document.body.scrollHeight)"
    # driver.execute_script(js)
    # js = "window.scrollTo(0,-document.body.scrollHeight)"
    # driver.execute_script(js)
    # driver.execute_script('window.scrollBy(0,500)')
    # driver.quit()
    # EveryDay1(driver)
    # DanMu(driver)
    GuanZhu()
    print("关注完成")


