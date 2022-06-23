"""
Author:
Purpose:
Date：
"""

import argparse
from tensorflow import keras
import ssl

ssl._create_default_https_context = ssl._create_unverified_context




def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def loadCifar():
    (xtrain,ytrain),(xtest,ytest) = keras.datasets.cifar10.load_data()
    print(ytrain[10])

def main():
    """the entrance of this file"""
    loadCifar()


if __name__ == '__main__':
    main()
