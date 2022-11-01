"""
Author:
Purpose:
Date：
"""
import argparse
import numpy as np
import torch
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
    # build modeule
    model = torch.nn.Sequential(
        torch.nn.Linear(10, 150),
        torch.nn.ReLU(),
        torch.nn.Linear(150, 4),
        torch.nn.ReLU(),
    )
    # loss function
    loss_fn = torch.nn.MSELoss()
    # optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

if __name__ == '__main__':
    main()
