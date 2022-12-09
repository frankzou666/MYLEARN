"""
Author:
Purpose:
Date："""
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


def main():
    """the entrance of this file"""
    x = np.array((1,3,5,7,9))
    y = np.array((-2,-4,-3,-8,-10))

    r= (x-x.mean())*(y-y.mean())
    r = r.sum()/(len(x)*x.std()*y.std())
    print(r)






if __name__ == '__main__':
    main()
