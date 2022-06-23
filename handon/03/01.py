
import sklearn
import numpy as np
from sklearn.datasets import  fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score,cross_val_predict
from sklearn.metrics import confusion_matrix,precision_score
import matplotlib.pyplot as plt

def load_data():
    mnist = fetch_openml('mnist_784', version=1,as_frame=False)
    X, y = mnist["data"], mnist["target"]
    return  X,y

def main():
    X,y =load_data()

    y = y.astype(np.uint8)
    X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
    some_digit = X[0]
    some_digit_image = some_digit.reshape(28, 28)
    y_train_5 = (y_train == 5)
    y_test_5 = (y_test == 5)
    sgdclf = SGDClassifier(random_state=4)
    sgdclf.fit(X_train,y_train_5)

   




if __name__ == '__main__':
    main()