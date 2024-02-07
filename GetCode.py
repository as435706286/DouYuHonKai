import requests
import json
from AllFunction import actAlias, GetCookies, CheckCookies
import datetime as dt

if __name__ == "__main__":

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
     }
    ListCode = []
    url = 'https://www.douyu.com/japi/carnival/nc/giftbag/myrecord?'
    session = requests.session()
    # 检测cookies有效性
    Status = CheckCookies()

    # 如果未登录
    if Status == 0:
        GetCookies()

    listA = []
    with open('cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    # 往session里添加cookies
        for cookie in listCookies:
            session.cookies.set(cookie['name'], cookie['value'])

    for page in range(1, 15):
        page = str(page)
        param = {
            'pageSize': '100',
            'currentPage': page,
            'actAlias': actAlias
        }
        page_text = session.get(url=url, headers=headers, params=param).text
        data = json.loads(page_text)
        for items in data["data"]["bags"]:
            if items["bname"] != "谢谢参与":
                listA = listA + items["prizes"]
    for dicA in listA:
        if dicA["name"] != "流量" and dicA["name"] != "鱼丸" and dicA["name"] != "体验鱼翅":
            # Code = str(dt.datetime.fromtimestamp(dicA["obtTime"])) + " " + dicA["name"] + ":" + dicA["ext"]
            Code = dicA["ext"]
            ListCode.append(Code)
            print(dt.datetime.fromtimestamp(dicA["obtTime"]), dicA["name"] + ":" + dicA["ext"])

    with open('./DouyuCode.txt', 'w', encoding='utf-8') as fp:
        for Code in ListCode:
            fp.write(Code+'\n')

