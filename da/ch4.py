
import numpy as np



def main():
    dataset=[[0,3,4,8],
             [5,3,4,9]]
    arr = np.array(dataset)
    print(arr)
    print(arr.T)
    #求矩阵内积
    print(np.dot(arr.T,arr))



if __name__ == '__main__':
    main()