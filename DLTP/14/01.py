"""
Author:
Purpose:
Date：
"""

import argparse
from keras.layers import Input,Dense,Concatenate
from keras.models import Model

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
    input1 = Input(shape=(28,))
    input2 = Input(shape=(10,))

    dense1 = Dense(32,activation='relu')
    dense2 = Dense(32,activation='relu')
    concate = Concatenate()

    layer_ouput_1 = dense1(input1)
    concate_layer_output = concate([layer_ouput_1,input2])
    layer_ouput_2 = dense2(concate_layer_output )
    model = Model(inputs=[input1,input2],outputs=[layer_ouput_2])
    model.summary()


if __name__ == '__main__':
    main()
