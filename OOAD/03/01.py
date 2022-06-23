"""
Author:
Purpose:
Date：
"""

import argparse
from threading import Thread


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

class BaseBook():
    def __init__(self,name):
        self.name = name
    def getBook(self):
        return  self.name


class PaperBook(BaseBook):
     def __init__(self,name):
         super(PaperBook, self).__init__(name=name)

     def getBook(self):
         return self.name+ ' from paper'

def fun1(i:int)->int:
    print(i)

class Mythread(Thread):
    def run(self) -> None:
        print(Thread.getName(self))
        print('my thread start..')

def main():
    """the entrance of this file"""
    paperBook = PaperBook('hello')
    print(paperBook.getBook())
    mythread = Mythread()
    mythread.start()


if __name__ == '__main__':
    main()
