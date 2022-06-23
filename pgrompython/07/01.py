
"""
Author:
Purpose:
Date：
"""


import argparse
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



class MyQuit():
    def __init__(self):
        print('object be created...')

    def __call__(self, *args, **kwargs):
        print('object be call...')
        sys.exit()


def hello(event):
     print('hello world')

def quit(event):
    print('exit')
    sys.exit()

def greeting():
    print('Hello stdout world!...')

def main():
    win = tk.Frame()
    win.pack()
    tk.Label(win, text='Hello container world').pack(side=tk.TOP)
    tk.Button(win, text='Hello', command=greeting).pack(side=tk.LEFT)
    tk.Button(win, text='Quit', command=win.quit).pack(side=tk.RIGHT)
    win.mainloop()

if __name__ == '__main__':
    main()

