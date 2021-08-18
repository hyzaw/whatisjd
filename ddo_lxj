# 京东领现金
# Author:ddo
# update time:2021/8/18
import urllib

import requests
import json
import re
import time
import random

proxies = {
    "http": None,
    "https": None,
}


def randomstr(num):
    randomstr = ""
    for i in range(num):
        randomstr = randomstr + random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    return randomstr


def main(ck):
    try:
        headers = {
            "Host": "api.m.jd.com",
            "Connection": "keep-alive",
            "User-Agent": "okhttp/3.12.1;jdmall;android;version/9.2.2;build/89568;screen/1440x2560;os/7.1.2;network/wifi",
            "Accept": "*/*",
            "Referer": "http s://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": ck,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        # st = str(int(time.time() * 1000))
        jduuid = randomstr(16)
        # sign = jdsign.get_sign("cash_sign", "{\"breakReward\":0,\"inviteCode\":null,\"remind\":0,\"type\":0}", jduuid,
        #                        "android", "9.2.2")
        params = {
            "functionId": "cash_sign",
            "body": "{\"breakReward\":0,\"inviteCode\":null,\"remind\":0,\"type\":0}",
            "uuid": jduuid,
            "client": "android",
            "clientVersion": "9.2.2"
        }
        sign = requests.post(url="https://sign.nz.lu/getSignFromJni", params=params, proxies=proxies).text
        url = "https://api.m.jd.com/client.action?functionId=cash_sign&clientVersion=9.2.2&client=android&uuid=%s&%s" % (
            jduuid, sign)
        data = "body=%7B%22breakReward%22%3A0%2C%22inviteCode%22%3Anull%2C%22remind%22%3A0%2C%22type%22%3A0%7D"
        r = requests.post(url, headers=headers, data=data, proxies=proxies)
        print(r.text)
        # r=requests.get(url,headers=headers,proxies=proxies)
    except:
        print("error")


def doTask(ck, body):
    try:
        jduuid = randomstr(16)
        headers = {
            "Host": "api.m.jd.com",
            "Connection": "keep-alive",
            "User-Agent": "okhttp/3.12.1;jdmall;android;version/9.2.2;build/89568;screen/1440x2560;os/7.1.2;network/wifi",
            "Accept": "*/*",
            "Referer": "http s://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": ck,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        params = {
            "functionId": "cash_doTask",
            "body": body,
            "uuid": jduuid,
            "client": "android",
            "clientVersion": "9.2.2"
        }
        sign = requests.post(url="https://sign.nz.lu/getSignFromJni", params=params, proxies=proxies).text
        url = "https://api.m.jd.com/client.action?functionId=cash_doTask&clientVersion=9.2.2&build=89568&client=android&uuid=%s&%s" % (
        jduuid, sign)
        data = "body=" + urllib.parse.quote_plus(body)
        r = requests.post(url, headers=headers, data=data, proxies=proxies)
        print(r.text)
    except:
        print("err")


def doTasker(ck):
    try:
        jduuid = randomstr(16)
        headers = {
            "Host": "api.m.jd.com",
            "Connection": "keep-alive",
            "User-Agent": "okhttp/3.12.1;jdmall;android;version/9.2.2;build/89568;screen/1440x2560;os/7.1.2;network/wifi",
            "Accept": "*/*",
            "Referer": "http s://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": ck,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        params = {
            "functionId": "cash_homePage",
            "body": "{}",
            "uuid": jduuid,
            "client": "android",
            "clientVersion": "9.2.2"
        }
        sign = requests.post(url="https://sign.nz.lu/getSignFromJni", params=params, proxies=proxies).text
        url = "https://api.m.jd.com/client.action?functionId=cash_homePage&clientVersion=9.2.2&build=89568&client=android&uuid=%s&%s" % (
        jduuid, sign)
        data = "body=%7B%7D"
        r = requests.post(url, headers=headers, data=data, proxies=proxies)
        TaskList = json.loads(r.text)["data"]["result"]["taskInfos"]
        for i in TaskList:
            if i["finishFlag"] == 2:
                TaskInfo = i["desc"].split(",")
                print(TaskInfo)
                for ii in TaskInfo:
                    body = "{\"taskInfo\":\"%s\",\"type\":%s}"%(TaskInfo,i["type"])
                    time.sleep(5)
                    doTask(ck, body)
    except:
        print("err")


if __name__ == '__main__':
    f = open("/jd/config/config.sh")
    cookies = re.findall("\"(pt_key=.*?;pt_pin=.*?;)\"",f.read())
    for i in cookies:
        main(i)
        doTasker(i)
