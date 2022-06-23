
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
    argparser.add_argument('name',nargs= '+', default='world!', help='name message')
    argparser.add_argument('-s','--sorted', action='store_true', help='sort message')
    return  argparser.parse_args()

def main():
    args = getargs()
    print(args.name)
    print(type(args.name))
    print(args.sorted)

if __name__ == '__main__':
    main()