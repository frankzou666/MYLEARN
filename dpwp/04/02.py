"""
Author:
Purpose:
Date：
"""

import argparse
from keras import models
from keras.layers import Dense,Dropout
from keras import regularizers

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
    model = models.Sequential()
    model.add(Dense(32, input_shape=(10000,), activation='relu'))
    model.add(Dropout(0.02))
    model.add(Dense(16, activation='relu', kernel_regularizer=regularizers.l2(0.0001)))
    model.add(Dense(1, activation='sigmoid'))
    model.summary()


if __name__ == '__main__':
    main()
