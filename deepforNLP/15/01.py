
"""
Author:
Purpose:
Date：
"""


import argparse
import re
import string
from nltk.corpus import stopwords
from os import listdir
from collections import Counter
from keras.preprocessing.text import Tokenizer
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.vis_utils import plot_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

# load doc into memory
def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def clean_doc1(doc):

    tokens = doc.split()
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    tokens = [re_punc.sub('', w) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    return tokens


def clean_doc(doc, vocab):
    tokens = doc.split()
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    tokens = [re_punc.sub('', w) for w in tokens]
    tokens = [w for w in tokens if w in vocab]
    tokens = ' '.join(tokens)
    return tokens

def add_doc_to_vocab(filename, vocab):
    doc = load_doc(filename)
    tokens = clean_doc1(doc)
    vocab.update(tokens)


def process_docs1(directory, vocab):
    for filename in listdir(directory):
        if filename.startswith('cv9'):
           continue
        path = directory + '/' + filename
        add_doc_to_vocab(path, vocab)


def process_docs(directory, vocab, is_train):
    documents = list()
    for filename in listdir(directory):
        if is_train and filename.startswith('cv9'):
            continue
        if not is_train and not filename.startswith('cv9'):
            continue
        path = directory + '/' + filename
        doc = load_doc(path)
        tokens = clean_doc(doc, vocab)
        documents.append(tokens)
    return documents




def encode_docs(tokenizer, max_length, docs):
    encoded = tokenizer.texts_to_sequences(docs)
    padded = pad_sequences(encoded, maxlen=max_length, padding='post')
    return padded


def load_clean_dataset(vocab, is_train):
# load documents
    neg = process_docs('C:\\1\\review_polarity\\txt_sentoken\\neg', vocab, is_train)
    pos = process_docs('C:\\1\\review_polarity\\txt_sentoken\\pos', vocab, is_train)
    docs = neg + pos
    labels = array([0 for _ in range(len(neg))] + [1 for _ in range(len(pos))])
    return docs, labels

 ##  how to encode docs.
def create_tokenizer(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer


def encode_docs(tokenizer, max_length, docs):
    encoded = tokenizer.texts_to_sequences(docs)
    padded = pad_sequences(encoded, maxlen=max_length, padding='post')
    return padded


def predict_sentiment(review, vocab, tokenizer, max_length, model):
    line = clean_doc(review, vocab)
    padded = encode_docs(tokenizer, max_length, [line])
    yhat = model.predict(padded, verbose=0)
    percent_pos = yhat[0,0]
    if round(percent_pos) == 0:
       return (1-percent_pos), 'NEGATIVE'
    return percent_pos, 'POSITIVE'

def define_model(vocab_size, max_length):
    model = Sequential()
    model.add(Embedding(vocab_size, 100, input_length=max_length))
    model.add(Conv1D(filters=32, kernel_size=8, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def main():
    vocab = Counter()
    # add all docs to vocab
    process_docs1('C:\\1\\review_polarity\\txt_sentoken\\pos', vocab)
    process_docs1('C:\\1\\review_polarity\\txt_sentoken\\neg', vocab)
    train_docs, ytrain = load_clean_dataset(vocab, True)
    tokenizer = create_tokenizer(train_docs)
    vocab_size = len(tokenizer.word_index) + 1
    max_length = max([len(s.split()) for s in train_docs])
    print('Maximum length: %d' % max_length)
    Xtrain = encode_docs(tokenizer, max_length, train_docs)
    model = define_model(vocab_size, max_length)
    model.fit(Xtrain, ytrain, epochs=10, verbose=2)


    text = 'Everyone will enjoy this film. I love it, recommended!'
    percent, sentiment = predict_sentiment(text, vocab, tokenizer, max_length, model)
    print('Review: [%s]\nSentiment: %s (%.3f%%)' % (text, sentiment, percent * 100))
    # test negative text
    text = 'This is a bad movie. Do not watch it. It sucks.'
    percent, sentiment = predict_sentiment(text, vocab, tokenizer, max_length, model)
    print('Review: [%s]\nSentiment: %s (%.3f%%)' % (text, sentiment, percent * 100))


if __name__ == '__main__':
    main()