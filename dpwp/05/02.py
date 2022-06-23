
import tensorflow as tf
import numpy as np
import keras
import matplotlib.pyplot   as plt
from keras import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten
from keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from keras.losses import CategoricalCrossentropy
from keras.applications.vgg16 import VGG16
import os
import shutil
import json
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import sys
from tensorflow.keras.applications import VGG16

def split_data():
    BASE_DIR="C:\\1\\dogandcat\\train"
    TRAIN_DIR="C:\\1\dogandcat\\train-data"
    VAILD_DIR="C:\\1\dogandcat\\valid-data"
    TEST_DIR = "C:\\1\dogandcat\\test-data"
    #copy train data
    traindatafnames = [ 'cat.{}.jpg'.format(x) for x in range(0,1000)]
    for fname in traindatafnames:
        desfn= os.path.join(TRAIN_DIR,'cat',fname)
        srcfn=  os.path.join(BASE_DIR, fname)
        shutil.copyfile(srcfn,desfn)

    traindatafnames = ['dog.{}.jpg'.format(x) for x in range(0, 1000)]
    for fname in traindatafnames:
        desfn = os.path.join(TRAIN_DIR, 'dog',fname)
        srcfn = os.path.join(BASE_DIR, fname)
        shutil.copyfile(srcfn, desfn)

    #copy validate data
    validdatafnames = ['cat.{}.jpg'.format(x) for x in range(1000, 1500)]
    for fname in validdatafnames:
        desfn = os.path.join(VAILD_DIR,'cat', fname)
        srcfn = os.path.join(BASE_DIR, fname)
        shutil.copyfile(srcfn, desfn)

    validdatafnames = ['dog.{}.jpg'.format(x) for x in range(1000, 1500)]
    for fname in validdatafnames:
        desfn = os.path.join(VAILD_DIR,'dog', fname)
        srcfn = os.path.join(BASE_DIR, fname)
        shutil.copyfile(srcfn, desfn)

    # copy test data
    testdatafnames = ['cat.{}.jpg'.format(x) for x in range(1500, 2000)]
    for fname in testdatafnames:
        desfn = os.path.join(TEST_DIR,'cat', fname)
        srcfn = os.path.join(BASE_DIR, fname)
        shutil.copyfile(srcfn, desfn)
    testdatafnames = ['dog.{}.jpg'.format(x) for x in range(1500, 2000)]
    for fname in testdatafnames:
        desfn = os.path.join(TEST_DIR,'dog', fname)
        srcfn = os.path.join(BASE_DIR, fname)
        shutil.copyfile(srcfn, desfn)


def jpgToGeneror(datadir):

    datagenerator = ImageDataGenerator(rescale=1./225)
    result = datagenerator.flow_from_directory(
        datadir,
        target_size=(150,150),
        batch_size=20,
        class_mode='binary'
    )
    return result

"""
   func:
   author:
   date

"""
def plotModelMetric(history):
    accuracy = history.history['accuracy']
    x = [x for x in range(1, len(accuracy) + 1)]
    acc_y = history.history['accuracy']
    valacc_y = history.history['val_accuracy']
    plt.plot(x, acc_y, 'b', label='accuracy')
    plt.plot(x, valacc_y, 'bo', label='validate_accuracy')
    plt.legend()
    plt.show()


def loadImage():
    img = image.load_img('C:\\1\\dogandcat\\valid-data\\cat\\cat.1000.jpg',target_size=(150,150))
    imgarray = image.img_to_array(img)
    imgarray = np.expand_dims(imgarray,axis=0)
    imgarray = imgarray/225.
    return imgarray


def main():

      TRAIN_DIR = "C:\\1\dogandcat\\train-data"
      VAILD_DIR = "C:\\1\dogandcat\\valid-data"
      TEST_DIR = "C:\\1\dogandcat\\test-data"
      print('getModel...')
      model = Sequential()
      model.add(Conv2D(64,(3,3),activation='relu',input_shape=(150,150,3)))
      model.add(MaxPooling2D(2,2))
      model.add(Conv2D(128,(3,3),activation='relu'))
      model.add(MaxPooling2D(2, 2))
      model.add(Conv2D(128, (3, 3), activation='relu'))
      model.add(MaxPooling2D(2, 2))
      model.add(Flatten())
      model.add(keras.layers.Dropout(0.5))
      model.add(Dense(512,activation='relu'))
      model.add(Dense(1,activation='sigmoid'))
      model.compile(optimizer='rmsprop',loss= 'binary_crossentropy',metrics=['accuracy'])
      traingenerator = jpgToGeneror(TRAIN_DIR)
      validgenerator = jpgToGeneror(VAILD_DIR)
      history = model.fit_generator(
          traingenerator,
          steps_per_epoch=100,
          epochs=10,
          validation_data=validgenerator,
          validation_steps=50
      )
      model.save('c:\\1')








if __name__ == '__main__':
    main()