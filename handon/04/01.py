
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
import math
import sympy
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def fun1():
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    x_p = np.c_[np.ones((100, 1)), X]
    print(X[:10])
    print(x_p[:10])
    plt.scatter(X,y)
    plt.show()
    theta = np.linalg.inv(x_p.T.dot(x_p)).dot(x_p.T).dot(y)
    print(theta)


def fun2():
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    x_p = np.c_[np.ones((100, 1)), X]

    #gradient desent
    times = 1000
    theta = np.random.randn(2,1)
    lr = 0.01
    m = 100
    for _ in range(times):
        gradients = 2/m * x_p.T.dot(x_p.dot(theta) - y)
        theta = theta - lr*gradients
    print(theta)
    plt.scatter(X,y)
    plt.show()

def fun3():
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    x_p = np.c_[np.ones((100, 1)), X]

    lrs = [0.5]  # learning rate
    plt.scatter(X, y)
    for lr in lrs:
        times = 1000
        theta = np.random.randn(2, 1)
        m = 100
        for _ in range(10):
            gradients = 2 / m * x_p.T.dot(x_p.dot(theta) - y)
            theta = theta - lr * gradients
            plt.plot(X,X*theta[0]+theta[1])

    plt.show()



def fun4():
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    x_p = np.c_[np.ones((100, 1)), X]
    lrs = [0.001,0.005,0.01,0.05,0.1]
    plt.scatter(X, y)
    for lr in lrs:
        sgd = SGDRegressor(eta0=lr, max_iter=1000)
        sgd.fit(X, y)
        plt.plot(X, X * sgd.intercept_ + sgd.coef_)
    plt.show()


def plotOfSinAndSog():
    X = np.linspace(0, 50, 1000).reshape(1000, 1)

    #plt.plot(X, np.sin(X), label='sign')
    plt.plot(X, 1/(1+np.log(X)), label='sigmoid')
    plt.legend()
    plt.show()


def testLogisticRegression():
    """

    :return:
    """
    datasets = load_iris()
    X = datasets["data"][:, 3:]
    y = (datasets["target"] == 2).astype(np.int)
    logisticregression  = LogisticRegression()
    logisticregression.fit(X,y)
    print(X)
    X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
    y_proba = logisticregression.predict_proba(X_new)
    plt.plot(X_new, y_proba[:, 1], "g-", label="Iris virginica")
    plt.plot(X_new, y_proba[:, 0], "b--", label="Not Iris virginica")
    plt.show()
    return True

def main():
    #fun2()
    testLogisticRegression()

if __name__ == '__main__':
    main()
