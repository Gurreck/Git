# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InicioeeYLvk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Git(object):
    def setupUi(self, Git):
        if not Git.objectName():
            Git.setObjectName(u"Git")
        Git.resize(1007, 742)
        Git.setStyleSheet(u"background-color: rgb(32, 73, 116)")
        self.centralwidget = QWidget(Git)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1011, 721))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(32, 73, 116)")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.page_inicio.setAutoFillBackground(False)
        self.page_inicio.setStyleSheet(u"")
        self.btn_iniciarSesion = QPushButton(self.page_inicio)
        self.btn_iniciarSesion.setObjectName(u"btn_iniciarSesion")
        self.btn_iniciarSesion.setGeometry(QRect(430, 420, 171, 31))
        self.btn_iniciarSesion.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.label = QLabel(self.page_inicio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 160, 431, 41))
        self.label.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_2 = QLabel(self.page_inicio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 250, 111, 21))
        self.label_2.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_3 = QLabel(self.page_inicio)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 340, 121, 21))
        self.label_3.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.btn_registrar = QPushButton(self.page_inicio)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setGeometry(QRect(430, 470, 171, 31))
        self.btn_registrar.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.text_usuario = QLineEdit(self.page_inicio)
        self.text_usuario.setObjectName(u"text_usuario")
        self.text_usuario.setGeometry(QRect(480, 250, 191, 31))
        self.text_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.text_password = QLineEdit(self.page_inicio)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setGeometry(QRect(480, 340, 191, 31))
        self.text_password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_registro = QWidget()
        self.page_registro.setObjectName(u"page_registro")
        self.label_4 = QLabel(self.page_registro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 350, 121, 21))
        self.label_4.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.text_usuarioRegistro = QLineEdit(self.page_registro)
        self.text_usuarioRegistro.setObjectName(u"text_usuarioRegistro")
        self.text_usuarioRegistro.setGeometry(QRect(500, 260, 191, 31))
        self.text_usuarioRegistro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.text_passwordRegistro = QLineEdit(self.page_registro)
        self.text_passwordRegistro.setObjectName(u"text_passwordRegistro")
        self.text_passwordRegistro.setGeometry(QRect(500, 350, 191, 31))
        self.text_passwordRegistro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.label_5 = QLabel(self.page_registro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 260, 111, 21))
        self.label_5.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_6 = QLabel(self.page_registro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 160, 151, 51))
        self.label_6.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_registrarse = QPushButton(self.page_registro)
        self.btn_registrarse.setObjectName(u"btn_registrarse")
        self.btn_registrarse.setGeometry(QRect(470, 440, 171, 31))
        self.btn_registrarse.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_atrasRegistro = QPushButton(self.page_registro)
        self.btn_atrasRegistro.setObjectName(u"btn_atrasRegistro")
        self.btn_atrasRegistro.setGeometry(QRect(470, 490, 171, 31))
        self.btn_atrasRegistro.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_registro)
        Git.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Git)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1007, 21))
        Git.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Git)
        self.statusbar.setObjectName(u"statusbar")
        Git.setStatusBar(self.statusbar)

        self.retranslateUi(Git)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Git)
    # setupUi

    def retranslateUi(self, Git):
        Git.setWindowTitle(QCoreApplication.translate("Git", u"Git", None))
        self.btn_iniciarSesion.setText(QCoreApplication.translate("Git", u"Iniciar sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Git", u"Bienvenido a Git Papus", None))
        self.label_2.setText(QCoreApplication.translate("Git", u"Usuario:", None))
        self.label_3.setText(QCoreApplication.translate("Git", u"Password:", None))
        self.btn_registrar.setText(QCoreApplication.translate("Git", u"Registrarse", None))
        self.label_4.setText(QCoreApplication.translate("Git", u"Password:", None))
        self.label_5.setText(QCoreApplication.translate("Git", u"Usuario:", None))
        self.label_6.setText(QCoreApplication.translate("Git", u"Registro", None))
        self.btn_registrarse.setText(QCoreApplication.translate("Git", u"Registrarse", None))
        self.btn_atrasRegistro.setText(QCoreApplication.translate("Git", u"Atr\u00e1s", None))
    # retranslateUi

