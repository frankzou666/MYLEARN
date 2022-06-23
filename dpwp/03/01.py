"""
Author:
Purpose:
Date：
"""

import argparse
from keras import  layers
import keras
import tensorflow as tf


tf.get_logger().setLevel('DEBUG')

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
    model = keras.Sequential()
    dense1 = layers.Dense(units=32, input_shape=(784,))
    dense2 = layers.Dense(units=32)
    model.add(dense1)
    model.add(dense2)




if __name__ == '__main__':
    main()
