
import numpy as np
import matplotlib.pyplot as plt


def main():
    n1= np.linspace(0,50,500)
    n2= np.zeros(n1.shape)+2
    plt.plot(n1,n2)
    plt.show()



if __name__ == '__main__':
    main()