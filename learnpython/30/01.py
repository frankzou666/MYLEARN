class Fater():
    def __init__(self,__str):
        self.__str = __str
        print('call __init__...')
    def __del__(self):
        print('del object')




def main():
    fater = Fater('hello')
    fater.name1=150
    print(fater._fater__str)


if __name__ == '__main__':
    main()
