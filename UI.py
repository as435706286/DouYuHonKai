import json
import logging
import time
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QPlainTextEdit, QMessageBox
import sys

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from AllFunction import HeadLessLogin, MyUrl, Login, KanBo, KaiBo, url, actAlias, headers


class BengHuai(QWidget):

    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('崩坏：星穹铁道小工具')
        self.driver = HeadLessLogin(url)
        self.driver1 = HeadLessLogin(MyUrl)

        self.button = QPushButton('自动关注', self.window)
        self.button.move(80, 40)
        self.button.clicked.connect(self.GuanZhu)

        self.button = QPushButton('发弹幕', self.window)
        self.button.move(80, 80)
        self.button.clicked.connect(self.DanMu)

        self.button = QPushButton('更新cookies', self.window)
        self.button.move(80, 120)
        self.button.clicked.connect(self.GetCookies)

    def GuanZhu(self):
        for i in range(10):
            # 刷新页面
            self.driver.refresh()
            self.driver.implicitly_wait(5)
            # 模拟鼠标滚轮，滑动至页面顶部
            js = "window.scrollTo(0,-document.body.scrollHeight)"
            self.driver.execute_script(js)
            self.driver.execute_script('window.scrollBy(0,500)')
            time.sleep(1)
            # 关注
            element = self.driver.find_element_by_xpath(
                '//*[@id="js-player-title"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span[1]')
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            element = self.driver.find_element(By.CLASS_NAME, 'dy-Modal-close-x')
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            # 取关
            element = self.driver.find_element_by_xpath(
                '//*[@id="js-player-title"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span[2]')
            ActionChains(self.driver).move_to_element(element).perform()
            time.sleep(1)
            element = self.driver.find_element(By.CLASS_NAME, 'CustomGroupMenu-cancel')
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            # 确认
            element = self.driver.find_element(By.CLASS_NAME, 'dy-btn')
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        logging.info('关注完成!')
        QMessageBox.information(self, "标题", "自动关注完成！", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def DanMu(self):
        element1 = self.driver1.find_element_by_xpath('//*[@id="layout-Player-aside"]/div[2]/div/div[2]/div[2]/textarea')
        element1.send_keys('1')
        time.sleep(1)
        element = self.driver1.find_element_by_xpath('//*[@id="layout-Player-aside"]/div[2]/div/div[2]/div[2]/div[2]')
        self.driver1.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element1.send_keys('2')
        time.sleep(1)
        self.driver1.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element1.send_keys('3')
        time.sleep(1)
        self.driver1.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element1.send_keys('4')
        time.sleep(1)
        self.driver1.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element1.send_keys('5')
        time.sleep(1)
        self.driver1.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element1.send_keys('6')
        time.sleep(1)
        self.driver1.execute_script("arguments[0].click();", element)
        time.sleep(1)
        logging.info("发送弹幕成功！")
        QMessageBox.information(self, "标题", "弹幕发送完成！", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def GetCookies(self):
        # 打开主页
        options = Options()
        options.binary_location = "../Chrome/chrome.exe"
        driver = webdriver.Chrome("../Chrome/chromedriver.exe", options=options)
        logging.basicConfig(filename='HonKai_DouYu.log', level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        driver.get('https://www.douyu.com')
        driver.implicitly_wait(5)
        # 点击登录
        element = driver.find_element_by_xpath('//*[@id="js-header"]/div/div[1]/div[3]/div[7]/div')
        element.click()
        session = requests.session()
        while True:
            dictCookies = driver.get_cookies()
            # 往session里添加cookies
            for cookie in dictCookies:
                session.cookies.set(cookie['name'], cookie['value'])
            param = {
                'actAlias': actAlias
            }
            url = 'https://www.douyu.com/japi/carnival/nc/giftbag/myrecord?'
            page_text = session.get(url=url, headers=headers, params=param).text
            data = json.loads(page_text)
            if data["msg"] == "操作成功":
                jsonCookies = json.dumps(dictCookies)
                print(dictCookies)
                with open('./cookies.txt', 'w') as f:
                    f.write(jsonCookies)
                logging.info('cookies保存成功！')
                driver.quit()
                break
        QMessageBox.information(self, "标题", "更新cookies成功！", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = BengHuai()
    root.window.show()
    sys.exit(app.exec())
