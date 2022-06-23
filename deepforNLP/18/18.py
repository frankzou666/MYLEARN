
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import LSTM,Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def loaddoc(file):
    with open(file,'r') as f:
        lines = f.read()
    return  lines

def loadsequences(rawtexts):
    length = 10
    sequences = []
    tokens = ' '.join(rawtexts.split())
    for i in range(length, len(tokens)):
        # 相当于一个silde window
        seq = tokens[i - length:i + 1]
        sequences.append(seq)
    return sequences


def getModel(X,vocabsize):
     model = Sequential()
     model.add(LSTM(75,input_shape= (X.shape[1],X.shape[2])))
     model.add(Dense(vocabsize,activation='softmax'))
     model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
     return model


def generate_seq(model, mapping, seq_length, seed_text, n_chars):
    in_text = seed_text
    for _ in range(n_chars):
        encoded = [mapping[char] for char in in_text]
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        encoded = to_categorical(encoded, num_classes=len(mapping))
        #print(encoded.shape)
        #encoded = encoded.reshape(1, encoded.shape[0], encoded.shape[1])
        yhat = model.predict_classes(encoded, verbose=0)
        out_char = ''
        for char, index in mapping.items():
            if index == yhat:
                out_char = char
                break
        in_text += out_char
    return in_text


def main():
    FILE = 'fly.txt'
    rawtexts = loaddoc(FILE)
    lines = loadsequences(rawtexts)
    chars = sorted(list(set(rawtexts)))
    mappings = dict(((i,c) for c,i in enumerate(chars)))
    vocabsize =  len(mappings)
    sequences = list()
    for line in lines:
        encodeseq = [mappings[char] for char in line]
        sequences.append(encodeseq)
    sequences = np.array(sequences)
    X, y = sequences[:,:-1],sequences[:,-1]
    sequences = [to_categorical(x,vocabsize) for x in X]
    X = np.array(sequences)
    y = to_categorical(y,vocabsize)
    model = getModel(X,vocabsize)
    model.fit(X,y,epochs=100,batch_size=32,verbose=2)
    print(generate_seq(model,mappings,10,'Sing a son',20))
    print(generate_seq(model, mappings, 10, 'king was i', 20))
    print(generate_seq(model, mappings, 10, 'hello worl', 20))





if __name__ == '__main__':
    main()