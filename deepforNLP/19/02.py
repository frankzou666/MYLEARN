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
    return argparser.parse_args()


def main():
    """the entrance of this file"""
    data = """ Jack and Jill went up the hill\n
    To fetch a pail of water\n
    Jack fell down and broke his crown
    \n And Jill came tumbling after\n """
    datas = data.split(' ')
    for i in range(2,len(datas)):
        print(datas[i-2:i+1])


if __name__ == '__main__':
    main()
