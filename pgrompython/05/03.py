"""
Author:
Purpose:
Date：
"""

import argparse
import threading


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
    def run(self):
        print('run from threading:'+threading.Thread.getName(self))

def main():
    """the entrance of this file"""
    threads = []
    for i in range(100):
        thread = MyThread()
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print('\nrun from threading:' + threading.current_thread().getName())


if __name__ == '__main__':
    main()
