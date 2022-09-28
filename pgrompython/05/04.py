"""
Author:
Purpose:
Date：
"""

import argparse
import threading
import  _thread
import time

count_locker = _thread.allocate_lock()
count =0


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
        count_locker.acquire()
        global count

        count = count + 1
        count_locker.release()
        time.sleep(1)
        print('run from threading:%s,count:%s'%(str(threading.Thread.getName(self)),str(count)))

def main():
    """the entrance of this file"""
    threads = []

    for i in range(10):
        thread = MyThread()
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print('\nrun from threading:' + threading.current_thread().getName())


if __name__ == '__main__':
    main()
