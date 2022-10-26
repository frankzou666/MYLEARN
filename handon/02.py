"""
Author:
Purpose:
Date：
"""
import numpy as np
import argparse
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
    n1=np.array(((3,4),(5,6)))
    print(n1)
    print(np.linalg.inv(n1))


if __name__ == '__main__':
    main()
