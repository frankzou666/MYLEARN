
import tensorflow as tf


BATCH_SIZE = 32
NUM_EPOCHS= 20
IMG_H = IMG_W = 224
IMG_SIZE = 224
LOG_DIR = './log'
SHUFFLE_BUFFER_SIZE = 1024
IMG_CHANNELS = 3


def create_model():
    model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu',
    input_shape=(IMG_SIZE, IMG_SIZE, IMG_CHANNELS)),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(rate=0.3),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(rate=0.3),
    tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
    ])
    return model


def scratch(train, val, learning_rate):
    model = create_model()
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy'])
    earlystop_callback = tf.keras.callbacks.EarlyStopping(
        monitor='val_accuracy',
        min_delta=0.0001,
        patience=5)
    model.fit(train,
              epochs=NUM_EPOCHS,
              steps_per_epoch=int(NUM_EXAMPLES / BATCH_SIZE),
              validation_data=val,
              validation_steps=1,
              validation_freq=1,
              callbacks=[ earlystop_callback])
    return model


def main():
    pass


if __name__ == '__main__':
    main()