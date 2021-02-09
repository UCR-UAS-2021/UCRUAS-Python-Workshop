import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import cv2

# mnist is a huge dataset of handwritten numbers
mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

cv2.imshow('first number', cv2.resize(x_train[0], (x_train[0].shape[1] * 10, \
    x_train[1].shape[0] * 10)))
print(y_train[0])
cv2.waitKey()
cv2.destroyAllWindows()

x_train = keras.utils.normalize(x_train, axis=1).reshape(x_train.shape[0], -1)
x_test = keras.utils.normalize(x_test, axis=1).reshape(x_test.shape[0], -1)

# sequential model
model = keras.models.Sequential()
# Flattens image
model.add(keras.layers.Flatten())

model.add(keras.layers.Dense(128, activation=tf.nn.relu))

model.add(keras.layers.Dense(128, activation=tf.nn.relu))

model.add(keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)

print("loss: ", val_loss)
print("accuracy: ", val_acc)

model.save("models/number_reader.model")