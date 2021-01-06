import tensorflow as tf
from tensorflow.keras.models import Sequential # Modelo Sequencial
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard # Para visualização do Modelo da Rede Neural
from keras.layers import LeakyReLU
import pickle
import numpy as np

import datetime

date = datetime.datetime.now()
date = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute)

NAME = 'Rede_neural_treinada-cnn-{}'.format(date)

tensorboard = TensorBoard(log_dir = 'cnn/logs/{}'.format(NAME)) # Para ter uma visualização do treinamento da rede neural

pickle_in = open("cnn\\output\\X_training.pickle","rb")
X_training = np.array(pickle.load(pickle_in))

pickle_in = open("cnn\\output\\y_training.pickle","rb")
y_training = np.array(pickle.load(pickle_in))

pickle_in = open("cnn\\output\\X_test.pickle","rb")
X_test = np.array(pickle.load(pickle_in))

pickle_in = open("cnn\\output\\y_test.pickle","rb")
y_test = np.array(pickle.load(pickle_in))

X_training = np.array(X_training/255.0) # Simplificando coloração de Pixels para valores entre 0 e 1
X_test = np.array(X_test/255.0) # Simplificando coloração de Pixels para valores entre 0 e 1

model = Sequential()
model.add(Conv2D(filters = 32, kernel_size = (3,3), padding = 'same', input_shape = (64, 64, 3))))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(filters = 32, kernel_size = (3,3)))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(filters = 64, kernel_size = (3,3)))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(classes, activation = 'softmax'))

model.compile(optimizer=SGD(0.01), loss="categorical_crossentropy",metrics=["accuracy"])

# model.summary()
# adam = tf.keras.optimizers.Adam(learning_rate=0.001)
# model.compile(optimizer= adam, loss='SparseCategoricalCrossentropy', metrics=['acc'])
model.fit(X_training, y_training, batch_size=32, epochs=1, validation_split=0.1, callbacks = [tensorboard], validation_data=(X_test, y_test))

model.save('cnn\\output\\treinando_rede_all.model') # Salvando Rede Neural