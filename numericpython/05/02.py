"""
Author:
Purpose:
Date："""
import argparse

from scipy import linalg
from scipy import optimize

import numpy as np
import  matplotlib.pyplot as pyt
import sympy
sympy.init_printing()

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
    pass


if __name__ == '__main__':
    main()
