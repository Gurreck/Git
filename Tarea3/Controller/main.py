import sys
import platform
import json
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
# GUI FILE
from InicioController import Ui_Git

data = {}
data['usuarios'] = []
def registrarUsuario(nombre, password):
    print( "hello")
    if nombre and password:
        global data
        data['usuarios'].append({
            'nombre' : nombre,
            'password': password
        })
        with open('usuarios.txt', 'w') as outfile:
            json.dump(data, outfile)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Git()
        self.ui.setupUi(self)

       # PAGE 1
        self.ui.btn_registrar.clicked.connect(print( "hello"))
        
        # PAGE 1
        self.ui.btn_registrarse.clicked.connect(registrarUsuario(self.ui.text_usuarioRegistro.text(),self.ui.text_passwordRegistro.text()))

        # PAGE 2
        self.ui.btn_atrasRegistro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))

        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
