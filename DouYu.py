import json
import logging
import time
import requests
import schedule
from AllFunction import Login, url, EveryDay1, EveryDay2, EveryDay3, EveryDay4, EveryDay5, ShutDown, DanMu, MyUrl, \
    HeadLessLogin, CheckCookies, GetCookies

if __name__ == '__main__':
    logging.basicConfig(filename='HonKai_DouYu.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
     }
    Status = CheckCookies()
    if Status == 0:
        GetCookies()
    driver = HeadLessLogin(url=url)
    driver1 = HeadLessLogin(url=MyUrl)
    session = requests.session()
    # 加载本地cookies
    with open('cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    # 往session里添加cookies
        for cookie in listCookies:
            session.cookies.set(cookie['name'], cookie['value'])

    Qurl = 'https://www.douyu.com/japi/carnival/nc/web/roomTask/getStatus?taskIds=256016%2C256017%2C256018%2C256019'
    # 每天0:01执行发弹幕
    schedule.every().day.at("00:01").do(DanMu, driver=driver1)
    # 每天2:10执行关机
    schedule.every().day.at("02:20").do(ShutDown)
    while True:
        time.sleep(30)
        page_text = session.get(url=Qurl, headers=headers).text
        data = json.loads(page_text)
        ListId = []
        for items in data["data"]:
            if items["condCompleteList"][0]["code"] == 0 \
                    and items["prizeInfo"][0]["remain"]["remainTdDesc"] != "0%" and items["curDeliverNum"] == 0:
                ListId.append(items["condCompleteList"][0]["name"])

        if len(ListId) != 0:
            for taskid in ListId:
                if "每日开播60分钟" in taskid:
                    EveryDay1(driver)
                elif "每日开播120分钟" in taskid:
                    EveryDay2(driver)
                elif "每日直播间被观看10分钟" in taskid:
                    EveryDay3(driver)
                elif "每日直播间收到6条弹幕" in taskid:
                    EveryDay4(driver)
                elif "每日收到“三月七的相片”" in taskid:
                    EveryDay5(driver)
        schedule.run_pending()

