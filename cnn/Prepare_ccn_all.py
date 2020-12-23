import numpy as np
import matplotlib.pyplot as plt
import os
import cv2


DIRTRANING = "cnn\\dataset\\training" #Onde estão salvas as imagens de training
DIRTEST = "cnn\\dataset\\test" #Onde estão salvas as imagens de test
CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","S","T","U","V","W","Y"] #Possibilidades de estudo
# CATEGORIES = ["A","B"]

IMG_SIZE = 64

def create_data(DIRECTORY):
    data = []
    for category in CATEGORIES:
        path = os.path.join(DIRECTORY,category) # Caminho com os diretórios das letras
        class_num = CATEGORIES.index(category) # Dando um número para a categoria
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) #Cada imagem também é convertida na escala de cinza
                new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #Redimensionando a imagem
                data.append([new_array,class_num]) #Inserindo a imagem e sua classificação
                print(category, img, DIRECTORY)
            except Exception as e: #Erro que pode ocorrer ao importar imagens
                pass
    return data

training_data = create_data(DIRTRANING)
test_data = create_data(DIRTEST)

import random

random.shuffle(training_data) #Embaralhando os dados que a rede vai usar para treinar
random.shuffle(test_data)

X_training = [] # Features for training
y_training = [] # Labels for training

X_test = [] # Features for test
y_test = [] # Labels for test

def organize(data, X, y):
    for features, label in data:
        X.append(features)
        y.append(label)

organize(training_data, X_training, y_training)
organize(test_data, X_test, y_test)

X_training = np.array(X_training).reshape(-1, IMG_SIZE, IMG_SIZE, 1) # -1: Quantas features tem, IMG_SIZE x IMG_SIZE: tamanho da imagem, 1: indica que o canal de cores é só o cinza (3 se RGB)
X_test = np.array(X_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1) # -1: Quantas features tem, IMG_SIZE x IMG_SIZE: tamanho da imagem, 1: indica que o canal de cores é só o cinza (3 se RGB)

import pickle # Salvar os arquivos criados 

pickle_out = open("cnn\\output\\X_training.pickle","wb") # Salvar X_training
pickle.dump(X_training,pickle_out)
pickle_out.close()
print("Saved X_training.pickle")

pickle_out = open("cnn\\output\\y_training.pickle","wb") # Salvar y_training
pickle.dump(y_training,pickle_out)
pickle_out.close()
print("Saved y_training.pickle")

pickle_out = open("cnn\\output\\X_test.pickle","wb") # Salvar X_training
pickle.dump(X_test,pickle_out)
pickle_out.close()
print("Saved X_test.pickle")

pickle_out = open("cnn\\output\\y_test.pickle","wb") # Salvar y_training
pickle.dump(y_test,pickle_out)
pickle_out.close()
print("Saved y_test.pickle")