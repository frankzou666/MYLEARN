"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
import keras
import numpy as np

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def tfTest():
    """the entrance of this file"""

    tf_options = tf.io.TFRecordOptions(compression_type='GZIP')
    # write
    data = [b'testdata',b'qq']
    with tf.io.TFRecordWriter('1.dat',options=tf_options) as tfw:
        tfw.write(data[0])
        tfw.write(data[1])

    # read,output is tensor
    dataset = tf.data.TFRecordDataset('1.dat',compression_type='GZIP')
    for item in dataset:
        print(item)


def main():
    x = np.random.rand(10)
    model = keras.models.Sequential()

    model.add(keras.layers.Lambda(lambda x: (x-x.mean())/x.std()))


if __name__ == '__main__':
    main()
