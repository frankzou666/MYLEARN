
import matplotlib.pyplot as plt
import numpy as np
from pandas import *


def main2():
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax1.plot([1,2],[2,3],linestyle='--',color='g')
    ax1.set_title('ax1')
    ax2 = fig.add_subplot(2,2,2)
    ax2.plot(np.random.randn(10).cumsum(), np.random.randn(10).cumsum(),color='r',marker='o',label='ax2label')
    ax2.set_title('ax2')
    ax2.set_xlabel('ax2xlabel')
    ax2.set_ylabel('ax2ylabel')
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.scatter(np.random.randn(10).cumsum(), np.arange(0, 100, 10), color='r', marker='o')
    ax3.set_title('ax3')

    plt.show()
    plt.legend()


def main3():
    df =  DataFrame(abs(np.random.randn(10,4)).cumsum(0),
                     columns=['A','B','C','D'],
                     index=np.arange(0, 100, 10))
    df.plot(kind='bar')
    plt.show()



def main():
    df =  DataFrame({'key1':(np.random.randn(5,1).cumsum()),
                     'key2': ['a','b','a','c','b']
                    })

    grouped = df['key1'].groupby(df['key2'])


if __name__ == '__main__':
    main()
