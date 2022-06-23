
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import tensorflow as tf
from tensorflow import keras

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

class MyLayer(keras.layers.Layer):
    def __init__(self,units=32,inputdims=32):
        super(MyLayer, self).__init__()
        self.units = units

    def build(self,inputdims):
        winitiler = tf.random_normal_initializer()
        binitiler = tf.zeros_initializer()
        self.w = tf.Variable(initial_value=winitiler(shape=(inputdims[-1],self.units), dtype='float32'),trainable=True)
        self.b = tf.Variable(initial_value=binitiler(shape=(self.units), dtype='float32'),trainable=True)

    def call(self,inputs):
        return  tf.matmul(inputs,self.w) + self.b


class ActivityRegularizationLayer(keras.layers.Layer):
    def __init__(self, rate=1e-2):
        super(ActivityRegularizationLayer, self).__init__()
        self.rate = rate

    def call(self, inputs):
        self.add_loss(self.rate * tf.reduce_sum(inputs))
        return inputs


class OutLayer(keras.layers.Layer):
    def __init__(self):
        super(OutLayer, self).__init__()
        self.dense = keras.layers.Dense(
            32, kernel_regularizer=tf.keras.regularizers.l2(1e-3)
        )

    def call(self, inputs):
        return self.dense(inputs)




def main():
    outlayer = OutLayer()


if __name__ == '__main__':
    main()