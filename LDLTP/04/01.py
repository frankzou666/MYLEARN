"""
Author:
Purpose:
Date："""
import argparse
import idx2numpy
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
    TRAIN_IMAGE_FILENAME = 'train-images-idx3-ubyte'
    TRAIN_IMAGE_LABEL = 'train-labels-idx1-ubyte'
    TEST_IMAGE_FILENAME = 't10k-images-idx3-ubyte'
    TEST_IMAGE_LABEL = 't10k-labels-idx1-ubyte'
    TRAIN_IMAGE = idx2numpy.convert_from_file(TRAIN_IMAGE_FILENAME)
    TRAIN_LABEL = idx2numpy.convert_from_file(TRAIN_IMAGE_LABEL)
    TEST_IMAGE = idx2numpy.convert_from_file(TEST_IMAGE_FILENAME)
    TEST_LABEL = idx2numpy.convert_from_file(TEST_IMAGE_LABEL)
    print("TRAIN_IMAGE:" ,TRAIN_IMAGE.shape)
    print("TRAIN_LABEL:", TRAIN_LABEL.shape)
    print("TEST_IMAGE:", TEST_IMAGE.shape)
    print("TEST_LABEL:", TEST_LABEL.shape)
    print("label:", TEST_LABEL[501])
    for line in TRAIN_IMAGE[501]:
        for num in line:
            if num>0:
                print('*',end=' ')
            else:
                print('', end=' ')
        print(' ')


if __name__ == '__main__':
    main()
