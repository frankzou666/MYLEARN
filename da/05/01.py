
"""
Author:
Purpose:
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
    return  argparser.parse_args()

def main():
    s = pd.Series([2,4,34,3,22,2])
    df1 = pd.DataFrame({'year': [2011, 2012, 2013], 'GDP': [100, 130, 160]})
    print(s.describe)

if __name__ == '__main__':
    main()