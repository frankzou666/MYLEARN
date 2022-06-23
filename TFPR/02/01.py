
"""
Author:
Purpose:
Date：
"""


import argparse
import tensorflow as tf
import pandas as pd
import csv

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def testGenerator():
    a = [1,2,4,3,4,5]
    yield a


def getCSVByStream():
    file = 'pima-indians-diabetes.data.csv'
    with open(file,'r') as f:
        csvfile = csv.reader(f,delimiter=',')
        holder = []
        for row in csvfile:
            holder.append(row)
            if  len(holder)%3 == 0:
                yield holder
                holder = []

def getCSV():
    file = 'pima-indians-diabetes.data.csv'
    holder = []
    with open(file,'r') as f:
        csvfile = csv.reader(f,delimiter=',')
        for row in csvfile:
            holder.append(row)
    return  holder

def getCSVByCSV():
    file = 'pima-indians-diabetes.data.csv'
    colname = ['Pregnancies', 'Glucose', 'BloodPressure',
                'SkinThickness', 'Insulin', 'BMI',
                'DiabetesPedigree', 'Age', 'Outcome']
    pds = pd.read_csv(file,names=colname)
    return  pds

def main():
    print(getCSV())
    A = getCSVByStream()
    print(next(A))
    print(next(A))
    print(next(A))

if __name__ == '__main__':
    main()