import requests

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
    }
    word = input('请输入您想查询的词：')
    data = {
        'kw': word
    }
    response = requests.post(url=post_url,data=data,headers=headers)
    obj = response.json()
    print(obj)
