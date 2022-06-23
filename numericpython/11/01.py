"""
Author:
Purpose:
Date：
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import mpl_toolkits.mplot3d
import scipy.sparse as sp
import scipy.sparse.linalg
import scipy.linalg as lg

from scipy import integrate



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
