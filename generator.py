import httpx
import json
import string
import json
from itertools import cycle 
import os
import threading
import names
import time
import base64
from hcapbypass import bypass
import random

imagestoencode = []
loginchecks = []

def getDirectory():
  return os.getcwd()

with open('usernames.txt','r+', encoding='utf-8') as usernamefile:
	logins = usernamefile.read().splitlines()

with open('config.json', 'r+', encoding='utf-8') as configfile:
    config = json.load(configfile)

for login in logins:
    loginchecks.append(login)

def getName():
    return random.choice(logins)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def setProfile(token):
  pathto = getDirectory()
  with open(f'{pathto}\Avatars\{random.choice(imagestoencode)}', "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    
  newstr = encoded_string.decode('utf-8')

  headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "authorization": token
  }
  data = {
    "avatar": f'data:image/png;base64,{newstr}'
  }
  changeprofile = httpx.patch('https://discord.com/api/v8/users/@me', headers=headers, json=data, proxies={'http://':config['rotating_proxy']})
  print(changeprofile.text)

def checkCompleted(tzid):
    checknew =  httpx.get('https://onlinesim.ru/api/getState.php?apikey=' + config['onlinesim_key'])
    for check in checknew.json():
        if str(check['tzid']) == str(tzid):
            if check['response'] == 'TZ_NUM_ANSWER':
                responseme = check['msg']
                print(f'Successfully got SMS response {responseme}')
                return check['msg']
            else:
                time.sleep(2)
                return checkCompleted(tzid)

def register(serverinv=None):
    username = random_char(10)
    email = random_char(10) + "@gmail.com"
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

    fingerprintres = httpx.get("https://discord.com/api/v9/experiments", proxies={"http://": config['rotating_proxy']}, timeout=10)

    while True:
        if fingerprintres.text != "":
            try:
                fingerprint = fingerprintres.json()['fingerprint']
            except:
                pass
            break
        else:
            return True


    # Handling Captcha

    sitekey = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"

    while True:
        try:
            captchakey = bypass(sitekey, "discord.com", proxy=config['rotating_proxy'])
            if captchakey == "False":
                continue
            else:
                break
        except:
            pass

    print("Successfully bypassed captcha ",captchakey)

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

    if serverinv != None:
        payload = {"fingerprint": fingerprint,
                    "email": email,
                    "username": getName(),
                    "password": password,
                    "consent": "true",
                    "date_of_birth": "1991-04-06",
                    "gift_code_sku_id": "",
                    "captcha_key": captchakey,
		    "invite": config['invite']
                    }
    else:
        payload = {"fingerprint": fingerprint,
                    "email": email,
                    "username": getName(),
                    "password": password,
                    "consent": "true",
                    "date_of_birth": "1991-04-06",
                    "gift_code_sku_id": "",
                    "captcha_key": captchakey
                    }

    try:
        registerreq = httpx.post("https://discord.com/api/v9/auth/register", headers=header3,
                            json=payload, proxies={"http://": config['rotating_proxy']}, timeout=10)

        token = registerreq.json()['token']
        with open('tokens.txt','a', encoding='utf-8') as f:
            f.write(f'{token}\n')
        with open('tokensp.txt','a', encoding='utf-8') as f:
            f.write(f'{token}:{password}\n')
        print(f"Successfully generated account name {token}")
    except:
        pass
    




def manager(invitecode=None):
    while True:
        if invitecode != None:
            register(invitecode)
        else:
            register()


def main():
    mypath = os.getcwd()

    path = rf"{mypath}\Avatars"
    dirs = os.listdir( path )
    for fileme in dirs:
        imagestoencode.append(fileme)
    for i in range(int(config['threads'])):
        t = threading.Thread(target=manager, args=[config['invite']])  # daemon means that all threads will exit when the main thread exits
        t.start()

if __name__ == '__main__':
    main()
