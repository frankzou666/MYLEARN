
"""
Author:
Purpose:
Date：
"""


import argparse
import tensorflow as tf
import keras
import numpy as np
from keras import layers
import os
import sys
import random

MAXLEN = 60
STEP = 3

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def loadText(FILE):
    with open(FILE,'r') as f:
        lines = f.read().lower()
    return  lines


def vectoriztionText(text):
    """
       :arg
       :return   programare guemnts
       :date
       :func   slidup windows
    """
    sentences = []
    nextchar = []
    for i in range(0,len(text) - MAXLEN,STEP):
        sentences.append(text[i:i+MAXLEN])
        nextchar.append(text[i+MAXLEN])

    chars = sorted(list(set(text)))
    LENCHARS = len(chars)
    onehots = dict((char,chars.index(char)) for char in chars)
    x =  np.zeros((len(sentences),MAXLEN,LENCHARS),dtype=np.bool)
    y =  np.zeros((len(sentences),LENCHARS),dtype=np.bool)

    for i ,sentence in enumerate(sentences):
        for j, char in enumerate(sentence):
            x[i,j,onehots[char]] = 1
        y[i,onehots[nextchar[i]]] = 1

    return LENCHARS,chars,onehots, x,y


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def getModel(LENCHARS):
    model = keras.models.Sequential()
    model.add(layers.LSTM(128, input_shape=(MAXLEN, LENCHARS)))
    model.add(layers.Dense(LENCHARS, activation='softmax'))
    optimizer = keras.optimizers.RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    return  model

def main():
    text = loadText('nietzsche.txt')
    LENCHARS,chars,onehots, x,y = vectoriztionText(text)
    model = getModel(LENCHARS)
    for epoch in range(1, 60):
        print('epoch', epoch)
        # Fit the model for 1 epoch on the available training data
        model.fit(x, y,
                  batch_size=128,
                  epochs=1)

        # Select a text seed at random
        start_index = random.randint(0, len(text) - MAXLEN - 1)
        generated_text = text[start_index: start_index + MAXLEN]
        print('--- Generating with seed: "' + generated_text + '"')

        for temperature in [0.2, 0.5, 1.0, 1.2]:
            print('------ temperature:', temperature)
            sys.stdout.write(generated_text)

            # We generate 400 characters
            for i in range(400):
                sampled = np.zeros((1, MAXLEN, LENCHARS))
                for t, char in enumerate(generated_text):
                    sampled[0, t, onehots[char]] = 1.

                preds = model.predict(sampled, verbose=0)[0]
                next_index = sample(preds, temperature)
                next_char = chars[next_index]

                generated_text += next_char
                generated_text = generated_text[1:]

                sys.stdout.write(next_char)
                sys.stdout.flush()
            print()

if __name__ == '__main__':
    main()