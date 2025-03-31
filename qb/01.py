import math

import numpy as np
def main():
    cnt = 0
    for i in range(0,1000):
        for j in range(1,100):
            m = i / 1000
            n = j / 100
            k = m/n
            if k<1:
                q=float(str(k)[0:5])*100
                if (q%10==0):
                    print("i:" + str(i) + " ,j:" + str(j) + ",k:" + str(k))
                    cnt = cnt +1
    #计算概率
    print('result:'+ str(round(cnt/(1000*100)*100,3)))

if __name__=='__main__':
    main()

