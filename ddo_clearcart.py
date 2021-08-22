# 清空购物车
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
    data={
        "functionId":functionid,
        "body":body,
        "uuid":jduuid,
        "client":"android",
        "clientVersion":"9.2.2"
    }
    sign=requests.post(url="https://service-ft43gk13-1302176878.sh.apigw.tencentcs.com/release/ddo",data=json.dumps(data)).text
    # print(sign)
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


def getcart(ck):
    headers = getheader(ck)
    jduuid = randomstr(16)
    functionId = "cartClearQuery"
    body = "%7B%22addressId%22%3A%220%22%2C%22cartBundleVersion%22%3A%2210100%22%2C%22coord_type%22%3A%22%22%2C%22latitude%22%3A%2230.904426%22%2C%22longitude%22%3A%22118.712839%22%2C%22userType%22%3A%221%22"
    sign = getsign(functionId, urllib.parse.unquote(body), jduuid)
    url = "https://api.m.jd.com/client.action?functionId=%s&clientVersion=9.2.2&build=89568&client=android&uuid=%s&%s" % (
    functionId, jduuid, sign)
    # print(url)
    r = requests.post(url, data="body=" + body, proxies=proxies, headers=headers).text
    r = json.loads(r)
    CartList = r["clearCartInfo"]
    operations = []
    for i in CartList:
        for ii in i["groupDetails"]:
            if "suitType" not in ii:
                item_json = {"itemId": ii["skuId"], "itemType": ii["itemType"], "skuUuid": ii["skuUuid"], "suitType": 0}
                operations.append(item_json)
            else:
                for iii in ii["clearSkus"]:
                    item_json = {"itemId": iii["skuId"], "itemType": iii["itemType"], "skuUuid": iii["skuUuid"],
                                 "suitType": 0}
                    operations.append(item_json)

    return operations


def main(ck):
    global r
    headers = getheader(ck)
    jduuid = randomstr(16)
    functionId = "cartClearRemove"
    try:
        body = "{\"addressId\":\"0\",\"cartBundleVersion\":\"10100\",\"coord_type\":\"\",\"latitude\":\"30.904426\",\"longitude\":\"118.712839\",\"operations\":" + str(
        getcart(ck)) + ",\"userType\":\"1\"}"
        time.sleep(3)
        sign = getsign(functionId, body, jduuid)
        url = "https://api.m.jd.com/client.action?functionId=%s&clientVersion=9.2.2&build=89568&client=android&uuid=%s&%s" % (
        functionId, jduuid, sign)
        r = requests.post(url, data="body=" + urllib.parse.quote(body), headers=headers, proxies=proxies)
        print(r.text)
    except:
        print("error")


if __name__ == '__main__':
    f = open("/jd/config/config.sh")
    cookies = re.findall("\"(pt_key=.*?;pt_pin=.*?;)\"", f.read())
    for i in cookies:
        main(i)
