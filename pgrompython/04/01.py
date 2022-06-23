
"""
Author:
Purpose:
Date：
"""


import argparse
import pickle
import datetime
import time
import os
import glob

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main2():
    test= datetime.datetime.now()
    print('first:' + test.__str__())
    if os.path.exists('text.obj') == False:
        print('file not exists')
    else:
        print('file exists')

    with open('text.obj','wb') as f:
        r=pickle.dump(test,f)
        print(r)


def walk(path):

    for line in os.listdir(path):
        newpath = os.path.join(path, line)
        if os.path.isdir(newpath):
            walk(newpath)
        else:
            print(newpath)



def main():
     path = r'C:\Users\Administrator\PycharmProjects\untitled\pgrompython\04'
     walk(path)





if __name__ == '__main__':
    main()