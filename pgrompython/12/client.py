
"""
Author:
Purpose: chapter 20
Date：
"""


import argparse
import socket
import datetime

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main():
    HOST='127.0.0.1'
    PORT =10001
    sc = socket.socket()
    sc.connect((HOST,PORT))
    #send bytes
    sc.send(bytearray('hello11',encoding='utf8'))
    #recv from server
    sc.close()

    sc.close()

if __name__ == '__main__':
    main()