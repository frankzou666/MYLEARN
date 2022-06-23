
"""
Author:
Purpose:
Date：
"""


import argparse
from tensorflow.keras.applications.vgg16 import VGG16,decode_predictions
from tensorflow import keras
from keras.utils.vis_utils import plot_model
from  keras.preprocessing.image  import load_img,img_to_array

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main():
    FILE = 'c:\\1\\7.jpg'
    model = VGG16()
    img = load_img(path=FILE,target_size=(224,224))
    imgarray = img_to_array(img)
    imgarray = imgarray.reshape((1,imgarray.shape[0],imgarray.shape[1],imgarray.shape[2]))
    result = model.predict(imgarray)
    print(decode_predictions(result)[0][0])


if __name__ == '__main__':
    main()