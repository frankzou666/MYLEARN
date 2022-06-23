



"""
Author:
Purpose:
Date：
"""


import argparse
from tkinter import *
import sys
from tkinter.messagebox import  *
from tkinter.filedialog import askopenfilename # get standard dialogs
from tkinter.colorchooser import askcolor # they live in Lib\tkinter
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def callback():
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')




class Demo(Frame):


    def __init__(self, parent=None, **options):
        demos = {
            'Open': askopenfilename,
            'Color': askcolor,
            'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
            'Error': lambda: showerror('Error!', "He's dead, Jim"),
            'Input': lambda: askfloat('Entry', 'Enter credit card number')
        }
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Basic demos").pack()
        for (key, value) in demos.items():
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)


def setBgColor(obj):
        (triple, hexstr) = askcolor()
        if hexstr:
            obj.config(bg=hexstr)


def main():
    class Demo(Frame):
        def __init__(self, parent=None, **options):

            Frame.__init__(self, parent, **options)

    self.pack()
    Label(self, text="Scale demos").pack()
    self.var = IntVar()
    Scale(self, label='Pick demo number',
          command=self.onMove,  # catch moves
          variable=self.var,  # reflects position
          from_=0, to=len(demos) - 1).pack()
    Scale(self, label='Pick demo number',
          command=self.onMove,  # catch moves
          variable=self.var,  # reflects position
          from_=0, to=len(demos) - 1,
          length=200, tickinterval=1,
          showvalue=YES, orient='horizontal').pack()
    Quitter(self).pack(side=RIGHT)
    Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
    Button(self, text="State", command=self.report).pack(side=RIGHT)

    def onMove(self, value):
        print('in onMove', value)

    def onRun(self):
        pos = self.var.get()

    print('You picked', pos)
    demo = list(demos.values())[pos]  # map from position to value (3.X view)
    print(demo())  # or demos[ list(demos.keys())[pos] ]()

    def report(self):
        print(self.var.get())

    if __name__ == '__main__':
        print(list(demos.keys()))
    Demo().mainloop()
if __name__ == '__main__':
    main()



