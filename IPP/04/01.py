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


def getList(l):
    """

    :return:
    """
    k = 5
    ciplerkey =[]
    for i in range(len(l)):
        if i%k==0:
            ciplerkey.append(l[i:i+k])
    return  ciplerkey


def encryptText(text:list, keys:list):
    """

    :param l:
    :param key:
    :return:
    """
    r2 = []
    print('encrypt..')
    for i in range(len(keys)):
         if keys[i]<0:
             r1=[]
             for j in range(len(text)):
                 r1.append(text[j][i])
             r2.append(r1)
         else:
             r1 = []
             for j in range(len(text)):
                 r1.append(text[-j-1][i])
             r2.append(r1)

    return  r2





def decryptText(cipter: list, keys: list):
    """

    :param l:
    :param key:
    :return:
    """
    print('decryptText')
    r2 = []
    rowlen = len(cipter[0])
    for i in range(len(keys)):
        if keys[i] < 0:
            r1 = []
            for j in range(rowlen):
                r1.append(cipter[i][j])
            r2.append(r1)
        else:
            r1 = []
            for j in range(rowlen):
                r1.append(cipter[i][-j-1])
            r2.append(r1)

    r3 = []
    for i in range(len(r2[0])):
        r31 = []
        for j in range(len(r2)):
            r31.append(r2[j][i])
        r3.append(r31)
    return r3


def main():
    """the entrance of this file"""
    q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(len(q))
    l= ['firstly',
 'we',
 'declare',
 'a',
 'list',

 'that',
 'has',
 'to',
 'be',
 'converted',

 'to',
 'a',
 'string',
 'Then',
 'an',

 'empty',
 'string',
 'has',
 'loop',
 'end']
    print(len(q))
    keys=[-1,-2,-3,4,-5]
    text = getList(l)
    print(text)
    encrypttext = encryptText(text, keys)
    print(encrypttext)
    text  = decryptText(encrypttext, keys)
    print(text)


if __name__ == '__main__':
    main()
