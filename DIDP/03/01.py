"""
Author:
Purpose:
Date：
"""

import argparse
from mxnet import np
from mxnet import gluon
from mxnet.gluon import nn
import math
from matplotlib import pyplot  as plt
import datetime

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def normalGussian(x,mu,sigmod):
    p = 1/math.sqrt(2*math.pi*sigmod)
    p*np.exp(-0.5/sigmod**2*(x-mu)**2)
    """the entrance of this file"""
    n = np.linspace(-10, 10, 100)

    params = [[0, 1], [0, 2], [3, 1]]
    for mu, sigmod in params:
        y = p*np.exp(-0.5/sigmod**2*(x-mu)**2)
        plt.plot(n, y, label='mu {} sigmod {}'.format(mu, sigmod))
    plt.legend()
    plt.show()

def generaterNormal(w, b, num):
    x = np.random.normal(0,1,(num,len(w)))
    y = np.dot(x,w) + b
    y = y.reshape((-1, 1))
    y = y + np.random.normal(0.01,0.5,y.shape)
    plt.scatter(x[:,(1)],y)
    plt.show()
    print(x)

def getSeqModel():
    model = nn.Sequential()
    model.add(nn.Dense(1))
    loss =  gluon.loss.L2Loss()
    trainer = gluon.Trainer(model.collect_params(), 'sgd', {'learning_rate': 0.03})


def getFasionMinst():
    X = gluon.data.vision.FashionMNIST(train=True)
    y = gluon.data.vision.FashionMNIST(train=False)
    return  X,y

def main():
    print(datetime.datetime.date())




if __name__ == '__main__':
    main()


