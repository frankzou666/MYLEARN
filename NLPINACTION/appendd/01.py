
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
    x= np.array([1,5,3,5,7,9])
    y= np.array(['a1','a5','a3','a5','a7','a9'])
    for i in range(len(x)):
        print('X is {x},Y is {y}'.format(x= x[i],y=y[i]))
    num=np.arange(len(x))
    np.random.shuffle(num)
    print('#############')
    for item in num:
        print('X is {x},Y is {y}'.format(x=x[item], y=y[item]))

if __name__ == '__main__':
    main()