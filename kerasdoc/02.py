
import tensorflow as tf
from tensorflow import keras


class Linear(keras.layers.Layer):
    """y = w.x + b"""

    def __init__(self, units=32, input_dim=32):
        super(Linear, self).__init__()
        self.units = units
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(
            initial_value=w_init(shape=(input_dim, units), dtype="float32"),
            trainable=False,
        )
        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(units,), dtype="float32"), trainable=False
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b

class ActivityRegularization(keras.layers.Layer):
    """Layer that creates an activity sparsity regularization loss."""

    def __init__(self, rate=1e-2):
        super(ActivityRegularization, self).__init__()
        self.rate = rate

    def call(self, inputs):
        # We use `add_loss` to create a regularization loss
        # that depends on the inputs.
        self.add_loss(self.rate * tf.reduce_sum(inputs))
        return inputs

class SparseMLP(keras.layers.Layer):
    """Stack of Linear layers with a sparsity regularization loss."""

    def __init__(self):
        super(SparseMLP, self).__init__()
        self.linear_1 = Linear(32)
        self.regularization = ActivityRegularization(1e-2)
        self.linear_3 = Linear(10)

    def call(self, inputs):
        x = self.linear_1(inputs)
        x = tf.nn.relu(x)
        x = self.regularization(x)
        return self.linear_3(x)

def main():
    # Instantiate a metric object
    accuracy = tf.keras.metrics.SparseCategoricalAccuracy()
    (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
    dataset = tf.data.Dataset.from_tensor_slices(
        (x_train.reshape(60000, 784).astype("float32") / 255, y_train)
    )
    dataset = dataset.shuffle(buffer_size=1024).batch(64)

    # Prepare our layer, loss, and optimizer.
    model = keras.Sequential(
        [
            keras.layers.Dense(32, activation="relu"),
            keras.layers.Dense(32, activation="relu"),
            keras.layers.Dense(10),
        ]
    )
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)

    for epoch in range(2):
        # Iterate over the batches of a dataset.
        for step, (x, y) in enumerate(dataset):
            with tf.GradientTape() as tape:
                logits = model(x)
                # Compute the loss value for this batch.
                loss_value = loss_fn(y, logits)

            # Update the state of the `accuracy` metric.
            accuracy.update_state(y, logits)

            # Update the weights of the model to minimize the loss value.
            gradients = tape.gradient(loss_value, model.trainable_weights)
            optimizer.apply_gradients(zip(gradients, model.trainable_weights))

            # Logging the current accuracy value so far.
            if step % 200 == 0:
                print("Epoch:", epoch, "Step:", step)
                print("Total running accuracy so far: %.3f" % accuracy.result())

        # Reset the metric's state at the end of an epoch
        accuracy.reset_state()



if __name__ == '__main__':
    main()
