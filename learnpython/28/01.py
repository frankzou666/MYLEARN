
class Person():
    classname = 'Class name is Person'
    def __init__(self ,name ,job=None ,pay=0):
        self.job = job
        self.name = name
        self.pay = pay
    def getLastName(self):
        return  self.name.split(' ')[-1]
    def __str__(self):
        return 'default string name: ' +self.name

class Manager( Person ):
    def __init__(self ,name ,job=None ,pay=0):
        Person.__init__(self,name,'mgr')
        #super().__init__(self,name,'mgr')
    def getLastName(self):
        return self.name.split(' ')[-1]

def main():
    p1 = Person('smith bob')
    m1 = Manager('devid john')
    print(p1.name)
    print(p1)
    print(m1.name)
    print(m1.job)
    print(Person.classname)


if __name__ == '__main__':
    main()
