"""
Author:
Purpose:
Date：
"""

import argparse
import pymc3 as  mc

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
    model = mc.Model()
    # start = dict(X=2)
    with model:
        start = mc.find_MAP()
        step = mc.Metropolis()
        mc_sample = mc.sample(100000,start=start,step=step)


if __name__ == '__main__':
    main()
