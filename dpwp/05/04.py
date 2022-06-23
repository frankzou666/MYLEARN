import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.applications import vgg16
from tensorflow.keras.applications import VGG16
from keras.models import  Sequential
from keras import models
from keras.layers import Dense,Flatten
from keras.preprocessing.image import ImageDataGenerator,image
from keras import models
import os
import json



def loadImage():
    img = image.load_img('C:\\1\\dogandcat\\valid-data\\cat\\cat.1000.jpg',target_size=(150,150))
    imgarray = image.img_to_array(img)
    imgarray = np.expand_dims(imgarray,axis=0)
    imgarray = imgarray/225.
    return imgarray



def loadModel(path):
    modelfile = os.path.join(path,'Model.json')
    weightfile = os.path.join(path, 'Weight')
    if os.path.isfile(modelfile):
        with open(modelfile, 'r') as f:
            model = keras.models.model_from_json(json.load(f))
        model.load_weights(weightfile)
        return model
    else:
        print('model file do not exists...')
        return None


def imgShow(i):
    pass

def main():
    model = loadModel('c:\\1')
    imgarray = loadImage()
    layer_outputs = [layer.output for layer in model.layers[:8]]
    act_model = models.Model(inputs=model.input, outputs=layer_outputs)
    actions = act_model.predict(imgarray)
    firstlayer = actions[0]
    plt.matshow(firstlayer[0, :, :, 4], cmap='viridis')
    plt.show()





if __name__ == '__main__':
    main()
