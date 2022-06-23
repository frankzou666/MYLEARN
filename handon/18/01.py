
"""
Author:
Purpose:
Date：
"""


import argparse
import gym
from tensorflow import keras
import tensorflow as tf


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
    n_inputs = 4  # == env.observation_space.shape[0]
    model = keras.models.Sequential([
        keras.layers.Dense(5, activation="elu", input_shape=[n_inputs]),
        keras.layers.Dense(1, activation="sigmoid"),
    ])


if __name__ == '__main__':
    main()