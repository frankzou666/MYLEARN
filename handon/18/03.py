"""
Author:
Purpose:
Date："""
import argparse

import numpy as np


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
    vo = ['good','hello','word']
    vodict = dict((item,1) for item in vo)
    nstring=['word']
    new_string = [0 for _ in range(len(vodict))]
    new_dict = {}
    for item in nstring:
         if item in vo:
             new_string[vo.index(item)]=1

    new_dict= dict((k,v ) for (k,v) in zip(vo,new_string))
    print(new_dict)

if __name__ == '__main__':
    main()
