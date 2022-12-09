"""
Author:
Purpose:
Date："""
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


class FirstClass:
    def setdata(self, value):
        self.value = value

    def displaydata(self):
        return self.value


class SecondClass(FirstClass):
    def displaydata(self):
        print('from second')




def main():
    """the entrance of this file"""
    x = FirstClass()
    y = FirstClass()
    z = SecondClass()
    z.displaydata()



if __name__ == '__main__':
    main()
