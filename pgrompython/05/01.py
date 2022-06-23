
"""
Author:
Purpose:
Date：
"""


import argparse
import os
import threading
import time
import datetime
from multiprocessing import Process,Lock

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

class Mythread(threading.Thread):
    def __init__(self,id):
        self.id = id
        threading.Thread.__init__(self)
    def run(self):
        print('this is my id %s'%(threading.get_ident()))


def action(i):
     print(i**2)

def main1():
    threads = []
    for i in range(10):
        thread = Mythread(i)
        #thread = threading.Thread(target=action,args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print('main thread exists...')



def child(po):

    while True:
        time.sleep(1)
        msg= ('hello ：'+datetime.datetime.now().strftime('%S')).encode()
        print('threading :' + str(threading.get_ident()) + ' wrte '+('hello ：'+datetime.datetime.now().strftime('%S')))
        os.write(po,msg)

def main2():
    pi,po=os.pipe()
    thread = threading.Thread(target=child,args=(po,))
    thread.start()
    while True:
        time.sleep(1)
        msg = os.read(pi,256)
        print('threading :' + str(threading.get_ident()) + ' read '+msg.decode())

def pidchild():
    print('pid: ' + str(os.getpid()))
    time.sleep(10)
    print('pid: '+str(os.getpid())+'  exit')

def main4():
    processes =[]
    for i in range(5):
        process= Process(target=pidchild,args=())
        process.start()
        processes.append(process)
    for process in processes:
        process.join()


    print('main pid: ' + str(os.getpid()))

def main():
    f =os.system('mstsc')
    print(f)

if __name__ == '__main__':
    main()