"""
Author:
Purpose:
Date：
"""


import argparse
import os
import pandas as pd
from mxnet import np

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def writeCSV():
    os.makedirs(os.path.join('..', 'data'), exist_ok=True)
    data_file = os.path.join('..', 'data', 'house_tiny.csv')
    with open(data_file, 'w') as f:
        f.write('NumRooms,Alley,Price\n')  # Column names
        f.write('NA,Pave,127500\n')  # Each row represents a data example
        f.write('2,NA,106000\n')
        f.write('4,NA,178100\n')
        f.write('NA,NA,140000\n')
    return True


def readCSV():
    data_file = os.path.join('..', 'data', 'house_tiny.csv')
    pds = pd.read_csv(data_file)
    return pds


def main():
    print(np.array(readCSV()))
    print(type(np.array(readCSV())))

if __name__ == '__main__':
    main()