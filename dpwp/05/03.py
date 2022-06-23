
import keras
from keras.applications import vgg16
from tensorflow.keras.applications import VGG16
from keras.models import  Sequential
from keras.layers import Dense,Flatten
from keras.preprocessing.image import ImageDataGenerator


def jpgToGeneror(datadir):

    datagenerator = ImageDataGenerator(rescale=1./225)
    result = datagenerator.flow_from_directory(
        datadir,
        target_size=(150,150),
        batch_size=20,
        class_mode='binary'
    )
    return result


def main():
    TRAIN_DIR = "C:\\1\dogandcat\\train-data"
    VAILD_DIR = "C:\\1\dogandcat\\valid-data"
    TEST_DIR = "C:\\1\dogandcat\\test-data"
    convbase = VGG16(include_top=False,weights='imagenet',input_shape=(150,150,3))
    model = Sequential()
    traingenerator = jpgToGeneror(TRAIN_DIR)
    validgenerator = jpgToGeneror(VAILD_DIR)
    model.add(convbase)
    #convbase.trainable=False
    model.add(Flatten())
    model.add(Dense(512,activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    history = model.fit_generator(
        traingenerator,
        steps_per_epoch=100,
        epochs=10,
        validation_data=validgenerator,
        validation_steps=50
    )



if __name__ == '__main__':
    main()