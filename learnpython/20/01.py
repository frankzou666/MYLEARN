

from threading import Thread
from time import sleep
import datetime
import time
def f(x):
    sleep(2)
    print(x*10)

def main():
    starttime = datetime.datetime.now()
    l = []
    for i in range(10):
        t = Thread(target=f,args=(10,))
        t.start()

    for t in l:
        t.join()
    print(datetime.datetime.now()-starttime)




if __name__ == '__main__':
    main()
    time.t
    print('main exit')