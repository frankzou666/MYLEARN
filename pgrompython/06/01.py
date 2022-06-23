
"""
Author:
Purpose:
Date：
"""


import argparse
import glob
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

def main1():
    PATH = r'c:/1/'
    files = glob.glob(PATH+'*.jpg')
    for file in files:
         print(os.path.getsize(file)/1024)


def main2():
    PATH = 'c:\\1\\'
    for a,b,c in os.walk(PATH):
        print(a)

def main():
    FILE='C:\\1\\1103\\creative_commons_elephant.jpg'
    DESTFILE = 'C:\\1\\1103\\c.jpg'
    input=open(FILE,'rb')
    output = None
    total = 0
    num=0
    while True:
        if output is None:
            output= open(DESTFILE+str(num), 'wb')
        buf = input.read(1024)
        if not buf: break
        output.write(buf)
        total = total + len(buf)
        if total%(30*1024) == 0:
            output.close()
            num= num+1
            output = open(DESTFILE+str(num), 'wb')



if __name__ == '__main__':
    main()