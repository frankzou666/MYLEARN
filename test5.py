import pandas as pd
import numpy as np
import sqlite3
import pandas.io.sql as sql
import matplotlib.pyplot as plt
import math

def f1():
    replacevalue={'M':['BBB']}
    dataframe = pd.read_csv('c://temp//1.txt',names=['I','J','K','M'],na_values=replacevalue)
    print(pd.HDFStore(dataframe,'c://temp//2.txt'))
    print(dataframe.sum(axis=1))

def f2():
    query ='create table t1(a integer)'
    con = sqlite3.connect('c://temp//sql.dat')
    #con.execute(query)
    con.execute('insert into t1 values (10)')
    rows = con.execute('select * from t1')
    a=sql.read_sql('select * from t1',con)
    print(a)

def f3():
     df1 = pd.DataFrame({'ke1':['a','b','c'],'data':[3,3,9]})
     df2 = pd.DataFrame({'ke1': ['a', 'b', 'c'], 'data1': ['I', 'M', 'J']})
     print(df1)
     print(df2)
     print(pd.merge(df1,df2))

def f4():
    np1 = pd.Series({'name':range(5)})
    np2 =  pd.Series({'key':range(5)})
    print(np1)
    print(pd.concat([np1,np2]))



def distance(x,y):
    return abs(x-y)

def sumofdistance(r1,r2):
    sum = 0
    for i in range(1, len(r1)):
        sum = sum + distance(r2[i - 1], r2[i])
    return  sum

def main():
    n1 = np.array([1,2,3,4,5])
    n2 = np.array([3,3,3,3,3])
    n3 = np.array([0,6,3,4,2])
    n4 = np.array([3,4,2,5,1])

    print(n4.sum())
    sum = sumofdistance(n1,n2)
    print('n2 distinance :{sum}'.format(sum=sum))

    sum = sumofdistance(n1, n3)
    print('n3 distinance :{sum}'.format(sum=sum))

    sum = sumofdistance(n1, n4)
    print('n4 distinance :{sum}'.format(sum=sum))

    plt.plot(n1, n2)
    plt.plot(n1, n3)
    plt.plot(n1, n4)
    plt.show()

if __name__ == '__main__':
    main()