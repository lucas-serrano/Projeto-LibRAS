import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QComboBox, QWidget, QVBoxLayout
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread


class Ui_windowInfo(object):
    def setupUi(self, windowInfo):
        Info.setObjectName("Info")

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

        self.info = QPushButton('Voltar',self) # Declarando o botão 1 para o o objeto
        self.info.move(630, 530) # Posição do objeto dentro da janela
        self.info.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        self.info.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}') # Mudar o estilo do botão

        self.load_window()

    def load_window(self):
        self.setGeometry(self.left,self.upper,self.width,self.height)
        self.setWindowTitle(self.name)
        self.show()

    def exit_click(self): # Comando do botão
        sys.exit()


application = QApplication(sys.argv) # Parametro para fechar janela
j = Ui_windowInfo()
sys.exit(application.exec())