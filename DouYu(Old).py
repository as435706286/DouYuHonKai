from AllFunction import Login, url, MyUrl, DanMu, EveryDay4, EveryDay3, EveryDay1, EveryDay, ShutDown
import schedule
import logging


if __name__ == '__main__':
    logging.basicConfig(filename='HonKai_DouYu.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    driver = Login(url=url)
    # 每天0:01执行发弹幕
    schedule.every().day.at("00:01").do(DanMu, driver=driver)
    # 每天0:02执行抢4
    schedule.every().day.at("00:02").do(EveryDay4, driver=driver)
    # 每天0:12执行抢3
    schedule.every().day.at("00:12").do(EveryDay3, driver=driver)
    # 每天1:02执行抢1
    schedule.every().day.at("01:02").do(EveryDay1, driver=driver)
    # 每天2:02执行
    schedule.every().day.at("02:02").do(EveryDay, driver=driver)
    # 每天2:10执行关机
    schedule.every().day.at("02:10").do(ShutDown)
    while True:
        schedule.run_pending()





