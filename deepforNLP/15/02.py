"""
Author:
Purpose:
Date：
"""

import argparse
import keras
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

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
    """
       how to sequence the text.
    """
    docs =['good','df','cool']
    text =['df']
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(docs)
    text_sequence = tokenizer.texts_to_sequences(text)
    print(text_sequence)
    padded = pad_sequences(text_sequence, maxlen=10, padding='post')
    print(padded)


if __name__ == '__main__':
    main()
