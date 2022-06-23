
"""
Author:
Purpose:
Date：
"""


import argparse
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
import sys

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()
def f1():
    print(sys.thread_info)
def main():
    ts = []
    for i in range(10):
        thread = Thread(target=f1)
        thread.start()
        ts.append(thread)
    for thread in ts:
        thread.join()
    print('main exit')

if __name__ == '__main__':
    main()