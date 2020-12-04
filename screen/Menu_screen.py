import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QComboBox, QWidget, QVBoxLayout
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread


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
        pixmap = QtGui.QPixmap('geral_images\LogoLibRAS.png')
        smaller_pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.FastTransformation)
        image_logo_LibRAS.setPixmap(QtGui.QPixmap(smaller_pixmap))

        image_logo_RAS = QLabel(self)
        image_logo_RAS.move(640,520)
        image_logo_RAS.resize(151,51)
        image_logo_RAS.setAlignment(QtCore.Qt.AlignCenter)
        pixmapRAS = QtGui.QPixmap('geral_images\LogoRAS.png')
        smaller_pixmapRAS = pixmapRAS.scaled(151, 51, Qt.KeepAspectRatio, Qt.FastTransformation)
        image_logo_RAS.setPixmap(QtGui.QPixmap(smaller_pixmapRAS))


        self.learn = QPushButton("Aprender",self)
        self.learn.move(100,160)
        self.learn.resize(160,80)
        self.learn.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        # learn.clicked.connect(self.select_click)

        self.test = QPushButton("Testar",self)
        self.test.move(100,250)
        self.test.resize(160,80)
        self.test.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        # test.clicked.connect(self.select_click)

        self.info = QPushButton("Informações",self)
        self.info.move(100,340)
        self.info.resize(160,80)
        self.info.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        # info.clicked.connect(self.select_click)

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

    def exit_click(self): # Comando do botão
        sys.exit()


application = QApplication(sys.argv) # Parametro para fechar janela
j = windowMenu()
sys.exit(application.exec())