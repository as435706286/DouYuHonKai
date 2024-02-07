import time
import json
import datetime as dt
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import logging
import subprocess
from selenium.webdriver.common.by import By

# -----------版本号
actAlias = '20231211FCGWM'
# -----------自己直播间地址
MyUrl = 'https://www.douyu.com/10404724'
# -----------随机直播间地址
url = 'https://www.douyu.com/topic/2024xqtd16?rid=6176470&dyshid=18cbfb-7c1470d326239a1fb0b148a500051601'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}


def Login(url):
    options = Options()
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option("prefs", prefs)
    options.binary_location = "../Chrome/chrome.exe"
    driver = webdriver.Chrome("../Chrome/chromedriver.exe", options=options)
    # 打开主页
    driver.get(url=url)
    driver.implicitly_wait(5)
    # 加载本地cookies
    with open('cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    # 往driver里添加cookies
        for cookie in listCookies:
            driver.add_cookie(cookie)
    # 刷新页面
    driver.refresh()
    time.sleep(2)
    # 模拟鼠标滚轮，滑动至页面底部
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    logging.info("登录成功！")
    return driver


def HeadLessLogin(url):
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.binary_location = "../Chrome/chrome.exe"
    options.add_argument('--headless')
    driver = webdriver.Chrome("../Chrome/chromedriver.exe", options=options)
    # 打开主页
    driver.get(url=url)
    driver.implicitly_wait(5)
    # 加载本地cookies
    with open('cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
        # 往driver里添加cookies
        for cookie in listCookies:
            driver.add_cookie(cookie)
    # 刷新页面
    driver.refresh()
    time.sleep(2)
    # 模拟鼠标滚轮，滑动至页面底部
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    logging.info("HeadLess登录成功！")
    return driver


# -----------------------领取每日开播任务奖励
def EveryDay(driver):
    # 点击开播福利
    element = driver.find_element_by_xpath('//*[@id="bc61"]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc122"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc4531"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc4542"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc4553"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc4564"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    logging.info("领取每日开播任务奖励成功！")


# -----------------------领取每日开播任务1奖励:开播60分钟id:242519
def EveryDay1(driver):
    try:
        # 点击开播福利
        element = driver.find_element_by_xpath('//*[@id="bc61"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="bc122"]/div/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        logging.info("领取每日开播任务1奖励成功！")
    except:
        logging.error("领取每日开播任务1失败！")


# -----------------------领取每日开播任务2奖励:开播120分钟id:242521
def EveryDay2(driver):
    try:
        # 点击开播福利
        element = driver.find_element_by_xpath('//*[@id="bc61"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="bc6077"]/div/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        logging.info("领取每日开播任务2奖励成功！")
    except:
        logging.error("领取每日开播任务2失败！")


# -----------------------领取每日开播任务3奖励:被观看10分钟id:242522
def EveryDay3(driver):
    try:
        # 点击开播福利
        element = driver.find_element_by_xpath('//*[@id="bc61"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="bc6088"]/div/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        logging.info("领取每日开播任务3奖励成功！")
    except:
        logging.error("领取每日开播任务3失败！")


# -----------------------领取每日开播任务4奖励:收到6条弹幕id:242523
def EveryDay4(driver):
    try:
        # 点击开播福利
        element = driver.find_element_by_xpath('//*[@id="bc61"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="bc6099"]/div/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        logging.info("领取每日开播任务4奖励成功！")
    except:
        logging.error("领取每日开播任务4失败！")


# -----------------------领取每日开播任务5奖励:收到三月七相片id:242524
def EveryDay5(driver):
    try:
        # 点击开播福利
        element = driver.find_element_by_xpath('//*[@id="bc61"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="bc6110"]/div/button')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        logging.info("领取每日开播任务5奖励成功！")
    except:
        logging.error("领取每日开播任务5失败！")


# ----------------------领取直播奖励
# 领取
def KaiBo(driver):
    # 点击开播福利
    element = driver.find_element_by_xpath('//*[@id="bc61"]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc257"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3419"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3429"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3439"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3449"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3459"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3469"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3479"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3489"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc3499"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    logging.info("领取开播奖励成功")


# -----------------------领取看播奖励
def KanBo(driver):
    # 刷新页面
    driver.refresh()
    time.sleep(2)
    # 模拟鼠标滚轮，滑动至页面底部
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    element = driver.find_element_by_xpath('//*[@id="bc5215"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc5225"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="bc5235"]/div/button')
    driver.execute_script("arguments[0].click();",element)
    logging.info("领取看播奖励成功")


# -----------------------发弹幕
def DanMu(driver):
    element1 = driver.find_element_by_xpath('//*[@id="layout-Player-aside"]/div[2]/div/div[2]/div[2]/textarea')
    element1.send_keys('1')
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="layout-Player-aside"]/div[2]/div/div[2]/div[2]/div[2]')
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element1.send_keys('2')
    time.sleep(1)
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element1.send_keys('3')
    time.sleep(1)
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element1.send_keys('4')
    time.sleep(1)
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element1.send_keys('5')
    time.sleep(1)
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    element1.send_keys('6')
    time.sleep(1)
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    logging.info("发送弹幕成功！")


# -----------------------关机
def ShutDown():
    # 执行关机命令
    shutdown_command = "shutdown /s /t 0"
    subprocess.call(shutdown_command, shell=True)


# -----------------------关注
def GuanZhu():
    driver = HeadLessLogin(url)
    for i in range(10):
        # 刷新页面
        driver.refresh()
        driver.implicitly_wait(5)
        # 模拟鼠标滚轮，滑动至页面顶部
        js = "window.scrollTo(0,-document.body.scrollHeight)"
        driver.execute_script(js)
        driver.execute_script('window.scrollBy(0,500)')
        time.sleep(1)
        #关注
        element = driver.find_element_by_xpath('//*[@id="js-player-title"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span[1]')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        element = driver.find_element(By.CLASS_NAME,'dy-Modal-close-x')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        #取关
        element = driver.find_element_by_xpath('//*[@id="js-player-title"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span[2]')
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(1)
        element = driver.find_element(By.CLASS_NAME,'CustomGroupMenu-cancel')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        #确认
        element = driver.find_element(By.CLASS_NAME,'dy-btn')
        driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
    driver.quit()
    logging.info('关注完成!')
    return "关注完成!"


# -----------------------查询任务状态
def GetStatus():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
     }

    session = requests.session()
    # 加载本地cookies
    with open('cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    # 往session里添加cookies
        for cookie in listCookies:
            session.cookies.set(cookie['name'], cookie['value'])

    Qurl = 'https://www.douyu.com/japi/carnival/nc/web/roomTask/getStatus?taskIds=242511%2C242512%2C242514%2C242515%2C242517'
    page_text = session.get(url=Qurl, headers=headers).text
    data = json.loads(page_text)

    ListId = []
    for items in data["data"]:
        if items["condCompleteList"][0]["code"] == 0 and items["prizeInfo"][0]["remain"]["remainTdDesc"] != "0%" and items["curDeliverNum"] == 0:
            ListId.append(items["condCompleteList"][0]["id"])

    return ListId


# -----------------------获取cookies
def GetCookies():
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


# -----------------------检测cookies有效性
def CheckCookies():
    ListExpiry = []
    # 加载本地cookies
    try:
        with open('cookies.txt', 'r', encoding='utf8') as f:
            ListCookies = json.loads(f.read())
    except FileNotFoundError:
        logging.info('cookies文件不存在！')
        return 0
    except:
        return 0
    # 获取cookie时间戳
    for item in ListCookies:
        if "expiry" in item.keys():
            ListExpiry.append(item["expiry"])
    # 获取当前时间戳
    now = dt.datetime.now()
    # 最小过期时间
    ddl = dt.datetime.fromtimestamp(min(ListExpiry))
    # 判断是否过期
    # 过期
    if now >= ddl:
        logging.info('cookies已过期！')
        return 0
    # 有效
    else:
        return 1


