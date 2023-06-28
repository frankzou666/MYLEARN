"""
Author:
Purpose:  image classificer use ResNet pretrained
Date："""
import argparse
import tensorflow_hub as hub
import ssl
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pylab as plt


ssl._create_default_https_context = ssl._create_unverified_context

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main():
    """the entrance of this file"""
    #define the global variable
    num_classes = 5
    pexles = 224
    IMAGE_SIZE = (pexles,pexles)
    BATCH_SIZE =128
    data_dir = '/Users/zoufrank/.keras/datasets/flower_photos'


    datagen_kwargs = dict(rescale=1. / 255, validation_split=.20)
    dataflow_kwargs = dict(target_size=IMAGE_SIZE, batch_size=BATCH_SIZE,
                           interpolation="bilinear")

    validata_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
    validate_generator = validata_datagen.flow_from_directory(data_dir,subset='validation',
                                                              shuffle=False,**dataflow_kwargs)

    train_datagen = validata_datagen
    train_generator = train_datagen.flow_from_directory(data_dir, subset='training',
                                                              shuffle=True, **dataflow_kwargs)

    lable_idx=(train_generator.class_indices)

    # we reserve the key and value.
    lables = dict((v,k) for k,v in lable_idx.items())

    # we only define the input and output laery
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=IMAGE_SIZE + (3,)),
        hub.KerasLayer("https://tfhub.dev/google/imagenet/resnet_v1_101/feature_vector/4",
                       trainable=False),
        tf.keras.layers.Dense(num_classes, activation='softmax', name='flower_class')
    ])
    model.build([None, 224, 224, 3])

    # we compile model
    model.compile(
        optimizer=tf.keras.optimizers.SGD(learning_rate=0.005, momentum=0.9),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True, label_smoothing=0.1),
        metrics=['accuracy'])

    ## fit
    steps_per_epoch = train_generator.samples // train_generator.batch_size
    validation_steps = validate_generator.samples // validate_generator.batch_size
    hist = model.fit(
        train_generator,
        epochs=5, steps_per_epoch=steps_per_epoch,
        validation_data=validate_generator,
        validation_steps=validation_steps).history


if __name__ == '__main__':
    main()
