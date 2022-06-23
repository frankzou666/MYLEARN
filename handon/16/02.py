
"""
Author:
Purpose:
Date：
"""


import argparse
from keras.preprocessing.text import Tokenizer
import keras
from keras.layers import TimeDistributed,Dense,GRU,Bidirectional
from keras.datasets.imdb import load_data
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
    (xtrain,ytrain),(xtest,ytest) = load_data()
    model = keras.models.Sequential()
    model.add(Bidirectional(GRU(40,return_sequences=True)))


if __name__ == '__main__':
    main()