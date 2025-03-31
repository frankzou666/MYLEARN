


import argparse
import os
import pandas as pd

from keras.models import  Sequential
from keras.layers import Dense
import numpy as np
import datetime
from sqlalchemy import create_engine
from concurrent.futures  import  ThreadPoolExecutor,wait
import pymysql
import threading


#Global variables
X_DIM = 5
EPOCHS = 512
TOTAL_TIMES = 100

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

def readSQL(ct):
    db_connection_str = 'mysql+pymysql://'+MYSQL_DB_USER+':'+MYSQL_DB_PWD+'@'+MYSQL_DB_HOST+':'+str(MYSQL_DB_PORT)+'/'+MYSQL_DB_NAME
    db_connection = create_engine(db_connection_str)
    sql_str = "select dt,sp,kp,high,low ,total from t_d where ct='"+ct+"' order by dt"

    df = pd.read_sql(sql=sql_str,con=db_connection)
    df['dt'] = df['dt'].astype('datetime64[ns]')
    df['sp'] = df['sp'].str.replace(',', '').astype('float')
    df['kp'] = df['kp'].str.replace(',', '').astype('float')
    df['high'] = df['high'].str.replace(',', '').astype('float')
    df['low'] = df['low'].str.replace(',', '').astype('float')
    df['total'] = df['total'].str.replace('K', 'e3')
    df['total'] = df['total'].str.replace('M', 'e6')
    df['total'] = df['total'].str.replace('B', 'e9')
    df['total'] = df['total'].apply(lambda x: eval(x))
    return df
def stdPd(df):
    #df['sp'] = (df['sp']-df['sp'].min()) / (df['sp'].max()-df['sp'].min())
    #df['kp'] = (df['kp'] - df['kp'].min()) / (df['kp'].max() - df['kp'].min())
    #df['high'] = (df['high'] - df['high'].min()) / (df['high'].max() - df['high'].min())
    #df['low'] = (df['low'] - df['low'].min()) / (df['low'].max() - df['low'].min())
    #df['total'] = (df['total'] - df['total'].min()) / (df['total'].max() - df['total'].min())
    df['sp'] = (df['sp'] - df['sp'].mean()) / (df['sp'].std())
    df['kp'] = (df['kp'] - df['kp'].mean()) / (df['kp'].std())
    df['high'] = (df['high'] - df['high'].mean()) / (df['high'].std())
    df['low'] = (df['low'] - df['low'].mean()) / (df['low'].std())
    df['total'] = (df['total'] - df['total'].mean()) / (df['total'].std())
    return  df


def getModel(X_DIM):
    model = Sequential()
    model.add(Dense(units=X_DIM * 4, kernel_initializer='normal', activation='relu',input_shape=(X_DIM,)))
    model.add(Dense(units=X_DIM * 2, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=4,kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=1,kernel_initializer='normal', activation='linear'))
    model.compile(optimizer='adam',loss='mean_absolute_error',metrics=['mean_absolute_error'])
    return  model

def getNormal(data,data_mean,data_std):
     #x = (data - data_min) / (data_max - data_min)
     x = (data - data_mean) / data_std
     return  x


def getOrgin(data,data_mean,data_std):
     #x = data *(data_max-data_min) +data_min
     x =( data* data_std ) + data_mean
     return  x


def fitModel(model,x,y ):
    model.fit(x=x, y=y, epochs=EPOCHS, batch_size=64, validation_split=0.3, verbose=0)
    return  model

def prediteFromModel(model,x_predict,data_mean,data_std):

    x_predict = np.asarray(x_predict).reshape(1, X_DIM)
    result = getOrgin(model.predict(x=x_predict, verbose=0), data_mean=data_mean, data_std=data_std)
    return result[0][0]


def getDFColumnMaxAndMin(df,column):
    #df_max = df[column].max()
    #df_min = df[column].min()
    data_mean = df[column].mean()
    data_std = df[column].std()
    return  data_mean,data_std


def getTrainData(df_normal,column):
    df_train = []
    df_label = []
    # get train data
    for item in df_normal[column].rolling(window=X_DIM):
        if len(item.to_list()) == X_DIM:
            df_train.append(item.to_list())
    # get label data
    for i in range(1, len(df_train)):
        df_label.append(df_train[i][0])

    # translate to numpy
    df_of_train_numpy = np.array(df_train[0:len(df_train) - 1])
    df_of_label_numpy = np.array(df_label).reshape(len(df_train) - 1, 1)

    return df_of_train_numpy,df_of_label_numpy


def getResultMap(data_dist,column):
    result_map = {}
    data_dist_sort_by_value = {k: v for k, v in sorted(data_dist.items(), key=lambda item: item[1])}
    data_dist_sort_by_value_top = list(data_dist_sort_by_value.keys())[-1]
    data_dist_sort_by_value_top = int(str(data_dist_sort_by_value_top) + "500")
    data_dist_sort_by_value_top_up = data_dist_sort_by_value_top * 1.01
    data_dist_sort_by_value_top_down = data_dist_sort_by_value_top * 0.995

    result_map["type"] = column
    result_map["in"] = data_dist_sort_by_value_top
    result_map["up"] = data_dist_sort_by_value_top_up
    result_map["down"] = data_dist_sort_by_value_top_down
    result_map["data"] = data_dist

    return  result_map


def saveResultToDb(resultMap,ct):

    mySQLUtil =  MySQLUtil()
    cursor = mySQLUtil.getCursor()
    sql_str = "insert into t_r(ct,type_n,in_r,up_r,down_r,data_str,createtime) values('{}','{}','{}','{}','{}','{}',now())".format(
                                                          ct,
                                                                resultMap["type"],
                                                                resultMap["in"],
                                                                resultMap["up"],
                                                                resultMap["down"],
                                                                resultMap["data"].__str__().replace("'",'')
                                                                )


    cursor.execute(sql_str)
    mySQLUtil.commit()

def getPreictDataDist(model,columns,column,df_normal,df_of_train_numpy,df_of_label_numpy,data_mean,data_std,ct):
    data_dist = {}
    for i in range(TOTAL_TIMES):
        print("CT:{},类型:{},时间:{},总次数:{},正动运行: {}".format(ct,
                                                              column,
                                                              datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                              TOTAL_TIMES, i + 1))
        model = fitModel(model=model, x=df_of_train_numpy, y=df_of_label_numpy)
        x_predict = df_normal[column].tail(X_DIM - 1).to_list()
        x_predict.append(getNormal(data=columns[column], data_mean=data_mean, data_std=data_std))
        result = prediteFromModel(model=model, x_predict=x_predict, data_mean=data_mean, data_std=data_std)
        sub_str = str(result)[0:2]
        if data_dist.get(sub_str):
            data_dist[sub_str] = data_dist[sub_str] + 1
        else:
            data_dist[sub_str] = 1
    resultMap = getResultMap(data_dist=data_dist,column=column)
    saveResultToDb(resultMap=resultMap,ct=ct)
    return resultMap

def main():


    cts = ['B']
    #columns = {'kp':64992,'sp':61668.57,'high':65114,'low':61440.0}
    columns = {'kp': 69428, 'sp': 68638, 'high': 69560, 'low': 67496.0}
    columns_result = []
    all_tasks = []
    with ThreadPoolExecutor(8) as executor:
          for ct in cts:
              df = readSQL(ct=ct)
              df_2 = readSQL(ct = ct)
              for column in columns.keys():
                  data_mean, data_std = getDFColumnMaxAndMin(df=df_2, column=column)
                  df_normal = stdPd(df=df)
                  df_of_train_numpy, df_of_label_numpy = getTrainData(df_normal=df_normal, column=column)
                  # get model
                  model = getModel(X_DIM=X_DIM)

                  all_tasks.append(executor.submit(getPreictDataDist,
                                                   model=model,
                                                   columns=columns,
                                                   column=column,
                                                   df_normal=df_normal,
                                                   df_of_train_numpy=df_of_train_numpy,
                                                   df_of_label_numpy=df_of_label_numpy,
                                                   data_mean=data_mean,
                                                   data_std=data_std,
                                                   ct=ct
                                                   ))



           #columns_result.append(getResultMap(data_dist=data_dist,column=column))

          wait(all_tasks,return_when="ALL_COMPLETED")
          for i in all_tasks:
             print(i.result())



    #output
    # for item in columns_result:
    #    print(item)



if __name__ == "__main__":
    main()
