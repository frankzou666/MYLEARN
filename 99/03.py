# _*_coding:utf-8 _*_



import argparse
import os

import pandas
import pandas as pd

import pymysql
from sqlalchemy import create_engine

#Global variables
X_DIM = 5
EPOCHS = 256
TOTAL_TIMES = 3


MYSQL_DB_HOST = '192.168.1.146'
MYSQL_DB_PORT = 11337
MYSQL_DB_USER = 'dp'
MYSQL_DB_PWD = 'dp123456'
MYSQL_DB_NAME = 'dp'
class MySQLUtil():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def getDbConnection(self):
        """
        返回数据库连接
        :return:
        """
        if self.connection is None:
            self.connection = pymysql.connect(host=MYSQL_DB_HOST,
                                              port=MYSQL_DB_PORT,
                                              user=MYSQL_DB_USER,
                                              password=MYSQL_DB_PWD,
                                              database=MYSQL_DB_NAME,
                                              charset="utf8"
                                              )

        return self.connection

    def getCursor(self):
        if ((not hasattr(self, "connection")) or (self.connection is None)):
            self.getDbConnection()
        if ((not hasattr(self, "cursor")) or (self.cursor is None)):
            self.cursor = self.connection.cursor()

       # self.logger.info("mySQLUtils  ,操作 getCursor")
        return self.cursor

    def closeDbConnection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            #self.logger.info("mySQLUtils ,操作 closeDbConnection")

    def closeCursor(self):
        self.cursor.close()
        self.cursor = None
        #self.logger.info("mySQLUtils ,操作 closeCursor")
    def commit(self):
        if self.connection is not None:
            self.connection.commit()


def readCSV():
    data_file = os.path.join('data.csv')
    df = pd.read_csv(data_file)
    df['date'] = df['date'].astype('datetime64[ns]')
    df['sp'] = df['sp'].str.replace(',', '').astype('float')
    df['kp'] = df['kp'].str.replace(',', '').astype('float')
    df['high'] = df['high'].str.replace(',', '').astype('float')
    df['low'] = df['low'].str.replace(',', '').astype('float')
    df['total'] = df['total'].str.replace('K', 'e3')
    df['total'] = df['total'].str.replace('M', 'e6')
    df['total'] = df['total'].str.replace('B', 'e9')
    df['total'] = df['total'].apply(lambda x: eval(x))
    df['inc_dec'] = df['inc_dec'].str.replace('%', '')
    newpds = df.sort_values(by=['date'],ascending=True)
    return newpds

def readSQL():
    db_connection_str = 'mysql+pymysql://'+MYSQL_DB_USER+':'+MYSQL_DB_PWD+'@'+MYSQL_DB_HOST+':'+str(MYSQL_DB_PORT)+'/'+MYSQL_DB_NAME
    db_connection = create_engine(db_connection_str)

    sql_str = "select sp,kp,high,low ,total from t_d order by dt"
    df = pandas.read_sql(sql=sql_str,con=db_connection)
    return df



def main():

    mySQLUtil = MySQLUtil()


    df = readCSV()
    df_sql = readSQL()
    print(df_sql)

    print(df["high"].mean())
    print(df["high"].std())

    mySQLUtil.closeDbConnection()

if __name__ == "__main__":
    main()