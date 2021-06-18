import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from InicioController import Ui_Git

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Git()
        self.ui.setupUi(self)
       
       # PAGE 1
        self.ui.btn_registrar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_registro))

        # PAGE 2
        self.ui.btn_atrasRegistro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))

        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
