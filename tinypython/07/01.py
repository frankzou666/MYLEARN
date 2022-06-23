
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
    argparser.add_argument('latters',metavar='latters',nargs='+', help='input latters')
    return  argparser.parse_args()

def main():
    args = getargs()
    print(args)
    for item in args.latters:
         print(item)

if __name__ == '__main__':
    main()


