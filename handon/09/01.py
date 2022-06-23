"""
Author:
Purpose:
Date：
"""

import argparse
from sklearn.cluster import KMeans
from sklearn.datasets import  load_iris

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def loadData():
    data = load_iris()
    return  data

def main():
    """the entrance of this file"""
    k = 5
    data = loadData()
    xtrain = data["target"].reshape(-1,1)
    kmean = KMeans(n_clusters=k)
    ypred = kmean.fit_predict(xtrain)
    print(kmean.cluster_centers_)
    print(kmean.transform(xtrain))



if __name__ == '__main__':
    main()
