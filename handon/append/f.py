
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
    #string as byte
    t1 = tf.constant(b'hello')
    print(t1)

if __name__ == '__main__':
    main()