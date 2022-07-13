"""
Author:
Purpose:
Date：
"""

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
    n1 = np.zeros((3,3))
    n2 = np.append(n1,[[4],[56],[6]],axis=1)
    print(n1)
    print(n2)



if __name__ == '__main__':
    main()
