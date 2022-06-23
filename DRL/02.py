
import math
import matplotlib.pyplot as plt


def main():
    x = [x for x in range(1,1000)]
    y = [math.sin(1/x) for x in range(1,1000)]
    plt.plot(x,y,'r')
    print(x)
    print(y)
    plt.show()


if __name__ == '__main__':
    main()
