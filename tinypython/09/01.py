
"""
Author:
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
    argparser.add_argument('--f', type=int, help='name message')
    return  argparser.parse_args()

def main():
    args = getargs()

if __name__ == '__main__':
    main()