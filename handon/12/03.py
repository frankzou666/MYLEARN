"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
import argparse
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def huber_fn(y_true, y_pred):
    """

    :param y_true:
    :param y_pred:
    :return:
    """
    error = y_true - y_pred
    is_small_error = tf.abs(error) < 1
    square_error = tf.square(error) / 2
    linear_error = tf.abs(error) - 0.5
    return tf.where(is_small_error, square_error, linear_error)


def my_softplus(z):  # return value is just tf.nn.softplus(z)
    return tf.sigmoid(z)

def my_glorot_initializer(shape, dtype=tf.float32):
    stddev = tf.sqrt(2. / (shape[0] + shape[1]))
    return tf.random.normal(shape, stddev=stddev, dtype=dtype)


def my_l1_regularizer(weights):
    return tf.reduce_sum(tf.abs(0.01 * weights))

def create_huber(threshold=1.0):
    def huber_fn(y_true, y_pred):
        error = y_true - y_pred
        is_small_error = tf.abs(error) < threshold
        squared_loss = tf.square(error) / 2
        linear_loss  = threshold * tf.abs(error) - threshold**2 / 2
        return tf.where(is_small_error, squared_loss, linear_loss)
    return huber_fn


class MyL1Regularizer(keras.regularizers.Regularizer):
    """
      we should implements __call__() and get_config()
    """
    def __init__(self,  config):
        self.config = config

    def __call__(self, weights):
        return tf.reduce_sum(tf.abs(self.config * weights))

    def get_config(self):
        return {'config': self.config}

class HuberMetric(keras.metrics.Metric):
    """

    """
    def __init__(self, threshold=1.0, **kwargs):
        super().__init__(**kwargs) # handles base args (e.g., dtype)
        self.threshold = threshold
        self.huber_fn = create_huber(threshold)
        self.total = self.add_weight("total", initializer="zeros")
        self.count = self.add_weight("count", initializer="zeros")
    def update_state(self, y_true, y_pred, sample_weight=None):
        metric = self.huber_fn(y_true, y_pred)
        self.total.assign_add(tf.reduce_sum(metric))
        self.count.assign_add(tf.cast(tf.size(y_true), tf.float32))
    def result(self):
        return self.total / self.count
    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "threshold": self.threshold}


class MyDense(keras.layers.Layer):
    def __init__(self, units, activation=None, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.activation = keras.activations.get(activation)

    def build(self, batch_input_shape):
        self.kernel = self.add_weight(
            name="kernel", shape=[batch_input_shape[-1], self.units],
            initializer="glorot_normal")
        self.bias = self.add_weight(
            name="bias", shape=[self.units], initializer="zeros")
        super().build(batch_input_shape) # must be at the end

    def call(self, X):
        return self.activation(X @ self.kernel + self.bias)

    def compute_output_shape(self, batch_input_shape):
        return tf.TensorShape(batch_input_shape.as_list()[:-1] + [self.units])

    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "units": self.units,
                "activation": keras.activations.serialize(self.activation)}


class MyModel(keras.Model):
    def __init__(self,output_dim, **kwargs):
        super(MyModel, self).__init__(**kwargs)
        self.hiden1 = keras.layers.Dense(30, activation='relu')
        self.out= keras.layer.Dense(output_dim)

    def call(self,inputs):
        pass

def main():
    """the entrance of this file"""
    housing = fetch_california_housing()
    X_train_full, X_test, y_train_full, y_test = train_test_split(
        housing.data, housing.target.reshape(-1, 1), random_state=42)
    X_train, X_valid, y_train, y_valid = train_test_split(
        X_train_full, y_train_full, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_valid_scaled = scaler.transform(X_valid)
    X_test_scaled = scaler.transform(X_test)

    input_shape = X_train.shape[1:]
    model = keras.models.Sequential([
        keras.layers.Dense(30, activation=my_softplus, input_shape=input_shape),
        keras.layers.Lambda(lambda x:tf.exp(x)),
        MyDense(30, activation='relu'),
        keras.layers.Dense(1),
    ])
    model.compile(loss='mse', optimizer="nadam", metrics=[create_huber(3.0)])
    model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))


if __name__ == '__main__':
    main()
