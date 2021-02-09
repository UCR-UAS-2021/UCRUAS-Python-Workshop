import tensorflow.keras as keras
import tensorflow as tf
import cv2
import numpy as np

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = keras.models.load_model("models/number_reader.model")

predictions = model.predict(x_test)

index = 20

cv2.imshow('first number', cv2.resize(x_test[index], (x_test[index].shape[1] * 10, \
    x_train[index].shape[0] * 10)))
print(np.argmax(predictions[index]))
cv2.waitKey()
cv2.destroyAllWindows()