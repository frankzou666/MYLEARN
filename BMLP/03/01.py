
"""
Author:
Purpose:
Date：
"""


import argparse
import tensorflow as tf
import os
import sys

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def testTFRecord():
    """test TF Record"""
    if not os.path.exists('a.tfrecord'):
        with tf.io.TFRecordWriter('a.tfrecord') as f:
            f.write('hello')
            f.write('world')
    for item in  tf.data.TFRecordDataset('a.tfrecord'):
        print(item)
    return True


class ContextTest():
    def __init__(self):
        pass

    def __enter__(self):
        print('enter contexttest..')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit contextest...')

    def run(self):
        print('i am running')



def main():
    c = ContextTest()
    with c:
        print('hello')
        c.run()

if __name__ == '__main__':
    main()