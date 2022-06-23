"""
Author:
Purpose:
Date：
"""

import argparse
import pandas
import sqlite3

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()




def main():
    """the entrance of this file"""
    query = 'create table t1(a integer)'
    con = sqlite3.connect(':memory:')
    con.execute(query)
    con.execute('insert into t1 values(10)')
    con.execute('insert into t1 values(20)')
    for item in con.execute('select * from t1'):
        print(item)
    pd=pandas.read_sql('select * from t1',con)
    print(pd)

if __name__ == '__main__':
    main()
