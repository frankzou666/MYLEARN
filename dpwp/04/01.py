"""
Author:
Purpose:
Date：
"""

import argparse
import numpy as np

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def shuffleData(data, location):
    """

    :param data:
    :return:
    """
    np.random.shuffle(data)
    train_data = data[:location]
    validate_data = data[location:]
    return  train_data,validate_data



def kFoldData(data, K):
    """

    :param data:
    :return:
    """
    print(data)
    intervl_data = len(data) // K
    for i in range(K):
        validate_data = data[(intervl_data*i): (intervl_data*(i + 1))]
        print(validate_data)
        train_data = data[:(intervl_data*i)] + data[(intervl_data * (i + 1)):]
        print(train_data)



def main():
    """the entrance of this file"""
    np1 = [13,5,6,7,9,10]

    # interial multitimes,shuffer the data very time
    interiations =10
    for i in range(interiations):
        np.random.shuffle(np1)
        kFoldData(np1,3)




if __name__ == '__main__':
    main()
