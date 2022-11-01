"""
Author:
Purpose:
Date：
"""
import argparse
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.preprocessing import sequence
from tensorflow.keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense,Conv1D,MaxPool1D,Embedding,GlobalMaxPool1D,GRU
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def loadImdb(MAX_WRODS,MAX_LENGTH):
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=MAX_WRODS)
    print(len(x_train), 'train sequences')
    print(len(x_test), 'test sequences')
    print('Pad sequences (samples x time)')
    x_train = sequence.pad_sequences(x_train, maxlen=MAX_LENGTH)
    x_test = sequence.pad_sequences(x_test, maxlen=MAX_LENGTH)
    print('x_train shape:', x_train.shape)
    print('x_test shape:', x_test.shape)
    return x_train,y_train,x_test,y_test


def getBaseModel(MAX_WRODS,MAX_LENGTH):
    model = Sequential()
    model.add(Embedding(MAX_WRODS,128,input_length=MAX_LENGTH))
    #model.add(Conv1D(32,7,activation='relu'))
    #model.add(MaxPool1D(5))
    #model.add(Conv1D(32, 7, activation='relu'))
    #model.add(GlobalMaxPool1D())
    model.add(GRU(32))
    model.add(Dense(1))
    model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['acc'])
    return  model


def main():
    """the entrance of this file"""
    # data length
    MAX_WRODS=10000
    MAX_LENGTH=50
    #load imdb
    print("load imdb...")
    X_train,y_train ,X_test,y_test =  loadImdb(MAX_WRODS, MAX_LENGTH)
    print("train data shape .."+str(X_train.shape))
    #get basemodel
    print('get model...')
    model = getBaseModel(MAX_WRODS, MAX_LENGTH)
    print('fit model...')
    # fit model
    model.fit(X_train,y_train,epochs=10,batch_size=128)



if __name__ == '__main__':
    main()
