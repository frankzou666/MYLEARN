"""
Author:
Purpose:
Date：
"""

import argparse

import  pandas as pd
from mxnet import np,npx,initializer
from mxnet.gluon import nn


class Myclass():
    def __call__(self, *args, **kwargs):
        print("call method..")



def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

class MyBlock(nn.Block):
    def __init__(self, **kwargs):
        super(MyBlock, self).__init__(**kwargs)
        self.hiden=nn.Dense(256,activation='relu')
        self.out=nn.Dense(10)
    def forward(self, X):
        return  self.out(self.hiden(X))

def main():
    """the entrance of this file"""
    npx.set_np()
    net = nn.Sequential()
    net.add(nn.Dense(8, activation='relu'))
    net.add(nn.Dense(1))
    net.initialize(force_reinit=True,init=initializer.Constant(0))

    X = np.random.uniform(size=(2, 4))
    print(net[0].weight.data())
    result = net(X)
    print(X)
    print(net[1].params)



if __name__ == '__main__':
    main()
