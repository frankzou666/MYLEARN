
"""
Author:
Purpose:
Date：
"""


import argparse
from numpy import array
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from keras.utils.vis_utils import plot_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def generate_seq(model, tokenizer, seed_text, n_words):
   in_text, result = seed_text, seed_text
   for _ in range(n_words):
       encoded = tokenizer.texts_to_sequences([in_text])[0]
       encoded = array(encoded)
       yhat = model.predict(encoded, verbose=0)
       out_word = ''
       for word, index in tokenizer.word_index.items():
           if index == yhat:
              out_word = word
              break
       in_text, result = out_word, result + ' ' + out_word
   return result


def main():
    data = """ Jack and Jill went up the hill\n
    To fetch a pail of water\n
    Jack fell down and broke his crown\n
    And Jill came tumbling after\n """
    tokenizer = Tokenizer()
    sequences = list()
    tokenizer.fit_on_texts([data])
    encoded = tokenizer.texts_to_sequences([data])[0]
    vocab_size = len(tokenizer.word_index) + 1
    for i in range(1, len(encoded)):
        sequence = encoded[i - 1:i + 1]
        sequences.append(sequence)
    sequences = array(sequences)
    X, y = sequences[:, 0], sequences[:,1]
    y = to_categorical(y, num_classes=vocab_size)
    model = Sequential()
    model.add(Embedding(vocab_size,10,input_length=1))
    model.add(LSTM(50))
    model.add(Dense(vocab_size,activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    model.fit(X,y,epochs=500,verbose=2)
    print(generate_seq(model, tokenizer, 'Jack', 6))






if __name__ == '__main__':
    main()

