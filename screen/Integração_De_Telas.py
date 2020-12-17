import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

from Menu_screen import *

# from info_screen import *
# from Aprender_screen import *
# from Testar_screen import *


# class Aprender(QMainWindow):
#     def __init__ (self):
#         super() .__init__()
#         self.ui = Ui_windowlearn()
#         self.ui.setupUi(self)
#         self.ui.learn.clicked.connect(self.voltaJanela)

#     def voltaJanela(self):
#         self.origem = Menu()
#         self.origem.show()
#         self.close()


# class Testar(QMainWindow):
#     def __init__ (self):
#         super() .__init__()
#         self.ui = Ui_windowTestar()
#         self.ui.setupUi(self)
#         self.ui.test.clicked.connect(self.voltaJanela)

#     def voltaJanela(self):
#         self.origem = Menu()
#         self.origem.show()
#         self.close()


# class Info(QMainWindow):
#     def __init__ (self):
#         super() .__init__()
#         self.ui = Ui_windowInfo()
#         self.ui.setupUi(self)
#         self.ui.info.clicked.connect(self.voltaJanela)

#     def voltaJanela(self):
#         self.origem = Menu()
#         self.origem.show()
#         self.close()


# class Menu(QMainWindow):
#     def __init__ (self):
#         super() .__init__()
#         self.ui = Ui_windowMenu()
#         self.ui.setupUi(self)
#         self.Aprender = Aprender()
#         self.ui.learn.clicked.connect(self.mudaJanela)
#         self.Testar = Testar()
#         self.ui.test.clicked.connect(self.mudaJanela2)
#         self.Info = Info()
#         self.ui.info.clicked.connect(self.mudaJanela3)


#     def mudaJanela(self):
#         self.Aprender.show()
#         self.hide()

#     def mudaJanela2(self):
#         self.Testar.show()
#         self.hide()

#     def mudaJanela3(self):
#         self.Info.show()
#         self.hide()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = Menu()
#     w.show()
#     sys.exit(app.exec_())