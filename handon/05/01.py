"""
Author:
Purpose:
Date：
"""

import argparse
from sklearn.pipeline import  Pipeline
from sklearn.svm import LinearSVC,SVC
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.datasets import load_iris,make_moons
import numpy as np
import  matplotlib.pyplot as plt


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def lineSvc():
    data = load_iris()
    X = data['data'][:,(2,3)]
    y = (data['target'] ==2).astype(np.float)
    svm_cls = Pipeline(([
        ('standardScaler',StandardScaler()),
        ('linearSVC', LinearSVC(C=1, loss='hinge'))
    ]))
    svm_cls.fit(X, y)
    print(svm_cls.predict([[5.5,1.7]]))
    return True


def lineSvcPoly():
    X, y = make_moons(n_samples=100,noise=0.1)
    svmp_cls = Pipeline(([
        ('polynomialFeatures', PolynomialFeatures()),
        ('standardScaler',StandardScaler()),
        ('SVC', SVC(kernel='poly',degree=3, C=5, coef0=1))
    ]))
    svmp_cls.fit(X, y)
    plt.scatter(X[:,(0)],X[:,(1)])
    plt.show()
    print(svmp_cls)
    return True

def main():
    """the entrance of this file"""
    lineSvcPoly()


if __name__ == '__main__':
    main()
