
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

    def getPay(self,pay):
        return pay*1.10
    # python will call pay*1.5
    def getPay(self,pay,type=None):
        return pay*1.5


class Manager(Person):



    def __init__(self ,name ,job=None ,pay=0):
        Person.__init__(self,name,'mgr')
        #super().__init__(self,name,'mgr')
    def getLastName(self):
        return self.name.split(' ')[0]

def main():
    p1 = Person('smith bob')
    m1 = Manager('devid john')
    print(p1.name)
    print(m1.getPay(pay=10))
    print(m1.getLastName())



if __name__ == '__main__':
    main()
