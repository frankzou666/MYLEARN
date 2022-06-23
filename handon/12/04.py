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
    return argparser.parse_args()


def cube(x):
    return  x**3

@tf.function
def tf_cube(x):
    return  x**3


def main():
    """the entrance of this file"""
    #y = cube(tf.constant(4))
    y = tf_cube(tf.constant(4))
    z = tf_cube(tf.constant(4))
    print(id(y))
    print(id(z))


if __name__ == '__main__':
    main()
