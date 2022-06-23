

"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import  Pipeline
from sklearn.datasets import make_moons
from sklearn.manifold import LocallyLinearEmbedding
import matplotlib.pyplot as plt

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main2():
    np.random.seed(4)
    m = 60
    w1, w2 = 0.1, 0.3
    noise = 0.1
    angles = np.random.rand(m) * 3 * np.pi / 2 - 0.5
    X = np.empty((m, 3))
    X[:, 0] = np.cos(angles) + np.sin(angles) / 2 + noise * np.random.randn(m) / 2
    X[:, 1] = np.sin(angles) * 0.7 + noise * np.random.randn(m) / 2
    X[:, 2] = X[:, 0] * w1 + X[:, 1] * w2 + noise * np.random.randn(m)


def getSVC():
    X = np.linspace(0,16,10).reshape(-1,2)
    Xcen = X - X.mean(axis=0)
    U, s, Vt = np.linalg.svd(Xcen)
    c1 = Vt.T[:, 0]
    c2 = Vt.T[:, 1]
    print(Xcen)
    # get princaple component
    # compone to 5*5 to 5*2
    print(Xcen.dot(Vt.T[:,:1]))
    plt.scatter(X[:,0],X[:,1])
    plt.show()
    print(Xcen.dot(Vt.T[:,:1]).dot(Vt.T[:,:1].T))




def main():
    getSVC()


if __name__ == '__main__':
    main()



