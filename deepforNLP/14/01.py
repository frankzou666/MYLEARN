"""
Author:
Purpose:
Date：
"""

import argparse
import keras
from keras.layers import Embedding,Conv1D,Flatten,Dense,MaxPool1D
import tensorflow as tf

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
    model = keras.models.Sequential()
    # embedding
    model.add(Embedding(input_dim=(100,),output_dim=(10,)))
    # CNN
    model.add(Conv1D())
    model.add(MaxPool1D())
    # CNN output is 2D,?
    model.add(Flatten())
    model.add(Dense())
    model.compile()
    model.summary()


if __name__ == '__main__':
    main()
