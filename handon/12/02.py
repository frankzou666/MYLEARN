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


def main():
    """the entrance of this file"""
    a = tf.constant([[3,4],[5,6]])
    tf.constant(2, dtype=tf.int64) + tf.constant(tf.cast(3.0, dtype=tf.int64))


if __name__ == '__main__':
    main()
