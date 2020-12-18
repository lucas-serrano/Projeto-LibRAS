import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QComboBox, QWidget, QVBoxLayout, QSpinBox
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QTimer

import cv2
import numpy as np

import datetime
from datetime import date


CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","T","U","V","W","Y"]

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while True:
            ret, cv_img = cap.read()
            crop_img = cv_img[100:300, 100:300]
            self.capturando = crop_img

            if ret:
                self.change_pixmap_signal.emit(crop_img)

class windowMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.upper = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.name = "Menu"

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        title = QLabel(self)
        title.move(250,40)
        title.resize(300,90)
        title.setText("LibRAS")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet('QLabel {font:bold; font-size:35px; color:#BA0C2F}')

        image_logo_LibRAS = QLabel(self)
        image_logo_LibRAS.move(320,140)
        image_logo_LibRAS.resize(400,400)
        image_logo_LibRAS.setAlignment(QtCore.Qt.AlignCenter)
        pixmap = QtGui.QPixmap('screen\geral_images\LogoLibRAS.png')
        smaller_pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.FastTransformation)
        image_logo_LibRAS.setPixmap(QtGui.QPixmap(smaller_pixmap))

        image_logo_RAS = QLabel(self)
        image_logo_RAS.move(640,520)
        image_logo_RAS.resize(151,51)
        image_logo_RAS.setAlignment(QtCore.Qt.AlignCenter)
        pixmapRAS = QtGui.QPixmap('screen\geral_images\LogoRAS.png')
        smaller_pixmapRAS = pixmapRAS.scaled(151, 51, Qt.KeepAspectRatio, Qt.FastTransformation)
        image_logo_RAS.setPixmap(QtGui.QPixmap(smaller_pixmapRAS))


        self.learn = QPushButton("Aprender",self)
        self.learn.move(100,160)
        self.learn.resize(160,80)
        self.learn.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        self.learn.clicked.connect(self.load_learn)

        self.test = QPushButton("Testar",self)
        self.test.move(100,250)
        self.test.resize(160,80)
        self.test.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        self.test.clicked.connect(self.load_test)

        self.info = QPushButton("Informações",self)
        self.info.move(100,340)
        self.info.resize(160,80)
        self.info.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        self.info.clicked.connect(self.load_info)

        exit = QPushButton('Sair',self) # Declarando o botão 1 para o o objeto
        exit.move(100, 430) # Posição do objeto dentro da janela
        exit.resize(160,80) # Define o tamanho do botão (Largura, Altura)
        exit.setStyleSheet('QPushButton {background-color:#BA0C2F; font-size:18px; color:white}') # Mudar o estilo do botão
        exit.clicked.connect(self.exit_click)


        self.load_window()

    def load_window(self):
        self.setGeometry(self.left,self.upper,self.width,self.height)
        self.setWindowTitle(self.name)
        self.show()

    def load_learn(self):
        Menu.hide()
        Aprender.load_window()

    def load_test(self):
        Menu.hide()
        Testar.load_window()

    def load_info(self):
        Menu.hide()
        Info.load_window()

    def exit_click(self): # Comando do botão
        sys.exit()

class windowlearn(QMainWindow):
    def __init__(self):
        super().__init__()

        self.upper = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.name = "Aprender"

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        combo_text = QLabel(self)
        combo_text.move(30,60)
        combo_text.resize(200,20)
        combo_text.setText("Selecione uma letra")
        combo_text.setAlignment(QtCore.Qt.AlignCenter)
        combo_text.setStyleSheet('QLabel {font:bold; font-size:20px; color="black"}')

        self.combo = QComboBox(self)
        self.combo.addItems(CATEGORIES)
        self.combo.move(30,100)
        self.combo.resize(200,30)

        select = QPushButton("Aprender!",self) # ! Só para ser ousado
        select.move(30,140)
        select.resize(200,30)
        select.clicked.connect(self.select_click)

        image_text = QLabel(self)
        image_text.move(30,270)
        image_text.resize(200,20)
        image_text.setText("Imite a letra")
        image_text.setAlignment(QtCore.Qt.AlignCenter)
        image_text.setStyleSheet('QLabel {font:bold; font-size:20px; color="black"}')

        self.image_hand = QLabel(self)
        self.image_hand.move(30,300)
        self.image_hand.resize(200,200)
        self.image_hand.setStyleSheet("border: 3px solid black;") 
        self.image_hand.setAlignment(QtCore.Qt.AlignCenter)
        self.image_hand.setPixmap(QtGui.QPixmap('hands_images\none.png'))

        self.image_opencv = QLabel(self)
        self.image_opencv.move(300, 50)
        self.image_opencv.resize(450, 450)
        self.image_opencv.setStyleSheet("border: 3px solid black;")

        self.Caixa = QSpinBox(self)
        self.Caixa.resize(200,20)
        self.Caixa.move(30,200)
        self.Caixa.setMaximum(3000)

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_opencv)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        ##### self.thread = VideoThread()
        # connect its signal to the update_image slot
        thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        thread.start()

        self.TakePicture = QPushButton('Fotografar',self)
        self.TakePicture.move(300, 530)
        self.TakePicture.resize(70,30)
        self.TakePicture.clicked.connect(self.start_action)

        self.count = 30
        self.start = False
        
        self.TakeLabel = QLabel('Texto',self)
        self.TakeLabel.move(400, 530)
        self.TakeLabel.resize(100,30)

        timer = QTimer(self) 
        timer.timeout.connect(self.showTime)
        timer.start(100) 

        exit = QPushButton('Sair',self) # Declarando o botão 1 para o o objeto
        exit.move(700, 530) # Posição do objeto dentro da janela
        exit.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        exit.setStyleSheet('QPushButton {background-color:#BA0C2F; font-size:18px; color:white}') # Mudar o estilo do botão
        exit.clicked.connect(self.exit_click)

        self.back = QPushButton('Voltar',self) # Declarando o botão 1 para o o objeto
        self.back.move(630, 530) # Posição do objeto dentro da janela
        self.back.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        self.back.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}') # Mudar o estilo do botão
        self.back.clicked.connect(self.back_click)

        # self.load_window()

    def showTime(self): 
  
        if self.start == True: 
            self.count -= 1
  
            if self.count == 0:
                self.start = False
                # thread.change_pixmap_signal.connect(self.capture_image)
                fotos = self.capture_image()
                self.TakeLabel.setText("Fotografado")
                self.count = 30 

  
        if self.start == True: 
            text = str(self.count / 10) + " s"
            self.TakeLabel.setText(text)

    @QtCore.pyqtSlot()
    def capture_image(self):
        for i in range (30):
            frame= thread.capturando
            img_name = 'screen\photos\{}\{}.png'.format(CATEGORIES[self.combo.currentIndex()],i+self.Caixa.value())
            cv2.imwrite(img_name, frame)
        self.Caixa.setValue(self.Caixa.value() + 30)
        return True


    def start_action(self): 
        
        self.start = True
  
        if self.count == 0: 
            self.start = False

    def load_window(self):
        self.setGeometry(self.left,self.upper,self.width,self.height)
        self.setWindowTitle(self.name)
        self.show()

    def select_click(self):
        pixmap = QtGui.QPixmap('screen\hands_images\{}.png'.format(CATEGORIES[self.combo.currentIndex()]))
        smaller_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_hand.setPixmap(smaller_pixmap)

    def exit_click(self): # Comando do botão
        sys.exit()

    def back_click(self):
        Aprender.close()
        Menu.show()

    @pyqtSlot(np.ndarray)
    def update_image(self, crop_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(crop_img)
        self.image_opencv.setPixmap(qt_img)
    
    def convert_cv_qt(self, crop_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(450, 450, Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)

class windowTestar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.upper = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.name = "Testar"

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        image_text = QLabel(self)
        image_text.move(30,270)
        image_text.resize(200,20)
        image_text.setText("Imite a letra")
        image_text.setAlignment(QtCore.Qt.AlignCenter)
        image_text.setStyleSheet('QLabel {font:bold; font-size:20px; color="black"}')

        self.image_hand = QLabel(self)
        self.image_hand.move(30,300)
        self.image_hand.resize(200,200)
        self.image_hand.setStyleSheet("border: 3px solid black;") 
        self.image_hand.setAlignment(QtCore.Qt.AlignCenter)
        self.image_hand.setPixmap(QtGui.QPixmap('hands_images\none.png'))

        self.image_opencv = QLabel(self)
        self.image_opencv.move(300, 50)
        self.image_opencv.resize(450, 450)
        self.image_opencv.setStyleSheet("border: 3px solid black;") 

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_opencv)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        #####self.thread = VideoThread()
        # connect its signal to the update_image slot
        thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        thread.start()

        self.TakePicture = QPushButton('Fotografar',self)
        self.TakePicture.move(300, 530)
        self.TakePicture.resize(70,30)
        self.TakePicture.clicked.connect(self.start_action)

        self.count = 30
        self.start = False
        
        self.TakeLabel = QLabel('Texto',self)
        self.TakeLabel.move(400, 530)
        self.TakeLabel.resize(100,30)

        timer = QTimer(self) 
        timer.timeout.connect(self.showTime)
        timer.start(100) 

        exit = QPushButton('Sair',self) # Declarando o botão 1 para o o objeto
        exit.move(700, 530) # Posição do objeto dentro da janela
        exit.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        exit.setStyleSheet('QPushButton {background-color:#BA0C2F; font-size:18px; color:white}') # Mudar o estilo do botão
        exit.clicked.connect(self.exit_click)

        self.back = QPushButton('Voltar',self) # Declarando o botão 1 para o o objeto
        self.back.move(630, 530) # Posição do objeto dentro da janela
        self.back.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        self.back.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}') # Mudar o estilo do botão
        self.back.clicked.connect(self.back_click)

        # self.load_window()

    def showTime(self): 
  
        if self.start == True: 
            self.count -= 1
  
            if self.count == 0:
                self.start = False
                # thread.change_pixmap_signal.connect(self.capture_image)
                fotos = self.capture_image()
                self.TakeLabel.setText("Fotografado")
                self.count = 30 

  
        if self.start == True: 
            text = str(self.count / 10) + " s"
            self.TakeLabel.setText(text)

    @QtCore.pyqtSlot()
    def capture_image(self):
        for i in range (30):
            frame= thread.capturando
            img_name = 'screen\photos\{}_{}.png'.format('a_mimir',i)
            cv2.imwrite(img_name, frame)
        return True

    def start_action(self): 
        
        self.start = True
  
        if self.count == 0: 
            self.start = False

    def load_window(self):
        self.setGeometry(self.left,self.upper,self.width,self.height)
        self.setWindowTitle(self.name)
        self.show()

    def select_click(self):
        pixmap = QtGui.QPixmap('hands_images\{}.png'.format(CATEGORIES[self.combo.currentIndex()]))
        smaller_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_hand.setPixmap(smaller_pixmap)

    def exit_click(self): # Comando do botão
        sys.exit()

    def back_click(self):
        Testar.close()
        Menu.show()

    @pyqtSlot(np.ndarray)
    def update_image(self, crop_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(crop_img)
        self.image_opencv.setPixmap(qt_img)
    
    def convert_cv_qt(self, crop_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(450, 450, Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)

class windowInfo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.upper = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.name = "Info"

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        title = QLabel(self)
        title.move(250,40)
        title.resize(300,90)
        title.setText("LibRAS")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet('QLabel {font:bold; font-size:35px; color:#BA0C2F}')

        title_learn = QLabel(self)
        title_learn.move(130,120)
        title_learn.resize(161,71)
        title_learn.setText("Aprender")
        title_learn.setAlignment(QtCore.Qt.AlignCenter)
        title_learn.setStyleSheet('QLabel {background-color:#772583; font-size:30px; color:"white"}')

        title_test = QLabel(self)
        title_test.move(530,120)
        title_test.resize(111,71)
        title_test.setText("Testar")
        title_test.setAlignment(QtCore.Qt.AlignCenter)
        title_test.setStyleSheet('QLabel {background-color:#772583; font-size:30px; color:"white"}')

        text_learn = QLabel(self)
        text_learn.move(30,230)
        text_learn.resize(361,281)
        text_learn.setText("Modo de treino, onde o usuário receberá a imagem da letra e do movimento que deverá ser executado para a validação. Caso esteja errado, deverá tentar novamente até que o movimento seja executado de maneira correta, seguindo para a próxima letra do alfabeto estático de forma aleatória.")
        text_learn.setAlignment(QtCore.Qt.AlignCenter)
        text_learn.setWordWrap(True)
        text_learn.setStyleSheet('QLabel {background-color:#772583; font-size:12px; color:"black"}')

        text_learn.setLayoutDirection(QtCore.Qt.LeftToRight)
        text_learn.setInputMethodHints(QtCore.Qt.ImhNone)
        text_learn.setFrameShape(QtWidgets.QFrame.Box)
        text_learn.setFrameShadow(QtWidgets.QFrame.Raised)
        text_learn.setLineWidth(3)
        text_learn.setTextFormat(QtCore.Qt.MarkdownText)
        text_learn.setScaledContents(False)

        text_test = QLabel(self)
        text_test.move(410,230)
        text_test.resize(361,281)
        text_test.setText("Modo para avaliar o aprendizado de LIBRAS, no qual o usuário receberá apenas a imagem da letra que deverá ser executada. O programa avaliará quais letras deverão ser feitas com maior frequência para reforçar o entendimento, e por meio do SRS (Sistema de Repetição Espaçada) encontrará a melhor maneira de fixação do que foi visto.")
        text_test.setAlignment(QtCore.Qt.AlignCenter)
        text_test.setWordWrap(True)
        text_test.setStyleSheet('QLabel {background-color:#772583; font-size:12px; color:"black"}')

        text_test.setLayoutDirection(QtCore.Qt.LeftToRight)
        text_test.setInputMethodHints(QtCore.Qt.ImhNone)
        text_test.setFrameShape(QtWidgets.QFrame.Box)
        text_test.setFrameShadow(QtWidgets.QFrame.Raised)
        text_test.setLineWidth(3)
        text_test.setTextFormat(QtCore.Qt.MarkdownText)
        text_test.setScaledContents(False)


        # image_logo_LibRAS = QLabel(self)
        # image_logo_LibRAS.move(320,140)
        # image_logo_LibRAS.resize(400,400)
        # image_logo_LibRAS.setAlignment(QtCore.Qt.AlignCenter)
        # pixmap = QtGui.QPixmap('geral_images\LogoLibRAS.png')
        # smaller_pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.FastTransformation)
        # image_logo_LibRAS.setPixmap(QtGui.QPixmap(smaller_pixmap))

        # image_logo_RAS = QLabel(self)
        # image_logo_RAS.move(640,520)
        # image_logo_RAS.resize(151,51)
        # image_logo_RAS.setAlignment(QtCore.Qt.AlignCenter)
        # pixmapRAS = QtGui.QPixmap('geral_images\LogoRAS.png')
        # smaller_pixmapRAS = pixmapRAS.scaled(151, 51, Qt.KeepAspectRatio, Qt.FastTransformation)
        # image_logo_RAS.setPixmap(QtGui.QPixmap(smaller_pixmapRAS))

        exit = QPushButton('Sair',self) # Declarando o botão 1 para o o objeto
        exit.move(700, 530) # Posição do objeto dentro da janela
        exit.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        exit.setStyleSheet('QPushButton {background-color:#BA0C2F; font-size:18px; color:white}') # Mudar o estilo do botão
        exit.clicked.connect(self.exit_click)

        self.back = QPushButton('Voltar',self) # Declarando o botão 1 para o o objeto
        self.back.move(630, 530) # Posição do objeto dentro da janela
        self.back.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        self.back.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}') # Mudar o estilo do botão
        self.back.clicked.connect(self.back_click)

        # self.load_window()

    def load_window(self):
        self.setGeometry(self.left,self.upper,self.width,self.height)
        self.setWindowTitle(self.name)
        self.show()

    def exit_click(self): # Comando do botão
        sys.exit()

    def back_click(self):
        Info.close()
        Menu.show()

application = QApplication(sys.argv) # Parametro para fechar janela

thread = VideoThread()

Testar = windowTestar()
Aprender = windowlearn()
Info = windowInfo()
Menu = windowMenu()
sys.exit(application.exec())