"""
Author:
Purpose:
Date：
"""

import argparse
import random
import numpy as np
from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
import time
import tqdm
import matplotlib.pyplot   as plt

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


@dataclass()
class StockPrice:
    symbol: str
    closedate : datetime

def testnametuples():
    """

    :return:
    """
    nt = namedtuple('Price', ['name', 'date'])
    qq = nt('AAPL', '2022')
    print(qq.name)



def testTqdm():
    """

    :return:
    """
    _ = [random.random() for _ in range(1000000)]
    for i in tqdm.tqdm(range(1)):
        time.sleep(10)
        _ = [random.random() for _ in range(1000000)]




def main():
    """the entrance of this file"""
    x = np.linspace(2,8,100)
    y = x*(10-x)
    plt.plot(x, y)
    plt.show()



if __name__ == '__main__':
    main()
