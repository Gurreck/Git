# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IniciobnmzlE.ui'
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
        Git.resize(1003, 733)
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
        self.label_6.setGeometry(QRect(440, 160, 151, 51))
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
        self.page_adminCreaRepo = QWidget()
        self.page_adminCreaRepo.setObjectName(u"page_adminCreaRepo")
        self.btn_iniciarSesion_2 = QPushButton(self.page_adminCreaRepo)
        self.btn_iniciarSesion_2.setObjectName(u"btn_iniciarSesion_2")
        self.btn_iniciarSesion_2.setGeometry(QRect(370, 300, 281, 31))
        self.btn_iniciarSesion_2.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion_3 = QPushButton(self.page_adminCreaRepo)
        self.btn_iniciarSesion_3.setObjectName(u"btn_iniciarSesion_3")
        self.btn_iniciarSesion_3.setGeometry(QRect(370, 370, 281, 31))
        self.btn_iniciarSesion_3.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.label_7 = QLabel(self.page_adminCreaRepo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 160, 171, 41))
        self.label_7.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_adminCreaRepo)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(430, 140, 171, 41))
        self.label_8.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion_4 = QPushButton(self.page)
        self.btn_iniciarSesion_4.setObjectName(u"btn_iniciarSesion_4")
        self.btn_iniciarSesion_4.setGeometry(QRect(380, 260, 271, 31))
        self.btn_iniciarSesion_4.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion_5 = QPushButton(self.page)
        self.btn_iniciarSesion_5.setObjectName(u"btn_iniciarSesion_5")
        self.btn_iniciarSesion_5.setGeometry(QRect(340, 350, 341, 31))
        self.btn_iniciarSesion_5.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(440, 60, 171, 41))
        self.label_9.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(280, 150, 471, 41))
        self.label_10.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion_6 = QPushButton(self.page_3)
        self.btn_iniciarSesion_6.setObjectName(u"btn_iniciarSesion_6")
        self.btn_iniciarSesion_6.setGeometry(QRect(420, 480, 211, 31))
        self.btn_iniciarSesion_6.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion_7 = QPushButton(self.page_3)
        self.btn_iniciarSesion_7.setObjectName(u"btn_iniciarSesion_7")
        self.btn_iniciarSesion_7.setGeometry(QRect(420, 280, 211, 31))
        self.btn_iniciarSesion_7.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion_8 = QPushButton(self.page_3)
        self.btn_iniciarSesion_8.setObjectName(u"btn_iniciarSesion_8")
        self.btn_iniciarSesion_8.setGeometry(QRect(420, 340, 211, 31))
        self.btn_iniciarSesion_8.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion_9 = QPushButton(self.page_3)
        self.btn_iniciarSesion_9.setObjectName(u"btn_iniciarSesion_9")
        self.btn_iniciarSesion_9.setGeometry(QRect(420, 410, 211, 31))
        self.btn_iniciarSesion_9.setStyleSheet(u"background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(280, 50, 461, 41))
        self.label_13.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(280, 160, 481, 51))
        self.label_11.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.text_password_2 = QLineEdit(self.page_4)
        self.text_password_2.setObjectName(u"text_password_2")
        self.text_password_2.setGeometry(QRect(490, 290, 191, 31))
        self.text_password_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(380, 290, 111, 21))
        self.label_12.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.checkBox_3 = QCheckBox(self.page_4)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(370, 380, 81, 21))
        self.checkBox_3.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.checkBox_4 = QCheckBox(self.page_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(510, 380, 121, 21))
        self.checkBox_4.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.checkBox_5 = QCheckBox(self.page_4)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(680, 380, 121, 21))
        self.checkBox_5.setStyleSheet(u"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.stackedWidget.addWidget(self.page_4)
        Git.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Git)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1003, 26))
        Git.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Git)
        self.statusbar.setObjectName(u"statusbar")
        Git.setStatusBar(self.statusbar)

        self.retranslateUi(Git)

        self.stackedWidget.setCurrentIndex(1)


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
        self.btn_iniciarSesion_2.setText(QCoreApplication.translate("Git", u"Crear Repositorio Principal", None))
        self.btn_iniciarSesion_3.setText(QCoreApplication.translate("Git", u"Administrar Repositorio", None))
        self.label_7.setText(QCoreApplication.translate("Git", u"Opciones", None))
        self.label_8.setText(QCoreApplication.translate("Git", u"Opciones", None))
        self.btn_iniciarSesion_4.setText(QCoreApplication.translate("Git", u"Crear carpeta repositorio", None))
        self.btn_iniciarSesion_5.setText(QCoreApplication.translate("Git", u"Administrar carpetas", None))
        self.label_9.setText(QCoreApplication.translate("Git", u"Carpetas", None))
        self.label_10.setText(QCoreApplication.translate("Git", u"Administracion de carpeta", None))
        self.btn_iniciarSesion_6.setText(QCoreApplication.translate("Git", u"Asignar permisos", None))
        self.btn_iniciarSesion_7.setText(QCoreApplication.translate("Git", u"Commit", None))
        self.btn_iniciarSesion_8.setText(QCoreApplication.translate("Git", u"Update", None))
        self.btn_iniciarSesion_9.setText(QCoreApplication.translate("Git", u"Recuperar archivos", None))
        self.label_13.setText(QCoreApplication.translate("Git", u"Recuperaci\u00f3n de archivos", None))
        self.label_11.setText(QCoreApplication.translate("Git", u"Asignar permisos a usuario", None))
        self.label_12.setText(QCoreApplication.translate("Git", u"Usuario:", None))
        self.checkBox_3.setText(QCoreApplication.translate("Git", u"Crear", None))
        self.checkBox_4.setText(QCoreApplication.translate("Git", u"Modificar", None))
        self.checkBox_5.setText(QCoreApplication.translate("Git", u"Eliminar", None))
    # retranslateUi

