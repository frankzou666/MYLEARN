
"""
Author:
Purpose: chapter 20
Date：
"""


import argparse
import socket
import datetime
import multiprocessing
import os

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def getPid():
    print(os.getpid())
    os._exit(0)

def main():
    for i in range(10):
        multiprocessing.Process(target=getPid).start()

if __name__ == '__main__':
    main()