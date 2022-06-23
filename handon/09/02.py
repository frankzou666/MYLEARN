
"""
Author:
Purpose:
Date：
"""


import argparse
from  sklearn.cluster  import KMeans,DBSCAN
from  sklearn.datasets import make_moons

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main():
    X,y=make_moons(n_samples=1000,noise=0.01)
    dbscan =DBSCAN(eps=0.05)
    dbscan.fit(X)
    print(dbscan.labels_)


if __name__ == '__main__':
    main()