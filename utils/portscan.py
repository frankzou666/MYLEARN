"""
Author:
Purpose:
Date：
"""

import argparse
import socket
import sys
from socket import *
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def checkPort(ip, port):
    """

    :param ip:
    :param port:
    :return:
    """
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, int(port)))
        if result == 0:
            print('#################ERROR########################\n')
            print(ip + ': ' + port + ' is OPEN!!!\n')
            print('#############################################\n')
        else:
            print(ip + ': ' + port + ' closed\n')
    except Exception as e:
        print(e)
        print(ip + ': ' + port + ' is OPEN!!!\n')


def main():
    """the entrance of this file"""
    MAX_WORKERS = 10
    PORT = '27017'
    ips = []
    ipprefix = [
        '202.55.239.',
        '202.153.186.',
        '209.9.72.',
        '209.9.73.',
        '209.9.74.',
        '209.9.75.',
        '206.161.235.',
        '206.161.233.',
        '175.100.205.'
    ]
    for j in ipprefix:
        for i in range(1, 255):
            ips.append(str(j)+str(i))
    print(ips)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for ip in ips:
            pool.submit(checkPort, ip, PORT)


if __name__ == '__main__':
    main()
