"""
Author:
Purpose: linear algebra
Date："""
import argparse
from typing import List,Tuple

#define my type,and shoule be use []
Matrix = List[List[float]]

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def getShape(m:Matrix) -> Tuple[float]:
    num_rows = len(m)
    num_cols = len(m[0]) if m else 0
    return num_rows,num_cols




def main():
    """the entrance of this file"""
    A = [[1,2,3],[4,5,6]]
    B = [
        [1,2],
        [3,4],
        [5,6]
    ]
    assert getShape(A) == (2,13)




if __name__ == '__main__':
    main()
