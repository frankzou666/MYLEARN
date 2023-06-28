"""
Author:
Purpose:
Date："""
import argparse
import numpy as np
import matplotlib.pyplot as plt
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()





def mainold():
    """the entrance of this file"""
    n1= np.array([
        [1,3,5,6],
        [2, 3, 4, 5],
        [3, 5, 9, 5]
    ])
    n2=np.array([2,3,4,2])
    print((n1-n2))
    print((n1-n2).sum(axis=1))


def main():
    n1=[((6, 4, 7, 9, 8, 3, 1, 2, 10, 5),),((6, 4, 7, 9, 8, 3, 1, 2, 10, 5),)]
    for item in n1:
        print(item[0])

if __name__ == '__main__':
    main()
