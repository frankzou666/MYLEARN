
"""
Author: frank oliver
Purpose: chapter 01
Date： 2022/01/23
"""
import functools
import numpy as np
import tensorflow as tf
import pandas as pd


import argparse
import os
import sys

TRAIN_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
TEST_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"

TRAIN_FILE = "train.csv"
TEST_FILE = "eval.csv"

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def downloadDataset():
    # download file, and save to filename
    print('download dataset...')
    train_file_path = tf.keras.utils.get_file(TRAIN_FILE , TRAIN_DATA_URL)
    test_file_path = tf.keras.utils.get_file(TEST_FILE, TEST_DATA_URL)
    return True


def main():
    """the entrance of this file"""
    # if dataset does not exist, dowlad
    if (not os.path.exists(TRAIN_FILE)) &  (not os.path.exists(TEST_FILE)):
        downloadDataset()
    # read data to pandas
    train_df = pd.read_csv(TRAIN_FILE,header='iner')
    test_df = pd.read_csv(TEST_FILE,header='iner')

    # make data to the tensflow. and can do one-hot code.
    LABEL_COLUMN = 'survived'
    LABELS = [0, 1]
    train_ds = tf.data.experimental.make_csv_dataset(
        TRAIN_FILE,
        batch_size=10,
        label_name=LABEL_COLUMN,
        na_value='?',
        ignore_errors=True
    )

    test_ds = tf.data.experimental.make_csv_dataset(
        TEST_FILE,
        batch_size=10,
        label_name=LABEL_COLUMN,
        na_value='?',
        ignore_errors=True
    )



if __name__ == '__main__':
    main()