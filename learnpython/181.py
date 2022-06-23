from threading import Thread


def listAdd(arg1,*other,arg2='a'):
    print(arg1)
    print(arg2)
    for i in other:
        print('from other')
        print(i)


def testThread(t):
     print(t)

def main():
    arr=['a','b','c']
    list(map(testThread,arr))



if __name__ == '__main__':
    main()