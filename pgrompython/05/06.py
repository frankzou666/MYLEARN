"""
Author:
Purpose:
Date：
"""

import argparse
import os,sys
import time


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


from subprocess import Popen, PIPE

def cmdExample():
    """the entrance of this file"""
    pipe = Popen('/usr/bin/top', stdout=PIPE)
    yield pipe.communicate()




def childFunc(pout):
    """
     child process write a message to pipe every second
    :param pin:
    :return:
    """
    while True:
        time.sleep(1)
        msg = str(os.getpid())+':'+str(time.time())
        os.write(pout,msg.encode())
        print('write to pipe:'+msg)

def main():
    """the entrance of this file"""
    # create piple
    #
    #pin,pout = os.pipe()
    named_pile_file='/tmp/np.tmp'
    if not os.path.exists(named_pile_file):
        os.mkfifo(named_pile_file)

    # create child process
    pid = os.fork()
    if pid==0:
        #child process target
        pout=os.open(named_pile_file,os.O_RDONLY)
        childFunc(pout)
    else:
        #parent target
        pin=open(named_pile_file,'r')
        while True:
            time.sleep(1)
            msg=os.readline(pin)
            print('my pid is: %s,get message: %s'%(str(os.getpid()), msg.decode()))



if __name__ == '__main__':
    main()
