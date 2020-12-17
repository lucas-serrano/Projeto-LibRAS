import numpy as np
import matplotlib.pyplot as plt
import os
import cv2


DATADIR = "cnn\\dataset\\training" #Onde estão sendo armazenados os arquivos
CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","T","U","V","W","Y"] #Possibilidades de estudo

training_data = []
IMG_SIZE = 64

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category) # Caminho com os diretórios das letras
        class_num = CATEGORIES.index(category) # Dando um número para a categoria
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) #Cada imagem também é convertida na escala de cinza
                new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #Redimensionando a imagem
                training_data.append([new_array,class_num]) #Inserindo a imagem e sua classificação
                print(category, img)
            except Exception as e: #Erro que pode ocorrer ao importar imagens
                pass

create_training_data()

import random
random.shuffle(training_data) #Embaralhando os dados que a rede vai usar para treinar

X = [] # Features
y = [] # Labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) # -1: Quantas features tem, IMG_SIZE x IMG_SIZE: tamanho da imagem, 1: indica que o canal de cores é só o cinza (3 se RGB)

import pickle # Salvar os arquivos criados 

pickle_out = open("cnn\\output\\X_all.pickle","wb") # Salvar X
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out = open("cnn\\output\\y_all.pickle","wb") # Salvar y
pickle.dump(y,pickle_out)
pickle_out.close()