import datetime
import hashlib
import time

import pytz as pytz
import requests
import json


def init():
    # 请求地址
    url = "https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query"

    # 请求头
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en,zh;q=0.9,zh-CN;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "132",
        "Content-Type": "application/json",
        "Host": "uwf7de983aad7a717eb.youzy.cn",
        "Origin": "http://pv4y-pc.youzy.cn",
        "Referer": "http://pv4y-pc.youzy.cn/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "U-Sign": "643ff9499febb3ee34c95ffe0bb29cb0",
        "U-Token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6ImE0ZjFlMGRjZjNlNWY1ZWI3ZTk2ZjE0ZTAyMDY4OWI5IiwidWlkIjoiNjA3YmQ2NTFiNTE3YWFiODM1MmNhNWYzIiwiaW5mbyI6IiIsImlhdCI6MTcxNTY0OTExOCwiZXhwIjoxNzE4MjQxMTE4fQ.BOc08ZrJY682Nbs1z3NodYnax5qGxC2F7QOd_ybAsgQgbtusQJyjOaMLqlQ0CojEhuxwLPa7VUEEcxaolsZzc4BHnWsnGw6GoIIRVD7R_aUj9ybD4ypTw7S1yggGuYvK57jCF_Ek4CD8cqa6ksymWRenCmfALZE1M2LV9YpTXo0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    # 请求参数
    data = {
        "keyword": "",
        "provinceNames": [],
        "natureTypes": [],
        "eduLevel": "",
        "categories": [],
        "features": [],
        "pageIndex": 1,
        "pageSize": 20,
        "sort": 11
    }

    secret_key = "0HN3FVPUTJR1L:0000000"
    # 创建一个GMT时区的对象
    gmt_tz = pytz.timezone('GMT')

    # 获取当前时间，并设置为GMT时区
    current_time_gmt = datetime.datetime.now(gmt_tz)

    # 将时间转换为时间戳（以秒为单位）
    timestamp_gmt = int(current_time_gmt.timestamp())

    print(timestamp_gmt)
    # 这里假设算法是将所有请求参数和密钥拼接起来，然后进行MD5哈希
    # data_to_sign = f"{url}{secret_key}{int(time.time())}"
    data_to_sign = f"{secret_key}{timestamp_gmt}"


    # 使用MD5算法生成签名
    u_sign = hashlib.md5(data_to_sign.encode()).hexdigest()
    print(u_sign)

    # 将生成的U-Sign添加到请求头中
    headers["U-Sign"] = u_sign

    # 发送请求
    # response = requests.post(url, headers=headers, data=json.dumps(data))
    print(headers)

    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 打印响应内容
    print(response.text)


if __name__ == '__main__':
    # lab_id = 'cc9de70b56d046bfa5c7afaeb5080b6c'
    init()
