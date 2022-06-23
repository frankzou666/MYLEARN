
"""
Author:
Purpose:
Date：
"""


import argparse
from tkinter import *
import tkinter as tk
import sys

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def hello(win):
    msg=Message(win,text='hello')
    msg.pack()


def main():
    colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']
    r = 0
    for c in colors:
        Label(text=c, relief=RIDGE, width=25).grid(row=r, column=0)
        Entry(bg=c, relief=SUNKEN, width=50).grid(row=r, column=1)
        r += 1
    mainloop()

if __name__ == '__main__':
    main()