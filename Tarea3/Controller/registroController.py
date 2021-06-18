import sys
import os
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile
class registroController:
    def __init__(self):
        super(registroController, self).__init__()
        self.ui = QUiLoader().load(QFile("View/Registro.ui"))
    def doSomething(self):
        window = self.ui()
        window.show()
        self.close()