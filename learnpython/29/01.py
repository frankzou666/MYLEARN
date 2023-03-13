

from abc import abstractmethod,ABCMeta


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
    """

    """
    # how to call superclass constuctor
    def __init__(self ,name ,job=None ,pay=0):
        Person.__init__(self,name,'mgr')
    def getLastName(self):
        return self.name.split(' ')[-1]

class Super(metaclass = ABCMeta):
    @abstractmethod
    def action(self):
        pass

class Sub(Super):
    pass

def main():
    a = Person("test")
    Person.classname="bbb"
    b = Person("testb")
    print(b.classname)


if __name__ == '__main__':
    main()
