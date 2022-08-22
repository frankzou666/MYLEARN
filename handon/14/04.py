"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
from tensorflow import keras

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
    model = keras.applications.resnet50.ResNet50(weights="imagenet")


if __name__ == '__main__':
    main()
