import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def main():
    x_label0 = np.random.normal(5, 1, 10)
    x_label1 = np.random.normal(2, 1, 10)
    learning_rate = 0.001;    DTYPE = tf.float32
    training_epochs = 1000;momentum = 0.0
    xs = np.append(x_label0, x_label1)
    labels = [0.] * len(x_label0) + [1.] * len(x_label1)
    plt.scatter(xs, labels)
    X = tf.constant(xs, dtype=DTYPE)
    Y = tf.constant(labels, dtype=DTYPE)
    @tf.function
    def model(X, w):
        return tf.add(
           tf.multiply(w[1], tf.pow(X, 1)),
           tf.multiply(w[0], tf.pow(X, 0))
        )
    w = tf.Variable([0., 0.], dtype=DTYPE, name='parameters')
    y_model = lambda: model(X, w)
    cost = lambda: tf.reduce_sum(tf.square(Y - y_model()))
    train_op = tf.keras.optimizers.SGD(learning_rate=learning_rate,momentum=momentum)
    for epoch in range(training_epochs):
        train_op.minimize(cost, w)
    w_val = w.numpy()
    all_xs = np.linspace(0, 10, 100)
    plt.plot(all_xs, all_xs * w_val[1] + w_val[0])
    plt.show()





if __name__ == '__main__':
    main()