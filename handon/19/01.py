
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
    convert = tf.lite.TFLiteConverter.from_saved_model(r'C:\1\2')
    model =  convert.convert()
    with open(r'c:\1\tf.lite','wb') as f:
        f.write(model)


if __name__ == '__main__':
    main()