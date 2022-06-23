"""
Author:
Purpose:
Date：
"""

import argparse
import pandas


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
    df = pandas.date_range('2022-03-01','2022-03-22',freq='1H')
    print(df.to_numpy())

if __name__ == '__main__':
    main()
