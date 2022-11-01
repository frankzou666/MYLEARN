"""
Author:
Purpose:
Date：
"""
import argparse
import os
from subprocess import Popen
import sys
from multiprocessing import Pipe
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main():
    """the entrance of this file"""
    if not os.path.exists('/tmp/fi.tmp'):
         fi= os.mkfifo('/tmp/fi.tmp')
    pi = Pipe()
    p= Popen('ls',std)



if __name__ == '__main__':
    main()
