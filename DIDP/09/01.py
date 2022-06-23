"""
Author:
Purpose:
Date：
"""

import argparse

from d2l import mxnet as d2l
from mxnet import npx
from mxnet.gluon import rnn


npx.set_np()

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
    # Load data
    batch_size, num_steps, device = 32, 35, d2l.try_gpu()
    train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)
    # Define the bidirectional LSTM model by setting `bidirectional=True`
    vocab_size, num_hiddens, num_layers = len(vocab), 256, 2
    lstm_layer = rnn.LSTM(num_hiddens, num_layers, bidirectional=True)
    model = d2l.RNNModel(lstm_layer, len(vocab))
    # Train the model
    num_epochs, lr = 50, 1
    d2l.train_ch8(model, train_iter, vocab, lr, num_epochs, device)


if __name__ == '__main__':
    main()
