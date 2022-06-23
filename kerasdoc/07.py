
"""
Author:
Purpose:
Date：
"""


import argparse
import tensorflow as tf
from tensorflow import keras
import numpy as np

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

loss_tracker = keras.metrics.Mean(name="loss")
mae_metric = keras.metrics.MeanAbsoluteError(name="mae")


class CustomModel(keras.Model):
    def train_step(self, data):
        x, y = data

        with tf.GradientTape() as tape:
            y_pred = self(x, training=True)  # Forward pass
            # Compute our own loss
            loss = keras.losses.mean_squared_error(y, y_pred)

        # Compute gradients
        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)

        # Update weights
        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        # Compute our own metrics
        loss_tracker.update_state(loss)
        mae_metric.update_state(y, y_pred)
        return {"loss": loss_tracker.result(), "mae": mae_metric.result()}

    @property
    def metrics(self):
        # We list our `Metric` objects here so that `reset_states()` can be
        # called automatically at the start of each epoch
        # or at the start of `evaluate()`.
        # If you don't implement this property, you have to call
        # `reset_states()` yourself at the time of your choosing.
        return [loss_tracker, mae_metric]



def main():
    inputs1 = keras.Input(shape=(32,))
    inputs2 = keras.layers.Dense(32)(inputs1)
    outputs = keras.layers.Dense(1)(inputs2)
    model = CustomModel(inputs1, outputs)
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    x = np.random.random((1000, 32))
    y = np.random.random((1000, 1))
    sw = np.random.random((1000, 1))
    model.fit(x, y, epochs=3)

if __name__ == '__main__':
    main()