# 领券中心签到
import time
import requests
import json
import random
import urllib
import uuid
import re
import urllib.parse

proxies = {
    "http": None,
    "https": None,
}


def randomstr(num):
    randomstr = ""
    for i in range(num):
        randomstr = randomstr + random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    return randomstr


def getsign(functionid, body, jduuid):
    data = {
        "functionId": functionid,
        "body": body,
        "uuid": jduuid,
        "client": "android",
        "clientVersion": "9.2.2"
    }
    sign = requests.post(url="", data=data, proxies=proxies).text
    return sign


def getheader(ck):
    headers = {
        "Host": "api.m.jd.com",
        "Connection": "keep-alive",
        "User-Agent": "okhttp/3.12.1;jdmall;android;version/9.2.2;build/89568;screen/1440x2560;os/7.1.2;network/wifi",
        "Accept": "*/*",
        "Referer": "https://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": ck,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    return headers

def main(ck):
    try:
        headers = getheader(ck)
        jduuid = randomstr(16)
        functionId = "ccSignInNew"
        body="%7B%22childActivityUrl%22%3A%22openapp.jdmobile%3A%2F%2Fvirtual%3Fparams%3D%7B%5C%22category%5C%22%3A%5C%22jump%5C%22%2C%5C%22des%5C%22%3A%5C%22couponCenter%5C%22%7D%22%2C%22monitorRefer%22%3A%22appClient%22%2C%22monitorSource%22%3A%22cc_sign_android_index_config%22%2C%22pageClickKey%22%3A%22Coupons_GetCenter%22%7D%26"
        sign=getsign(functionId,urllib.parse.unquote(body),jduuid)
        url = "https://api.m.jd.com/client.action?functionId=%s&clientVersion=9.2.2&build=89568&client=android&uuid=%s&%s" % (
        functionId, jduuid, sign)
        r=requests.post(url,data="body="+body,headers=headers)
        r=json.loads(r.text)
        if r["busiCode"]=="1002":
            print("今日已签到")
        else:
            print("签到"+r["message"],"获得"+r["result"]["signResult"]["signData"]["amount"]+"红包")
    except:
        print("签到失败")

if __name__ == '__main__':
    f = open("/jd/config/config.sh")
    cookies = re.findall("\"(pt_key=.*?;pt_pin=.*?;)\"", f.read())
    for i in cookies:
        main(i)
