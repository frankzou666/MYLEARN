
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

class Student():
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = 'you are' + name


def main():
    student = Student()
    student.name ='frank'
    print(student.name)

if __name__ == '__main__':
    main()