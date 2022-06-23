
"""
Author:
Purpose: base mnsit dataset ,CNN,recognition hand write digitial
Date：
"""


import argparse
import tkinter as tk
from PIL import  Image,ImageDraw
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.layers import MaxPooling2D
from keras.datasets import mnist
from keras.preprocessing import image as kerasimage
from tensorflow.keras.utils import to_categorical
import os
from PIL import EpsImagePlugin

#download from https://www.ghostscript.com/download/gsdnld.html
EpsImagePlugin.gs_windows_binary='C:\\Program Files\\gs\\gs9.55.0\\bin\\gswin64c.exe'


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def getMnist():
    """
        :arg
        :return  mnist data
        :date
    """
    (traindata,trainlabel),(testdata,testlabel) = mnist.load_data()
    traindata = traindata.reshape((60000, 28, 28, 1))
    traindata = traindata.astype('float32') / 255.
    testdata = testdata.reshape((10000, 28, 28, 1))
    testdata = testdata.astype('float32') / 255.
    trainlabel = to_categorical(trainlabel)
    testlabel = to_categorical(testlabel)
    return traindata,trainlabel,testdata,testlabel



def getModel(filename):
    """
           :arg
           :return model
           :date
    """
    traindata, trainlabel, testdata, testlabel = getMnist()
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu', input_shape=(28, 28, 1)))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(64, (2, 2), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2,2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(512, activation='relu'))
    model.add(keras.layers.Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x=traindata,y=trainlabel, epochs=10, batch_size=32,validation_split=0.2)
    model.save(filename)
    return  model

class MainWin():
    def __init__(self,model):
        self.model = model
        self.window = tk.Tk()
        self.window.title = 'HandWrite Recognition App'
        self.canvas = tk.Canvas(self.window,width=300,height=300,bg='white',cursor='cross')
        self.button2 = tk.Button(self.window, text='clean', command=self.cleanCanvas)
        self.button3 = tk.Button(self.window, text='predi', command=self.saveImage)
        self.label = tk.Label(self.window)
        self.button2.pack()
        self.button3.pack()
        self.label.pack()
        self.canvas.bind("<Button-1>", self.getXY)
        self.canvas.bind("<B1-Motion>",self.draw_smth)
        self.canvas.pack()
        self.window.mainloop()

    def cleanCanvas(self):
        """
            :arg
            :return clean all canvas object and reset ImageDraw object
            :date
        """
        self.canvas.delete('all')
        self.label['text'] = ''

    def getXY(self,event):
         self.lastX=event.x
         self.lasty=event.y

    def draw_smth(self,event):
        """
             :arg
             :return draw line on canvas ,draw imagedraw object
            :date
        """
        self.linex = event.x
        self.liney = event.y
        self.line = self.canvas.create_oval((self.lastX, self.lasty, self.linex, self.liney),
                           fill='black',width=15
                           )
        self.lastX = event.x
        self.lasty = event.y

    def saveImage(self):
        """
            :arg
            :return predict image.update label['txt]
            :date
        """
        self.img= None
        self.canvas.postscript(file= 'm.eps')
        self.img = Image.open('m.eps')
        self.img.save('m.jpg','jpeg')
        self.img = self.img.resize((28,28))
        loadimage = self.img.convert('L')
        imgarray = np.array(loadimage)
        imgarray = imgarray.reshape((1,28,28,1))
        imgarray = imgarray.astype('float32')/255.
        predictresult = self.model.predict([imgarray])[0]
        proablitystr = round(max(predictresult) * 100)
        resultstr = np.argmax(predictresult)
        self.label['text'] = 'result: %s,proab:%s%%' % (str(resultstr), str(proablitystr))




def main():
    """
         :arg
         :return main,get keras model,creat Tk object
        :date
    """
    filename = 'm.h5'
    if not os.path.exists(filename):
         model = getModel(filename)
    else:
         model = load_model(filename)
    MainWin(model)


if __name__ == '__main__':
    """
        :arg
        :return app run
        :date
    """
    main()