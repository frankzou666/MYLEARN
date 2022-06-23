
import keras
import keras.layers
from  keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def getMnist():
    (traindata,trainlabel),(testdata,testlabel) = mnist.load_data()
    traindata = traindata.reshape((60000, 28, 28, 1))
    traindata = traindata.astype('float32') / 255
    testdata = testdata.reshape((10000, 28, 28, 1))
    testdata = testdata.astype('float32') / 255
    trainlabel = to_categorical(trainlabel)
    testlabel = to_categorical(testlabel)
    return traindata,trainlabel,testdata,testlabel


def main():
    traindata, trainlabel, testdata, testlabel =  getMnist()
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(128, (3, 3),activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(256, activation='relu'))
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    model.fit(x=traindata,y=trainlabel,epochs=5,batch_size=128)
    testloss,testacc = model.evaluate(testdata,testlabel)
    print(testacc)
    #model.save('C://Users//Administrator//PycharmProjects//untitled//tk//m.h5')




if __name__ == '__main__':
    main()