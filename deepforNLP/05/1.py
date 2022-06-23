
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import  PorterStemmer
import requests
import numpy as np

def main2():
    textpath= 'C:\\1\\pg5200.txt'
    file = open(textpath,'r')
    textline = file.read()
    file.close()
    words = textline.split()
    words = [word.lower() for word in words]
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    stripped = [re_punc.sub('', w) for w in words]
    print(stripped[:100])


def main3():
    textpath= 'C:\\1\\pg5200.txt'
    file = open(textpath,'r')
    textline = file.read()
    file.close()
    words = nltk.word_tokenize(textline)
    words = [word.lower() for word in words]
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    words = [re_punc.sub('', w) for w in words]
    words = [word for word in words if word.isalpha()]
    stopword = stopwords.words('english')
    words = [word for word in words if word not in stopword]
    porterstemmer = PorterStemmer()
    words = [porterstemmer.stem(word) for word in words]
    print(words[:50])

def main6():

    #read file
    with open('metamorphosis_clean.txt','r') as f:
        text = f.read()
    tokener = nltk.tokenize.word_tokenize(text)

    #remove non isalpha
    words = [ word for word in tokener if word.isalpha()]

    #change to lower()
    words = [word.lower() for word in words]
    #remove punctuation and non-printable
    reprunc = re.compile('[%s]'%re.escape(string.punctuation))
    words = [reprunc.sub('',word) for word in words]
    repprint = re.compile('[^%s]' % re.escape(string.printable))
    words = [repprint.sub('', word) for word in words]
    #remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('english'))
    words = [word for word in words if not word in stopwords]
    #stemmer
    porterstemmer =  PorterStemmer()
    words = [porterstemmer.stem(word) for word in words]


    print(words[:100])



def main():
    n1 = np.array([['aa','b','c'],['a','e','c'],['q','w','v']])
    vocab =sorted(set(n1.flatten()))
    onehots= np.zeros((n1.shape[0],len(vocab)))
    print(vocab)
    for i in range(0,onehots.shape[0]):
        for j in range(0,onehots.shape[1]):
               for item in vocab:
                   if item in n1[i]:
                       onehots[i][vocab.index(item)] =1
    print(onehots)


if __name__ == '__main__':
    main()