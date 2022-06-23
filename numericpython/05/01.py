"""
Author:
Purpose:
Date：
"""

import argparse
from scipy import linalg as la
from scipy import optimize
import sympy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

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
    "x=(5,4)"
    import urllib3
    curdate= datetime.datetime.now()
    startdate = (curdate - datetime.timedelta(hours=24)).strftime('%Y-%m-%d')
    enddate = (curdate).strftime('%Y-%m-%d')
    result = pd.period_range(start=startdate, end=enddate, freq='1H').to_list()
    for i in range(len(result)-1):
        sqlstr = str(result[i]) + ' and ' + str(result[i+1])
        # query real source
        # build report object
        # save to report source


if __name__ == '__main__':
    main()
