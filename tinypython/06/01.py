
"""
Author:
Purpose:
Date：
"""


import argparse
import threading
import time
import yaml

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def fun1(x):
    time.sleep(5)
    print(x)

def main():
    threads = []
    for i in range(10):
        th1 = threading.Thread(target=fun1,args=(i,))
        th1.start()
        threads.append(th1)

    for th in threads:
        th.join()
    print('main exit')

if __name__ == '__main__':
    main()