"""
Author:
Purpose:
Date：
"""

import argparse
from decimal import Decimal

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
    print(0.3+0.3+0.3-0.6)
    print(Decimal('0.3') + Decimal('0.3') + Decimal('0.3') - Decimal('0.6'))


if __name__ == '__main__':
    main()
