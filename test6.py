
import  librosa
import python_speech_features
from scipy.signal.windows import hann, hamming
import numpy as np
import pandas as pd
import  matplotlib.pyplot as  plt
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV


import os
import tarfile
import urllib.request

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("c://1/", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_data_csv(housing_path=HOUSING_PATH):
    csvpath=os.path.join(housing_path,'housing.csv')
    return pd.read_csv(csvpath)

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_bound=int(len(data)*test_ratio)
    test_data=shuffled_indices[0:test_bound]
    train_data=shuffled_indices[test_bound:]
    return  data.iloc[train_data],data.iloc[test_data]

def main():
    #fetch_housing_data()
    housing_data=load_data_csv()
    train_data,test_data =split_train_test(housing_data,0.2)
    housing_train_label = train_data['median_house_value'].copy()
    housing_train_data = train_data.drop('median_house_value',axis=1)
    mean_total_bed_room=housing_train_data["total_bedrooms"].mean()
    housing_train_data["total_bedrooms"].fillna(mean_total_bed_room,inplace=True)
    housing_cat = housing_data[["ocean_proximity"]]
    one_hot_encoder = OneHotEncoder()
    housing_cat_encoded = one_hot_encoder.fit_transform(housing_cat)
    print(housing_cat_encoded.toarray())

if __name__ == '__main__':
    main()