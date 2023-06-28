import os
import numpy as np
import keras
from keras.preprocessing import image as image_util
from keras.models import  Sequential
from keras.layers import  Dense,SimpleRNN
from  keras.utils import np_utils
from keras.losses import BinaryCrossentropy
from keras.preprocessing.text import  Tokenizer
from keras.datasets import imdb
from keras import preprocessing
import  matplotlib.pyplot as plt
import tensorflow as tf
import sys
import random
import ssl
from keras.applications import inception_v3
from keras import backend as K
import scipy
from tensorflow.keras.preprocessing import image



tf.compat.v1.disable_eager_execution()
ssl._create_default_https_context = ssl._create_unverified_context

def resize_img(img, size):
    img = np.copy(img)
    factors = (1,
               float(size[0]) / img.shape[1],
               float(size[1]) / img.shape[2],
               1)
    return scipy.ndimage.zoom(img, factors, order=1)




def preprocess_image(image_path):
    # Util function to open, resize and format pictures
    # into appropriate tensors.
    img = image.load_img(image_path)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = inception_v3.preprocess_input(img)
    return img


def deprocess_image(x):
    # Util function to convert a tensor into a valid image.
    if K.image_data_format() == 'channels_first':
        x = x.reshape((3, x.shape[2], x.shape[3]))
        x = x.transpose((1, 2, 0))
    else:
        x = x.reshape((x.shape[1], x.shape[2], 3))
    x /= 2.
    x += 0.5
    x *= 255.
    x = np.clip(x, 0, 255).astype('uint8')
    return x


def main():
    from keras import backend as K
    K.set_learning_phase = 0
    model = inception_v3.InceptionV3(weights='imagenet',include_top=False)
    # You can list all layer names using `model.summary()`.
    layer_contributions = {
        'mixed2': 0.2,
        'mixed3': 3.,
        'mixed4': 2.,
        'mixed5': 1.5,
    }

    # Get the symbolic outputs of each "key" layer (we gave them unique names).
    layer_dict = dict([(layer.name, layer) for layer in model.layers])

    # Define the loss.
    loss = K.variable(0.)
    for layer_name in layer_contributions:
        # Add the L2 norm of the features of a layer to the loss.
        coeff = layer_contributions[layer_name]
        activation = layer_dict[layer_name].output

        # We avoid border artifacts by only involving non-border pixels in the loss.
        scaling = K.prod(K.cast(K.shape(activation), 'float32'))
        loss = loss+ coeff * K.sum(K.square(activation[:, 2: -2, 2: -2, :])) / scaling
    # This holds our generated image
    dream = model.input

    # Compute the gradients of the dream with regard to the loss.
    grads = K.gradients(loss, dream)[0]

    # Normalize gradients.
    grads /= K.maximum(K.mean(K.abs(grads)), 1e-7)

    # Set up function to retrieve the value
    # of the loss and gradients given an input image.
    outputs = [loss, grads]
    fetch_loss_and_grads = K.function([dream], outputs)

    def eval_loss_and_grads(x):
        outs = fetch_loss_and_grads([x])
        loss_value = outs[0]
        grad_values = outs[1]
        return loss_value, grad_values

    def gradient_ascent(x, iterations, step, max_loss=None):
        for i in range(iterations):
            loss_value, grad_values = eval_loss_and_grads(x)
            if max_loss is not None and loss_value > max_loss:
                break
            print('...Loss value at', i, ':', loss_value)
            x += step * grad_values
        return x

    step = 0.5  # Gradient ascent step size
    num_octave = 3  # Number of scales at which to run gradient ascent
    octave_scale = 1.4  # Size ratio between scales
    iterations = 20  # Number of ascent steps per scale

    # If our loss gets larger than 10,
    # we will interrupt the gradient ascent process, to avoid ugly artifacts
    max_loss = 10.

    # Fill this to the path to the image you want to use
    base_image_path = 'Screen Shot 2023-03-30 at 15.04.17.png'

    # Load the image into a Numpy array
    img = preprocess_image(base_image_path)

    # We prepare a list of shape tuples
    # defining the different scales at which we will run gradient ascent
    original_shape = img.shape[1:3]
    successive_shapes = [original_shape]
    for i in range(1, num_octave):
        shape = tuple([int(dim / (octave_scale ** i)) for dim in original_shape])
        successive_shapes.append(shape)

    # Reverse list of shapes, so that they are in increasing order
    successive_shapes = successive_shapes[::-1]

    # Resize the Numpy array of the image to our smallest scale
    original_img = np.copy(img)
    shrunk_original_img = resize_img(img, successive_shapes[0])

    for shape in successive_shapes:
        print('Processing image shape', shape)
        img = resize_img(img, shape)
        img = gradient_ascent(img,
                              iterations=iterations,
                              step=step,
                              max_loss=max_loss)
        upscaled_shrunk_original_img = resize_img(shrunk_original_img, shape)
        same_size_original = resize_img(original_img, shape)
        lost_detail = same_size_original - upscaled_shrunk_original_img

        img += lost_detail
        shrunk_original_img = resize_img(original_img, shape)
    plt.imshow(deprocess_image(np.copy(img)))
    plt.show()

if __name__ == '__main__':
    main()
