"""
Author:
Purpose:
Date：
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import Normalizer
from numpy import set_printoptions
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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
    file_name = 'pima-indians-diabetes.data.csv'
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    df = pd.read_csv(file_name, names=names)
    array = df.values
    X = array[:, 0:8]
    Y = array[:, 8]
    test_size = 0.33

    sum = 0
    total_inter =50
    models =[]
    for i in range(total_inter):
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size)
        model = LogisticRegression(max_iter=10000)
        model.fit(X_train, Y_train)
        result = model.score(X_test, Y_test)
        models.append(model)
        sum = sum + result * 100.0
        print("the model %sth,Accuracy: %.1f%%"%(i, result * 100.0))
    print('Average Accuracy %.3f'%(sum/total_inter))

if __name__ == '__main__':
    main()
