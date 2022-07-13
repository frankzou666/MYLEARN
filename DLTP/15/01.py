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
    tf.compat.v1.disable_v2_behavior()
    t1 = tf.compat.v1.placeholder(tf.float64,name='t1')
    t2 = tf.compat.v1.placeholder(tf.float64,name='t2')
    tf_add = tf.add(t1,t2)
    with tf.compat.v1.Session() as sess:
        r = sess.run(tf_add,feed_dict={t1:10,t2:10})
        print(r)



if __name__ == '__main__':
    main()
