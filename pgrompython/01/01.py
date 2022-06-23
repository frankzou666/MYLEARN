"""
Author:
Purpose:
Date：
"""

import argparse
import pickle

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def funType(l :list[str]):
    """

    :return:
    """
    print(type(l))
    return l

def main():
    """the entrance of this file"""
    l1 = ['a','b']
    l2 = [1,2]
    with open('a.data','wb') as f:
        pickle.dump(l2, f)

    #read
    with open('a.data','rb') as f:
        result = pickle.load(f)
        print(result)

if __name__ == '__main__':
    main()
