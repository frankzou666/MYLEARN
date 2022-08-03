"""
Author:
Purpose:
Date：
"""

import argparse
import pandas as pd
import numpy as np

import csv
import json

import h5py



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
