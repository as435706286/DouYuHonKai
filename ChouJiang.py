import logging
from datetime import time
from AllFunction import Login, url
from AllFunction import KanBo

# -----------------领取抽奖次数并抽奖
if __name__ == "__main__":
    logging.basicConfig(filename='HonKai_DouYu.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    driver = Login(url=url)
    KanBo(driver)
