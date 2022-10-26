
"""
Author:
Purpose:
Date：
"""


import argparse
import re
import string
import numpy as np
import keras
import pickle
import random
from keras.preprocessing.text import  Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential,load_model
from keras.layers import Embedding,LSTM,Dense


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def loadDoc(filename):
    """

    :param filename:
    :return:
    """
    with open(filename,'r',encoding='utf-8') as f:
        texts = f.read()
    return texts


def cleanDoc(texts):
    """

    :param texts:
    :return:
    """
    texts = texts.replace('--',' ')
    tokens = texts.split()
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    tokens = [re_punc.sub('',w) for w in tokens]
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token.lower() for token in tokens]
    return tokens

def getSequences(tokens):
    """

    :param tokens:
    :return:
    """

    length = 50 +1
    sequences = []
    for i in range(length,len(tokens)):
        sequence = tokens[i-length:i]
        sequence = ' '.join(sequence)
        sequences.append(sequence)
    return sequences


def getTokenSequences(lines):
    """

    :param lines:
    :return:
    """
    # Tokenizer from keras
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    sequences = tokenizer.texts_to_sequences(lines)
    vocab_size = len(tokenizer.word_index) + 1
    pickle.dump(tokenizer,open('tokenizer.wbl','wb'))
    return sequences,vocab_size


def getModel(vocab_size,seq_length):
    """

    :param vocab_size:
    :param seq_length:
    :return:
    """
    model = Sequential()
    model.add(Embedding(vocab_size,50,input_length=seq_length))
    model.add(LSTM(100,return_sequences=True))
    model.add(LSTM(1000))
    model.add(Dense(1000,activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    model.summary()

    return  model



def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    result = list()
    in_text = seed_text
    for _ in range(n_words):
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        yhat = model.predict(encoded, verbose=0)
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index in yhat:
                 out_word = word
                 break

        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)



def main():
    FILENAME ='republic.txt'
    texts =  loadDoc(FILENAME)
    tokens = cleanDoc(texts)
    lines = getSequences(tokens)
    sequences,vocab_size = getTokenSequences(lines)
    data = np.array(sequences)
    X = data[:,:-1]
    y = data[:,-1]
    y = to_categorical(y,num_classes=vocab_size)
    seq_length = X.shape[1]
    model = getModel(vocab_size,seq_length)
    model.fit(X,y,batch_size=2048,epochs=10)
    model.save('model.h5')
    #model = load_model('model.h5')
    tokenizer = pickle.load(open('tokenizer.wbl', 'rb'))
    seed_text = lines[random.randint(0, len(lines))]
    print(seed_text)
    generated = generate_seq(model, tokenizer, seq_length , seed_text, 50)
    print('result:')
    print(generated)



if __name__ == '__main__':
    main()