"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
from tensorflow.keras.models import Sequential,model_from_json
from tensorflow.keras.layers import Conv1D,GlobalMaxPool1D,Dropout,Dense,LSTM,Flatten
import glob

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
    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
        model = Sequential()
        model.add(LSTM(32, return_sequences=True, input_shape=(100, 100)))
        model.add(Dropout(0.2))
        model.add(Flatten())
        model.add(Dense(100, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.summary()


if __name__ == '__main__':
    main()
