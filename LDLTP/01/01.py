"""
Author:
Purpose:  SIMulate perceptron
Date：

"""
import argparse
import random
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def computePerceptron(w, x):
    """

    :return:  input matrix weight and input
    """
    z = 0
    for i in range(len(x)):
        z = z + x[i]*w[i]
    # sign fu
    if z > 0:
        return 1
    else:
        return -1

def show_learning(w):
    """

    :param w:
    :return:
    """
    print('w0 =', '%5.2f' % w[0], ', w1 =', '%5.2f' % w[1],
          ', w2 =', '%5.2f' % w[2])

def main():
    """the entrance of this file"""
    random.seed(7)  # To make repeatable
    LEARNING_RATE = 0.1
    index_list = [0, 1, 2, 3]  # Used to randomize order

    # Define training examples.
    x_train = [(1.0, -1.0, -1.0), (1.0, -1.0, 1.0),
               (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)]  # Inputs
    y_train = [1.0, 1.0, 1.0, -1.0]  # Output (ground truth)

    # Define perceptron weights.
    w = [0.2, -0.6, 0.25]  # Initialize to some "random" numbers

    all_correct = False
    while not all_correct:
        all_correct = True
        random.shuffle(index_list)  # Randomize order
        for i in index_list:
            x = x_train[i]
            y = y_train[i]
            p_out = computePerceptron(w, x)  # Perceptron function

            if y != p_out:  # Update weights when wrong
                for j in range(0, len(w)):
                    w[j] += (y * LEARNING_RATE * x[j])
                all_correct = False
                show_learning(w)  # Show updated weights”




if __name__ == '__main__':
    main()
