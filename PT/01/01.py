"""
Author:
Purpose:
Date：
"""
import logging
import argparse
import tensorflow as tf
tf.get_logger().setLevel(logging.DEBUG)

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
    print(tf.version)


if __name__ == '__main__':
    main()
