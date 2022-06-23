
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main2():
    (xtrain,ytrain),(xtest,ytest) = keras.datasets.mnist.load_data()
    xtrain = xtrain.reshape(60000,784).astype('float32')/255.
    xtest = xtest.reshape(10000, 784).astype('float32') /255.
    input = keras.Input(shape=(784,))
    dense1 = layers.Dense(64,activation='relu')(input)
    dense2 = layers.Dense(64, activation="relu")(dense1)
    output =  layers.Dense(10)(dense2)
    model = keras.Model(inputs=input,outputs=output,name ='mymodel')
    model.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        optimizer=keras.optimizers.RMSprop(),
        metrics=["accuracy"],
    )
    history = model.fit(xtrain, ytrain, batch_size=64, epochs=2, validation_split=0.2)
    test_scores = model.evaluate(xtest, ytest, verbose=2)
    print("Test loss:", test_scores[0])
    print("Test accuracy:", test_scores[1])


def main3():
    encoder_input = keras.Input(shape=(28, 28, 1), name="img")
    x = layers.Conv2D(16, 3, activation="relu")(encoder_input)
    x = layers.Conv2D(32, 3, activation="relu")(x)
    x = layers.MaxPooling2D(3)(x)
    x = layers.Conv2D(32, 3, activation="relu")(x)
    x = layers.Conv2D(16, 3, activation="relu")(x)
    encoder_output = layers.GlobalMaxPooling2D()(x)

    encoder = keras.Model(encoder_input, encoder_output, name="encoder")
    encoder.summary()

    x = layers.Reshape((4, 4, 1))(encoder_output)
    x = layers.Conv2DTranspose(16, 3, activation="relu")(x)
    x = layers.Conv2DTranspose(32, 3, activation="relu")(x)
    x = layers.UpSampling2D(3)(x)
    x = layers.Conv2DTranspose(16, 3, activation="relu")(x)
    decoder_output = layers.Conv2DTranspose(1, 3, activation="relu")(x)

    autoencoder = keras.Model(encoder_input, decoder_output, name="autoencoder")
    autoencoder.summary()



def main4():
    encoder_input = keras.Input(shape=(28, 28, 1), name="original_img")
    x = layers.Conv2D(16, 3, activation="relu")(encoder_input)
    x = layers.Conv2D(32, 3, activation="relu")(x)
    x = layers.MaxPooling2D(3)(x)
    x = layers.Conv2D(32, 3, activation="relu")(x)
    x = layers.Conv2D(16, 3, activation="relu")(x)
    encoder_output = layers.GlobalMaxPooling2D()(x)

    encoder = keras.Model(encoder_input, encoder_output, name="encoder")
    encoder.summary()

    decoder_input = keras.Input(shape=(16,), name="encoded_img")
    x = layers.Reshape((4, 4, 1))(decoder_input)
    x = layers.Conv2DTranspose(16, 3, activation="relu")(x)
    x = layers.Conv2DTranspose(32, 3, activation="relu")(x)
    x = layers.UpSampling2D(3)(x)
    x = layers.Conv2DTranspose(16, 3, activation="relu")(x)
    decoder_output = layers.Conv2DTranspose(1, 3, activation="relu")(x)

    decoder = keras.Model(decoder_input, decoder_output, name="decoder")
    decoder.summary()

    autoencoder_input = keras.Input(shape=(28, 28, 1), name="img")
    encoded_img = encoder(autoencoder_input)
    decoded_img = decoder(encoded_img)
    autoencoder = keras.Model(autoencoder_input, decoded_img, name="autoencoder")
    autoencoder.summary()


def main6():
    num_tags = 12  # Number of unique issue tags
    num_words = 10000  # Size of vocabulary obtained when preprocessing text data
    num_departments = 4  # Number of departments for predictions

    title_input = keras.Input(
        shape=(None,), name="title"
    )  # Variable-length sequence of ints
    body_input = keras.Input(shape=(None,), name="body")  # Variable-length sequence of ints
    tags_input = keras.Input(
        shape=(num_tags,), name="tags"
    )  # Binary vectors of size `num_tags`

    title_features = layers.Embedding(num_words, 64)(title_input)
    body_features = layers.Embedding(num_words, 64)(body_input)
    title_features = layers.LSTM(128)(title_features)
    body_features = layers.LSTM(32)(body_features)


    x = layers.concatenate([title_features, body_features, tags_input])


    priority_pred = layers.Dense(1, name="priority")(x)
    department_pred = layers.Dense(num_departments, name="department")(x)
    model = keras.Model(
        inputs=[title_input, body_input, tags_input],
        outputs=[priority_pred, department_pred],
    )

    model.compile(
        optimizer=keras.optimizers.RMSprop(1e-3),
        loss=[
            keras.losses.BinaryCrossentropy(from_logits=True),
            keras.losses.CategoricalCrossentropy(from_logits=True),
        ],
        loss_weights=[1.0, 0.2],
    )


def main7():
    class CustomDense(layers.Layer):
        def __init__(self,units = 32):
            super(CustomDense,self).__init__()
            self.units = units

        def build(self, input_shape):
            self.w = self.add_weight(
                shape=(input_shape[-1], self.units),
                initializer="random_normal",
                trainable=True,
            )
            self.b = self.add_weight(
                shape=(self.units,), initializer="random_normal", trainable=True
            )

        def call(self,inputs):
            return  tf.matmul(inputs,self.w) + self.b

    inputs = keras.Input((4,))
    outputs = CustomDense(10)(inputs)

    model = keras.Model(inputs, outputs)



def main():
    units = 32
    timesteps = 10
    input_dim = 5

    # Define a Functional model
    inputs = keras.Input((None, units))
    x = layers.GlobalAveragePooling1D()(inputs)
    outputs = layers.Dense(1)(x)
    model = keras.Model(inputs, outputs)

    class CustomRNN(layers.Layer):
        def __init__(self):
            super(CustomRNN, self).__init__()
            self.units = units
            self.projection_1 = layers.Dense(units=units, activation="tanh")
            self.projection_2 = layers.Dense(units=units, activation="tanh")
            # Our previously-defined Functional model
            self.classifier = model

        def call(self, inputs):
            outputs = []
            state = tf.zeros(shape=(inputs.shape[0], self.units))
            for t in range(inputs.shape[1]):
                x = inputs[:, t, :]
                h = self.projection_1(x)
                y = h + self.projection_2(state)
                state = y
                outputs.append(y)
            features = tf.stack(outputs, axis=1)
            print(features.shape)
            return self.classifier(features)

    rnn_model = CustomRNN()
    _ = rnn_model(tf.zeros((1, timesteps, input_dim)))

if __name__ == '__main__':
    main()