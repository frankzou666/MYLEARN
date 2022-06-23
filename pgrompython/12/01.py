
"""
Author:
Purpose: chapter 20
Date：
"""


import argparse
import socket
import datetime
import os
import _thread as thread


WORKS = []


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def handelconnection(connection):
    while True:
        data= connection.recv(1024)
        if not data:
            break
        print(data)


def dispatcher(sc):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' listen...')
    while True:
        connection, address = sc.accept()
        thread.start_new_thread(handelconnection,(connection,))


def main():
    HOST='0.0.0.0'
    PORT =10001
    sc = socket.socket()
    sc.bind((HOST,PORT))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' binding host={HOST},port={PORT}'.format(HOST=HOST,PORT=PORT))
    sc.listen(10)
    dispatcher(sc)


if __name__ == '__main__':
    main()