

class C1():
    pass
class C2():
    def displayname(self):
        print('this is C2')

class C3(C1,C2):
    def __init__(self,name):
        self.name=name

    def displayname(self):
        print(self.name)
    def __X__(self):
        print('this is X')

def main():
    c3 =C3('devid')
    c3.displayname()


if __name__ == '__main__':
    main()