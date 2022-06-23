"""
Author:  my agents code
Purpose:
Date：
"""

import argparse


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

class Agents():
    """
     this class of agent
    """
    def __init__(self):
        pass

    def go(self, n):
        raise NotImplementedError("the go() ")




class Enviorment():
    """

    """
    def initial_percepters(self):
        pass

    def do(self,action):
        raise NotImplementedError("the do() ")

def main():
    """the entrance of this file"""
    agents = Agents()
    agents.go(n=5)


if __name__ == '__main__':
    main()
