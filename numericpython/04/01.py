"""
Author:
Purpose:
Date：
"""

import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def fun1():
    # prepare data
    x = np.linspace(-5, 5, 100)
    y = x ** 3 + 5 * x ** 2 + 10
    z = 3 * x ** 2 + 10 * x + 0
    w = 6 * x + 10
    # create figure instance and axes instance
    fig, ax = plt.subplots()
    # draw
    ax.plot(x, y, color='red', label='y')
    ax.plot(x, z, color='green', label='z')
    ax.plot(x, w, color='blue', label='w')
    # configure
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-100, 500)
    ax.set_title('my god')
    ax.grid(linestyle=':', color='gray')
    ax.annotate('my', xy=(1, 10), xytext=(+2,+2),  textcoords="offset points", arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.9"))
    ax.legend(bbox_to_anchor=(1, 5))
    # show figure
    fig.show()
    print('hello')


def fun2():
    x = np.linspace(-2, 2, 1000)
    y = np.cos(40 * x)
    fig = plt.Figure(figsize=(8, 2.5), facecolor='#f1f1f1')
    ax = fig.add_axes((0.1, 0.1, 0.8, 0.8), facecolor='#e1e1e1')
    ax.plot(x, y)
    ax.text(2,1,'mytest')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    fig.savefig('1.pdf', dpi=100, facecolor='#f1f1f1')


def getSubplots():
    fig, ax = plt.subplots(nrows=2, ncols=1)
    return fig, ax


def main():
    x = np.linspace(-1, 1, 1000)
    y = np.cos(40 * x)
    # fig,ax = getSubplots()
    # ax[0][0].plot(x, y, color='red', marker='o')
    # fig.show()
    fun1()


if __name__ == '__main__':
    main()
