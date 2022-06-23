
"""
Author:
Purpose:
Date：
"""


import argparse
import tensorflow as tf

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
    x = tf.range(5)
    dataset = tf.data.Dataset.from_tensor_slices(x)
    dataset = dataset.repeat(3)
    """
    for item in dataset.shuffle(buffer_size=100):
        print(item)
    """
    ds2 = tf.data.Dataset.range(10).repeat(3)
    for item in ds2.shuffle(buffer_size=100, seed=10):
        print(item)



if __name__ == '__main__':
    main()