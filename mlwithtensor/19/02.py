"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf


tf.get_logger().setLevel(4)

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
    print(tf.__version__)
    print(tf.config.list_physical_devices())
    #tf_session = tf.Session()
    #tf_session.run()


if __name__ == '__main__':
    main()
