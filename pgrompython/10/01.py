
"""
Author:
Purpose:
Date：
"""


import argparse
from tkinter import *
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def myLabel(root):
    label = Label(root,text='hello')
    label.pack(side=LEFT,fill=BOTH,expand=YES)
    return  label


def main():
    app = Tk()
    label=myLabel(app)
    mainloop()

if __name__ == '__main__':
    main()