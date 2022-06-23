
"""
Author:
Purpose:
Date：
"""


import argparse
from tensorflow.keras.models import Sequential,model_from_json
from tensorflow.keras.layers import Conv1D,GlobalMaxPool1D,Dropout,Dense
import glob
import os
import random
from nltk.tokenize import TreebankWordTokenizer

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def getData():
     NEGPATH = 'C:\\1\\review_polarity\\txt_sentoken\\neg'
     POSPATH = 'C:\\1\\review_polarity\\txt_sentoken\\pos'
     POSLABEL=1
     NEGLABEL=0
     dataset= []
     for file in glob.glob(os.path.join(NEGPATH,'*.txt')):
         with open(file,'r') as f:
              dataset.append((NEGLABEL,f.read()))

     for file in glob.glob(os.path.join(POSPATH,'*.txt')):
         with open(file,'r') as f:
              dataset.append((POSLABEL,f.read()))

     random.shuffle(dataset)
     return  dataset


def main():
    model = Sequential()
    model.add(Conv1D(filters=16,kernel_size=3,strides=1,input_shape=(100,100)))
    model.add(GlobalMaxPool1D())
    model.add(Dense(100,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    model.summary()

if __name__ == '__main__':
    main()