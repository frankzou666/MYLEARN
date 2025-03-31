
from concurrent.futures  import  ThreadPoolExecutor
import threading

def sayHello(i,j):
    print(i+j)
    print(threading.currentThread().getName())
def main():
    with ThreadPoolExecutor(5) as executor:
        for i in range(10):
            executor.submit(sayHello,i=i,j=i)

if __name__ == '__main__':
    main()