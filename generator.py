import httpx
import json
import string
import json
from itertools import cycle 
import threading
from hcapbypass import bypass
import random

usernames = []

with open('usernames.txt','r+', encoding='utf-8') as usernamefile:
	logins = usernamefile.read().splitlines()

with open('config.json', 'r+', encoding='utf-8') as configfile:
    config = json.load(configfile)

with open('proxies.txt','r+', encoding='utf-8') as proxyfile:
    ProxyPool = cycle(proxyfile.read().splitlines())

for user in usernames:
    usernames.append(user)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def register(serverinv):
    username = random_char(10)
    email = random_char(10) + "@" + random_char(10) + ".com"
    password = random_char(10)


    # Getting cookies

    header1 = {
        "Host": "discord.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en;q=0.9",
    }

    getcookie = httpx.get("https://discord.com/register").headers['set-cookie']
    sep = getcookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dfc = sx2[1]
    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]

    # Get Fingerprint

    header2 = {
        "Host": "discord.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        "X-Context-Properties": "eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=",
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Authorization": "undefined",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/register",
        "Accept-Encoding": "gzip, deflate, br"
    }

    fingerprintres = httpx.get("https://discord.com/api/v9/experiments", timeout=10)

    while True:
        if fingerprintres.text != "":
            fingerprint = fingerprintres.json()['fingerprint']
            break
        else:
            return True


    # Handling Captcha

    sitekey = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"

    while True:
        currentproxy = next(ProxyPool)
        captchakey = bypass(sitekey, "discord.com", proxy=currentproxy)
        if captchakey == "False":
            continue
        else:
            break

    print("CAPTCHA KEY IS >>>>: ",captchakey)

    header3 = {

        "Host": "discord.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        "X-Fingerprint": fingerprint,
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Content-Type": "application/json",
        "Authorization": "undefined",
        "Accept": "*/*",
        "Origin": "https://discord.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/register",
        "X-Debug-Options": "bugReporterEnabled",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}"

    }

    payload = {"fingerprint": fingerprint,
                "email": email,
                "username": random.choice(usernames),
                "password": password,
                "invite": serverinv,
                "consent": "true",
                "date_of_birth": "1991-04-06",
                "gift_code_sku_id": "",
                "captcha_key": captchakey,
                }

    registerreq = httpx.post("https://discord.com/api/v9/auth/register", proxies={"https": "https://" + next(ProxyPool)}, headers=header3,
                           json=payload, timeout=10)

    print("ACCOUNT REGISTERED")

    token = registerreq.json()['token']
    print("TOKEN IS >>>", token)




def manager():

    invitecode = config['invite']

    register(invitecode)


def main():
    threads_to_start = int(input("threads to use:"))



    for i in range(threads_to_start):
        t = threading.Thread(target=manager)  # daemon means that all threads will exit when the main thread exits
        t.start()



if __name__ == '__main__':
    main()
