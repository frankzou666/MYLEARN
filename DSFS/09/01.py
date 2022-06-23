"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow_hub   as tfb


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
    model = tfb.KerasLayer("https://tfhub.dev/google/nnlm-en-dim128/2")


if __name__ == '__main__':
    main()
