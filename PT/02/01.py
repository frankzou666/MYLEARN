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
    #v1
    """
    tf._compat.disable_v2_behavior()
    h = tf.constant('hello')
    q = tf.constant(' tensorflow')
    hq = h+q
    sess = tf.compat.v1.Session()
    print(sess.run(hq))
    """
    """
    h = tf.constant('hello')
    q = tf.constant(' tensorflow')
    hq = h+q
    print(tf.__version__)
    print(hq)
    """
    """
    tf._compat.disable_v2_behavior()
    h = tf.ones((50,50))
    h2 = tf.constant([1,9,2])
    sess = tf.compat.v1.Session()
    print(sess.run(h))
    print(sess.run(tf.negative(h2)))
    """
    """
    tf._compat.disable_v2_behavior()
    h2 = tf.constant(12)
    v1 = tf.Variable(h2+10)
    with tf.compat.v1.Session() as sess:
         z = tf.compat.v1.global_variables_initializer()
         sess.run(z)
         print(sess.run(v1))
    """
    """
    tf._compat.disable_v2_behavior()
    p1 = tf.compat.v1.placeholder(tf.int32,shape=[2,2])
    p2 = tf.compat.v1.placeholder(tf.int32,shape=[2,2])
    with tf.compat.v1.Session() as sess:
        c = tf.matmul(p1,p2)
        print(sess.run(c,feed_dict={p1: [[2,3],[2,3]], p2: [[2,3],[2,3]]}))
    """

    """
    tf._compat.disable_v2_behavior()
    p1 = tf.compat.v1.placeholder(tf.int32)
    p2 = tf.compat.v1.placeholder(tf.int32)
    with tf.compat.v1.Session() as sess:
        c = tf.add(p1, p2)
        print(sess.run(c, feed_dict={p1: 11, p2: 12}))
    """
    tf._compat.disable_v2_behavior()
    c1 = tf.constant(5)
    with tf.compat.v1.Session() as sess:
        print(sess.run(tf.add(c1,c1)))
        print(sess.run(tf.multiply(c1, c1)))
        print(sess.run(tf.subtract(c1, c1)))
        print(sess.run(tf.pow(c1, c1)))



if __name__ == '__main__':
    main()
