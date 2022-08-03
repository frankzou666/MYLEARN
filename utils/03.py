import sys
import requests
import time
def main():



    ips =[




        '66.249.66.19',
        '66.249.66.40',
        '66.249.66.78',
        '66.249.66.79',
        '66.249.66.90',
        '66.249.66.91',
        '67.203.6.43',
        '68.183.151.254',
        '69.160.160.58',
        '69.63.184.2',
        '69.63.184.3',
        '69.63.184.4',
        '72.10.175.226',
        '8.26.182.26',
        '8.31.2.43',
        '84.242.125.234',
        '88.214.43.118',
        '89.104.111.166'
    ]

    for ip in ips:
        #url = 'http://freeapi.ipip.net/'  # 中文免费
        #url = 'http://ip-api.com/docs/api:json'
        url2 = 'http://ip-api.com/json/'  # 外国网站
        #url = url + format(ip)
        url2 = url2 + format(ip)
        #response = requests.get(url)
        response = requests.get(url2)

        str = response.text.replace('\"', '')  # 去掉双引号
        str = str.replace('[', '')  # 去掉方括号
        str = str.replace(']', '')
        str = str.replace(' ', '')

        str = str.split(",")  # 已逗号为分割符号，分割字符串为数组
        time.sleep(1)
        print("您查询的IP地址 %s 来源地是：%s" % (ip,str[1]))


if __name__ == '__main__':
    main()