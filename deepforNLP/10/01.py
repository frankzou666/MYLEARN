

import os
import re
import nltk
import string
from collections import Counter
import keras
import tensorflow as tf
from keras.layers import Dense
from keras.preprocessing.text import  Tokenizer
import numpy as np



def loadfile(path):
    file=open(path,'r')
    line=file.read()
    file.close()
    return line

def loadpath(path,vocab):
    for file in os.listdir(path):
        if not file.endswith('.txt'):
            continue
        addvocab(os.path.join(path,file),vocab)


def addvocab(file,vocab):
    texts = loadfile(file)
    tokens = custoke(texts)
    vocab.update(tokens)

def custoke(texts):
    tokens = texts.split()
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    tokens = [re_punc.sub('', w) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    return tokens



def doctoline(filename, vocab):
    doc = loadfile(filename)
    tokens = custoke(doc)
    tokens = [w for w in tokens if w in vocab]
    return ' '.join(tokens)

def processtodoc(path,vocab):
    lines= list()
    for file in os.listdir(path):
        if not file.endswith('.txt'):
            continue
        line =   doctoline(os.path.join(path,file),vocab)
        lines.append(line)
    return lines

def savelist(lines,filename):
    data='\n'.join(lines)
    file=open(filename,'w')
    file.write(data)
    file.close()

def createtokzer(lines):
    tokenizer =Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer


def loadcleandataset(vocab):
    NEGBASEPATH = 'C:\\1\\movie\\review_polarity\\txt_sentoken\\neg'
    POSBASEPATH = 'C:\\1\\movie\\review_polarity\\txt_sentoken\\pos'
    neg = processtodoc(NEGBASEPATH,vocab)
    pos = processtodoc(POSBASEPATH, vocab)
    docs = neg+pos
    labels = [0 for _ in range(len(neg))] + [1 for _ in range(len(pos))]
    return  docs, labels



def createmodel(nwords):
    model = tf.keras.models.Sequential()
    model.add(Dense(50,input_shape=(nwords,),activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model


def predictsentiment(review,vocab,tokizer,model):
    tokens = custoke(review)
    tokerns= [token for token in tokens if token in vocab]
    lines = ' '.join(tokens)
    encodes = tokizer.texts_to_matrix([lines],mode='binary')
    yhat = model.predict(encodes)
    precentpos =  yhat[0,0]
    if round(precentpos) == 0 :
        return (1-precentpos),'NEGATIVE'
    return (precentpos), 'POSITIVE'




def main():
    NEGBASEPATH = 'C:\\1\\movie\\review_polarity\\txt_sentoken\\neg'
    POSBASEPATH = 'C:\\1\\movie\\review_polarity\\txt_sentoken\\pos'
    vocab =Counter()
    loadpath(NEGBASEPATH,vocab)
    loadpath(POSBASEPATH, vocab)
    traindocs,labels = loadcleandataset(list(vocab.keys()))
    tokenizer = createtokzer(traindocs)
    Xtrain = tokenizer.texts_to_matrix(traindocs,mode='binary')
    model = createmodel(Xtrain.shape[1])
    model.fit(Xtrain,np.array(labels),epochs=10,batch_size=32)
    texts ='you should to view.'
    percent,sentiment= predictsentiment(texts,vocab,tokenizer,model)
    print("review: %s" % (texts))
    print(percent)
    print(sentiment)

    # try to predicte bad review
    texts = 'That is bad movie.'
    print('#############')
    percent, sentiment = predictsentiment(texts, vocab, tokenizer, model)
    print("review: %s"%(texts))
    print(percent)
    print(sentiment)





if __name__ == '__main__':
    main()