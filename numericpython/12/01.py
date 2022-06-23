"""
Author:
Purpose:
Date：
"""

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import matplotlib as mpl


mpl.style.use('ggplot')

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def seriesTest():
    data = [1, 3, 5, 2, 10, 2]
    pd1 = pd.Series(data)
    pd1.index = ['A', 'B', 'C', 'E', 'F', 'H']
    fig, axes = plt.subplots(1, 4, figsize=(50, 50))
    pd1.plot(ax=axes[0], kind='line', title='line')
    pd1.plot(ax=axes[1], kind='bar', title='bar')
    pd1.plot(ax=axes[2], kind='pie', title='pie')
    plt.show()



def dataFrameTest():
    data = [[1,'A'], [3,'D'], [5,'E'], [6,'E'],[4,'H']]
    df = pd.DataFrame(data)
    df.columns = ['ID','LEVEL']
    print(df.LEVEL.value_counts())



def main():
    """the entrance of this file"""
    dataFrameTest()



if __name__ == '__main__':
    main()
