# 京东首页领京豆签到

import requests
import json
import re

url="https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld"
proxies = {
    "http": None,
    "https": None,
}

def main(ck):
    try:
        headers={
            "Host":"api.m.jd.com",
            "Connection":"keep-alive",
            "User-Agent":"jdapp;android;10.1.0;7.1.2;network/wifi;model/OPPO R11 Plus;addressid/0;aid/f1d05dbf9b907206;oaid/;osVer/25;appBuild/89568;partner/baidu;eufv/1;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 7.1.2; OPPO R11 Plus Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36",
            "Accept":"*/*",
            "Referer":"https://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie":ck
        }
        r=requests.get(url,headers=headers,proxies=proxies)
        r=json.loads(r.text)
        print(r["data"]["dailyAward"])
    except:
        print("error")

if __name__ == '__main__':
    f = open("/jd/config/config.sh")
    cookies = re.findall("\"(pt_key=.*?;pt_pin=.*?;)\"",f.read())
    for i in cookies:
        main(i)
