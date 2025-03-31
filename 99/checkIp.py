

import requests



URL   = "http://ip-api.com/json/"

def checkIP(ip):
    url_str = URL + ip
    try:
        response = requests.get(url = url_str)
        return response.json()
    except Exception as e:
        print(e.__str__())

def main1():
    ips = [
        '94.202.212.125',

    ]


    for ip in ips:
        result = checkIP(ip=ip)
        print()
        print("ip:"+ip+ ",          country:"+result.get("country") +",city:" + result.get("city"))



def main():
    a='helo'
    print('ddfdf %s'%(a))
if __name__ == '__main__':
    main()