"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
import keras
from  keras.preprocessing.text  import one_hot

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
    docs = ['Well done!',
            'Good work',
            'Great effort',
            'nice work',
            'Excellent!',
            'Weak',
            'Poor effort!',
            'not good',
            'poor work',
            'Could have done better.']
    vocab_size=100
    max_length = 4
    one_hot_docs = [one_hot(word,vocab_size) for word in docs]
    print(one_hot_docs)
    padded_docs = keras.preprocessing.sequence.pad_sequences(one_hot_docs, maxlen=max_length, padding='post')
    print(padded_docs)



if __name__ == '__main__':
    main()
