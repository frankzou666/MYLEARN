
"""
Author:
Purpose:
Date：
"""


import argparse
from typing import  List
from math import sqrt



def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


Vector = List[float]


def addVector(v:Vector,b:Vector) ->Vector:
    assert  len(v) == len(b)
    return [(n1-n2)**2 for n1,n2 in zip(v,b)]

def sumOFDistance(v:Vector) ->float:
    assert Vector
    return sum(v)

def distanceBetweenVector(v:Vector,b:Vector)->float:
    assert len(v) == len(b)
    addvectors = addVector(v,b)
    sumvector =  sumOFDistance(addvectors)
    return  sqrt(sumvector)

def main():
    v = [2,3,4]
    b = [1,3,5]
    print(distanceBetweenVector(v,b))

if __name__ == '__main__':
    main()