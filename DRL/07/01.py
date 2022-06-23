
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
    return  argparser.parse_args()

def main():
    n1 = np.array([1,2,3,4,5,6])
    n2 = np.array([0.1,0.1,0.1,0.1,0.2,0.4])
    #1*0.1+2*0.1+3*0.1+4*0.1+5*0.2+6*0.4
    #expectation value
    E = n1@n2
    print('Expectation Value: {e}'.format(e=E))
    #variance value
    V = (np.square(n1-n1.mean())) @ n2
    print('Variance Value: {v}'.format(v=V))
    #standed divation
    D = np.sqrt(V)
    print('starded deviation Value: {d}'.format(d=D))




if __name__ == '__main__':
    main()