import numpy as np
from keras.utils import to_categorical
from keras.datasets import cifar10
from keras.models import Sequential,load_model
from keras.layers import Dense,Flatten
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


(x_train, y_train), (x_test, y_test) = cifar10.load_data()
NUM_CLASSES = 10
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
y_train = to_categorical(y_train, NUM_CLASSES)
y_test = to_categorical(y_test, NUM_CLASSES)


model = Sequential([
    Dense(200, activation = 'relu', input_shape=(32, 32, 3)),
    Flatten(),
    Dense(150, activation = 'relu'),
    Dense(10, activation = 'softmax'),
])

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10,batch_size=512,shuffle=True)
model.save('model1.h5')