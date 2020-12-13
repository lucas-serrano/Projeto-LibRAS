import datetime
from datetime import date
from datetime import time

#Bibliotecas para função cria_dataset()
import cv2
import numpy as np
import math

def cria_dataset(cadastro): # Mesma função que a Iris explicou no último cooworking
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        ret, img = cap.read()

        cv2.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 0)
        crop_img = img[100:300, 100:300]

        grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

        value = (35, 35)
        blurred = cv2.GaussianBlur(grey, value, 0)

        _, thresh1 = cv2.threshold(blurred, 127, 255,
            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        
        # cv2.imshow('Thresholded', thresh1) # Mostra o background subtractor

        (version, _, _) = cv2.__version__.split('.')

        if version == '3':
            image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
                cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        elif version == '4':
            contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, \
                cv2.CHAIN_APPROX_NONE)
        
        cnt = max(contours, key = lambda x: cv2.contourArea(x))

        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

        hull = cv2.convexHull(cnt)

        drawing = np.zeros(crop_img.shape, np.uint8)
        cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 0)

        hull = cv2.convexHull(cnt, returnPoints=False)

        defects = cv2.convexityDefects(cnt, hull)
        count_defects = 0
        cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]

            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])

            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

            angle = math.acos((b**2 + c**2 - a**2) / (2*b*c)) * 57

            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_img, far, 1, [0, 0, 255], -1)
            
            cv2.line(crop_img, start, end, [0, 255, 0], 2)
        
        # if count_defects == 1:
        #     str = "Detect"
        #     cv2.putText(img, str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # elif count_defects == 2:
        #     str = "Detect"
        #     cv2.putText(img, str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # elif count_defects == 3:
        #     str = "Detect"
        #     cv2.putText(img, str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # elif count_defects == 4:
        #     str = "Detect"
        #     cv2.putText(img, str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # else:
        #     str = "Detect"
        #     cv2.putText(img, str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        str1 = 'Posicione sua mao dentro do quadrado'
        cv2.putText(img, str1, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        str2 = 'Aperte "Espaco" para salvar o movimento'
        cv2.putText(img, str2, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        

        cv2.imshow('Gesture', img)
        all_img = np.hstack((drawing, crop_img))
        # cv2.imshow('Contours', all_img) # Mostrar tela de captura de mão
        
        if cv2.waitKey(1)%256 == 32: # Espaço tira a foto
            print("Capturando fotos")
            for i in range (30):
                ret, img = cap.read()
                crop_img = img[100:300, 100:300] # Atualizando o crop_img toda vez que passa por aqui
                img_name = '{}{}{}{}_{}.png'.format(cadastro,today.year,today.month,today.day,i)
                # img_name = "opencv_frame_{}.png".format(i)
                cv2.imwrite(img_name, crop_img)
                print("{} written!".format(img_name))
            break

        k = cv2.waitKey(10)
        if k == 27:
            break

# Programa principal

CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","T","U","V","W","Y"] #Possibilidades de estudo


print('Cadastrar nova letra no dataset? s / n') 
answer = list(input().lower()) # Transformando numa lista, dessa forma o código pode ler quando entre SIM ou NÃO

if answer[0] == 's':
    print('Qual letra deseja cadastrar no dataset?')
    letra_cad = ['placeholder']
    while letra_cad[0] not in CATEGORIES:
        letra_cad = list(input().upper())
    
    print('Letra que irá ser cadastrada:',letra_cad[0])
    print('Iniciando programa de captura...')

    cria_dataset(letra_cad[0])