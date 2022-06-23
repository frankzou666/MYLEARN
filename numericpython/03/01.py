
"""
Author:
Purpose:
Date：
"""


import argparse
import sympy
from tensorflow.keras.utils import to_categorical
import numpy as np

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def testcategory():
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    a = ['a','e','b']
    b = [dict.get(i) for i in a]
    cate = to_categorical(np.array(b).reshape(-1, 1))

    print(cate)
    result = [i.index(1) for i in cate.tolist()]
    print(result)


def main():
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    a = [[10, 'a',5], [20, 'e',5], [90, 'b',5]]
    b = to_categorical(a)
    print(b)



if __name__ == '__main__':
    main()