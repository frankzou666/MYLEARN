"""
Author:
Purpose: Introducing to Pandas
Date：
"""

import argparse
import pandas as pd

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def getPdOptions():
    """
        :arg
        :return
        :date
     """
    print(pd.get_option('compute.use_numba'))


def main():
    """the entrance of this file"""
    getPdOptions()


if __name__ == '__main__':
    main()
