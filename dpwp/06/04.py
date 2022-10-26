"""
Author:
Purpose:
Date：
"""
import argparse

import keras
import numpy as np
from keras import layers
from keras.models import Sequential
from keras.optimizers import RMSprop
from matplotlib.pyplot import  plot as plt
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def generator(data, lookback, delay, min_index, max_index,
              shuffle=False, batch_size=128, step=6):
    if max_index is None:
        max_index = len(data) - delay - 1
    i = min_index + lookback
    while 1:
        if shuffle:
            rows = np.random.randint(
                min_index + lookback, max_index, size=batch_size)
        else:
            if i + batch_size >= max_index:
                i = min_index + lookback
            rows = np.arange(i, min(i + batch_size, max_index))
            i += len(rows)
        samples = np.zeros((len(rows),
                           lookback // step,
                           data.shape[-1]))
        targets = np.zeros((len(rows),))
        for j, row in enumerate(rows):
            indices = range(rows[j] - lookback, rows[j], step)
            samples[j] = data[indices]
            targets[j] = data[rows[j] + delay][1]
        yield samples, targets



def dataTest():
    """the entrance of this file"""
    fname ='jena_climate_2009_2016.csv'
    f= open(fname)
    data= f.read()
    f.close()
    data=data.split('\n')
    header = data[0].split(',')
    lines=data[1:]
    #create new numpy size
    float_data = np.zeros((len(lines), len(header) - 1))

    #enumerate, i get index number
    for i, line in enumerate(lines):
        value=[float(x) for x in line.split(',')[1:]]
        float_data[i,:]=value
    from matplotlib import pyplot as plt
    # the last column
    temp = float_data[:, 1]
    # fist 1440
    #plt.plot(range(1440),temp[0:1440])
    # all
    plt.plot(range(len(temp)),temp[:])
    plt.show()

def plotHistory(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.legend()
    plt.show()


def main():
    fname = 'jena_climate_2009_2016.csv'
    f = open(fname)
    data = f.read()
    f.close()
    data = data.split('\n')
    header = data[0].split(',')
    lines = data[1:]
    # create new numpy size
    float_data = np.zeros((len(lines), len(header) - 1))

    # enumerate, i get index number
    lookback = 1440
    step = 6
    delay = 144
    batch_size = 128

    train_gen = generator(float_data,
                          lookback=lookback,
                          delay=delay,
                          min_index=0,
                          max_index=200000,
                          shuffle=True,
                          step=step,
                          batch_size=batch_size)
    val_gen = generator(float_data,
                        lookback=lookback,
                        delay=delay,
                        min_index=200001,
                        max_index=300000,
                        step=step,
                        batch_size=batch_size)
    test_gen = generator(float_data,
                         lookback=lookback,
                         delay=delay,
                         min_index=300001,
                         max_index=None,
                         step=step,
                         batch_size=batch_size)
    val_steps = (300000 - 200001 - lookback)


    test_steps = (len(float_data) - 300001 - lookback)


    for i, line in enumerate(lines):
        value = [float(x) for x in line.split(',')[1:]]
        float_data[i, :] = value
    model= Sequential()
    model.add(layers.GRU(32, input_shape=(None, float_data.shape[-1])))
    model.add(layers.Dense(1))
    model.compile(optimizer=RMSprop(), loss='mae')
    history = model.fit_generator(train_gen,
                                  steps_per_epoch=500,
                                  epochs=20,
                                  validation_data=val_gen
                                  )
    plotHistory(history)

if __name__ == '__main__':
    main()
