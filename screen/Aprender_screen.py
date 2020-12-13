import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QComboBox, QWidget, QVBoxLayout
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

class windowlearn(QMainWindow):
    def __init__(self):
        super().__init__()

#class Ui_windowlearn(object):
 #   def setupUi(self, windowlearn):
  #      windowlearn.setObjectName("Aprender")
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

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_opencv)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

        self.TakePicture = QPushButton('Fotografar',self)
        self.TakePicture.move(300, 530)
        self.TakePicture.resize(70,30)
        self.TakePicture.clicked.connect(self.start_action)

        self.TirarAgora = QPushButton('Tirar',self)
        self.TirarAgora.move(500, 530)
        self.TirarAgora.resize(70,30)
        self.TirarAgora.clicked.connect(self.capture_image)

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

        #self.learn = QtWidgets.QPushButton(self.centralwidget)
        #self.learn.setObjectName("learn")
        self.learn = QtWidgets.QPushButton('Voltar',self) # Declarando o botão 1 para o o objeto
        self.learn.move(630, 530) # Posição do objeto dentro da janela
        self.learn.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        self.learn.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}') # Mudar o estilo do botão

        self.load_window()

    def showTime(self): 
  
        if self.start == True: 
            self.count -= 1
  
            if self.count == 0:
                self.start = False
                self.thread.change_pixmap_signal.connect(self.capture_image)
                self.TakeLabel.setText("Fotografado")
                self.count = 30 

  
        if self.start == True: 
            text = str(self.count / 10) + " s"
            self.TakeLabel.setText(text)

    @QtCore.pyqtSlot()
    def capture_image(self):
        for i in range (30):
            frame= self.thread.capturando
            img_name = 'photos\{}_{}.png'.format(CATEGORIES[self.combo.currentIndex()],i)
            cv2.imwrite(img_name, frame)

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

application = QApplication(sys.argv) # Parametro para fechar janela
j = windowlearn()
sys.exit(application.exec())
