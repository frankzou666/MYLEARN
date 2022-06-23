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


def sort():
    """the entrance of this file"""
    a = [9, 2, 8, 4, 68, 13, 6]
    b = []
    # 只要数组中有元素就循环
    while (len(a) > 0):
        # 每一轮到都找最大的元素
        min = a[0]
        for i in range(1, len(a)):
            if min < a[i]:
                min = a[i]
        # 把每一轮找到的最大元素放到另一个数组
        b.append(min)
        # 把对应的元素从原来的数组中删掉
        del a[a.index(min)]
    print(b)


def main():
    """the entrance of this file"""
    pass

if __name__ == '__main__':
    main()
