"""
Author:
Purpose:
Date："""
import argparse
import os
import tensorflow
#from keras.preprocessing.image import load_img

from tensorflow.keras.preprocessing.image import load_img,img_to_array
from keras.applications.vgg16 import preprocess_input


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def load_photos(dictory):
    """

    :param dictory:
    :return:
    """
    images = dict()
    for name in os.listdir(dictory):
        file_name = os.path.join(dictory,name)
        image = load_img(file_name,target_size=(224,224))
        image_array = img_to_array(image)
        image_array = image_array.reshape((1,image_array.shape[0],image_array.shape[1],image_array.shape[2]))
        image_id = file_name.split('.')[0]
        images[image_id] = image_array
    return images


def main():
    """the entrance of this file"""
    IMAGE_DIRECTORY = '/Users/zoufrank/Documents/dev/py/MYLEARN/deepforNLP/25/Flicker8k_Dataset'

    images = load_photos(IMAGE_DIRECTORY)
    print('load images %s'%(len(images)))


if __name__ == '__main__':
    main()
