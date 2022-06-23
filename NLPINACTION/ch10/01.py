
"""
Author:
Purpose:
Date：
"""


import argparse
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input,LSTM,Dense


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
    inputvocabsize= 100
    outputvocabsize = 100
    encoderinput = Input(shape=(None,inputvocabsize))
    encoderlstm1 = LSTM(100,return_sequences=True)(encoderinput)

    decoderinput = Input(shape=(None,  outputvocabsize))
    decoderlstm1 = LSTM(100, return_sequences=True)(decoderinput)
    output = Dense(outputvocabsize,activation='softmax')(decoderlstm1)
    model = Model(inputs=[encoderinput,decoderinput],outputs=output)
    model.compile(loss='categorical_crossentropy',optimizer='rmsprop')

if __name__ == '__main__':
    main()