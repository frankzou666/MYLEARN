"""
Author:
Purpose: multiprocessing
Date：
"""
import argparse
from multiprocessing import Process
import os
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def whoAmI():
    msg="name:%s,pid:%s"
    print(msg%(__name__,os.getpid()))


def main():
    """the entrance of this file"""
    process_list=[]
    for i in range(5):
        process = Process(target=whoAmI,args=())
        process.start()
        process_list.append(process)
   # wait child process exit
    for i in range(len(process_list)):
        process_list[i].join()

    print("main pid exit..")




if __name__ == '__main__':
    main()
