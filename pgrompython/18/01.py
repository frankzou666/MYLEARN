
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
    return  argparser.parse_args()


class Error(Exception):
    pass

class MyStack():
    def __init__(self):
        self.stack = []
    def push(self,obj):
        self.stack = [obj] , self.stack
    def pop(self):
        if not self.stack:
            raise  Error('stack is empty')
        pop,self.stack = self.stack
        return  pop
    def isIn(self,obj):
        if obj in self.stack:
            return  1
        else:
            return 0
    def empty(self):
        pass

    def getAll(self):
        return self.stack


def getBinaryTree(res:dict,item:object):
     if len(res.items()) == 0:
         res = {str(item):[0,0]}
         return  res
     if item < 4:
         res['4'][0] = item
         res[str(item)] = [0,0]
     if item > 4 :
         res['4'][1] = item
         res[str(item)] = [0,0]

     return  res

def updateBinarTree(res:dict,root:object,item:object):
    if int(res[root][0]) > item:
        res[str(res[root][0])][0] = item
        res[str(item)] = [0,0]

    if item > int(root) and int(res[root][1]) < item:
        res[str(res[root][1])][1] = item
        res[str(item)] = [0,0]
    return  res


def main():
    res = {}
    res = getBinaryTree(res, 4)
    res = getBinaryTree(res, 2)
    res = getBinaryTree(res, 9)
    print(res)
    res = updateBinarTree(res, '4', 1)
    print(res)
    res = updateBinarTree(res, '4', 13)
    res = updateBinarTree(res, '4', 8)
    print(res)
    print(res)


def test(reps):
    import time
    start = time.time()
    for i in range(reps):
        main()
    print(time.time()-start)
if __name__ == '__main__':
    main()