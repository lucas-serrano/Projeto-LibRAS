import cv2
import tensorflow as tf

import numpy as np

CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","T","U","V","W","Y"] #Possibilidades de estudo


def prepare(filepath):
    IMG_SIZE = 64  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("cnn\\output\\treinando_rede_all.model")

prediction = model.predict([prepare('cnn\\lucas.png')]) # Quando usar Predict -> Deve ser uma lista
#prediction = model.predict('cnn\\iris.png')
print(prediction)  # will be a list in a list.
# print(CATEGORIES[int(prediction[0][0])])
valor = np.where(prediction==1)
print(CATEGORIES[int(valor[1])])