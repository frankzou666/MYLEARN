
"""
Author:
Purpose:
Date：
"""


import argparse
from keras.preprocessing.text import Tokenizer
import keras
from keras.layers import TimeDistributed,Dense,GRU
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
    tokenizer = Tokenizer(char_level=True)
    model = keras.models.Sequential()
    model.add(keras.layers.GRU(128, return_sequences=True,
                               stateful=True, dropout=0.2,
                               recurrent_dropout=0.2,
                               batch_input_shape=(100,None,39)))
    model.add(keras.layers.GRU(128,return_sequences=True,
                               stateful=True,dropout=0.2,
                               recurrent_dropout=0.2))
    model.add(TimeDistributed(Dense(39,activation='softmax')))
    model.summary()

if __name__ == '__main__':
    main()