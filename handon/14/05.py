"""
Author:
Purpose: classifier and localization
Date：
"""

import argparse
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
import matplotlib.pyplot   as plt



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


    dataset, info = tfds.load("tf_flowers", as_supervised=True, with_info=True)
    class_names = info.features["label"].names
    n_classes = info.features["label"].num_classes
    test_set_raw, valid_set_raw, train_set_raw = tfds.load(
        "tf_flowers",
        split=["train[:10%]", "train[10%:25%]", "train[25%:]"],
        as_supervised=True)

    plt.figure(figsize=(12, 10))
    index = 0
    for image, label in train_set_raw.take(9):
        index += 1
        plt.subplot(3, 3, index)
        plt.imshow(image)
        plt.title("Class: {}".format(class_names[label]))
        plt.axis("off")

    plt.show()

    base_model = keras.applications.xception.Xception(weights="imagenet",
                                                      include_top=False)
    avg = keras.layers.GlobalAveragePooling2D()(base_model.output)
    class_output = keras.layers.Dense(n_classes, activation="softmax")(avg)
    loc_output = keras.layers.Dense(4)(avg)
    model = keras.Model(inputs=base_model.input,
                        outputs=[class_output, loc_output])
    optimizer = keras.optimizers.SGD(learning_rate=0.2, momentum=0.9, decay=0.01)
    model.compile(loss=["sparse_categorical_crossentropy", "mse"],
                  loss_weights=[0.8, 0.2],  # depends on what you care most about
                  optimizer=optimizer, metrics=["accuracy"])
    model.summary()


if __name__ == '__main__':
    main()
