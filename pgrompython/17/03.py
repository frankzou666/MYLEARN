
"""
Author:
Purpose:
Date：
"""


import argparse
import shelve
import sqlite3
import random

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


class Person:
   def __init__(self, name, job, pay=0):
       self.name = name
       self.job = job
       self.pay = pay # real instance data
   def tax(self):
       return self.pay * 0.25 # computed on call
   def info(self):
       return self.name, self.job, self.pay, self.tax()


def main3():
    p1 = Person(name='frank',job='dba',pay=10)
    p2 = Person(name='smith', job='dba', pay=10)
    file = shelve.open('b')
    for p in (p1,p2):
        file[p.name] = p
    file.close()

def main2():
    file = shelve.open('b')
    for k in file.keys():
        print(file[k].info())


def main4():
    db = sqlite3.connect('sqllit.db')
    db.execute('create table t2(a int,b int)')


def insertRecord():
    for _ in range(10):
        db = sqlite3.connect('sqllit.db')
        db.execute('insert into t2 values(?,?)',((random.randint(1,100),random.randint(1,100))))
        db.commit()
        db.close()


def delRecord():
    db = sqlite3.connect('sqllit.db')
    db.execute('delete from t2')
    db.commit()
    db.close()


def main():
    result = []
    db = sqlite3.connect('sqllit.db')
    cursor = db.execute('select * from t2')
    desc = [desc[0] for desc in cursor.description]

    for row in cursor.fetchall():
        newdict = {}
        for (name,val) in zip(desc,row):
            newdict[name] = val
        result.append(newdict)

    db.close()
    print(result)

if __name__ == '__main__':
    delRecord()
    insertRecord()
    main()