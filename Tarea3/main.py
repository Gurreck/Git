# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import platform
import json
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import json
import Funciones.login as usuarios
import Funciones.carpetas as carpeta
class Ui_Git(object):
    def setupUi(self, Git):
        Git.setObjectName("Git")
        Git.resize(1003, 733)
        Git.setStyleSheet("background-color: rgb(32, 73, 116)")
        self.centralwidget = QtWidgets.QWidget(Git)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1011, 721))
        self.stackedWidget.setStyleSheet("background-color: rgb(32, 73, 116)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_inicio = QtWidgets.QWidget()
        self.page_inicio.setAutoFillBackground(False)
        self.page_inicio.setStyleSheet("")
        self.page_inicio.setObjectName("page_inicio")
        self.btn_iniciarSesion = QtWidgets.QPushButton(self.page_inicio)
        self.btn_iniciarSesion.setGeometry(QtCore.QRect(430, 420, 171, 31))
        self.btn_iniciarSesion.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_iniciarSesion.setObjectName("btn_iniciarSesion")
        self.label = QtWidgets.QLabel(self.page_inicio)
        self.label.setGeometry(QtCore.QRect(290, 160, 431, 41))
        self.label.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_inicio)
        self.label_2.setGeometry(QtCore.QRect(360, 250, 111, 21))
        self.label_2.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_inicio)
        self.label_3.setGeometry(QtCore.QRect(340, 340, 121, 21))
        self.label_3.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.btn_registrar = QtWidgets.QPushButton(self.page_inicio)
        self.btn_registrar.setGeometry(QtCore.QRect(430, 470, 171, 31))
        self.btn_registrar.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_registrar.setObjectName("btn_registrar")
        self.text_usuario = QtWidgets.QLineEdit(self.page_inicio)
        self.text_usuario.setGeometry(QtCore.QRect(480, 250, 191, 31))
        self.text_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.text_usuario.setObjectName("text_usuario")
        self.text_password = QtWidgets.QLineEdit(self.page_inicio)
        self.text_password.setGeometry(QtCore.QRect(480, 340, 191, 31))
        self.text_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.text_password.setObjectName("text_password")
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_registro = QtWidgets.QWidget()
        self.page_registro.setObjectName("page_registro")
        self.label_4 = QtWidgets.QLabel(self.page_registro)
        self.label_4.setGeometry(QtCore.QRect(360, 350, 121, 21))
        self.label_4.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.text_usuarioRegistro = QtWidgets.QLineEdit(self.page_registro)
        self.text_usuarioRegistro.setGeometry(QtCore.QRect(500, 260, 191, 31))
        self.text_usuarioRegistro.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.text_usuarioRegistro.setObjectName("text_usuarioRegistro")
        self.text_passwordRegistro = QtWidgets.QLineEdit(self.page_registro)
        self.text_passwordRegistro.setGeometry(QtCore.QRect(500, 350, 191, 31))
        self.text_passwordRegistro.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.text_passwordRegistro.setObjectName("text_passwordRegistro")
        self.label_5 = QtWidgets.QLabel(self.page_registro)
        self.label_5.setGeometry(QtCore.QRect(380, 260, 111, 21))
        self.label_5.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_registro)
        self.label_6.setGeometry(QtCore.QRect(440, 160, 151, 51))
        self.label_6.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.btn_registrarse = QtWidgets.QPushButton(self.page_registro)
        self.btn_registrarse.setGeometry(QtCore.QRect(470, 440, 171, 31))
        self.btn_registrarse.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_registrarse.setObjectName("btn_registrarse")
        self.btn_atrasRegistro = QtWidgets.QPushButton(self.page_registro)
        self.btn_atrasRegistro.setGeometry(QtCore.QRect(470, 490, 171, 31))
        self.btn_atrasRegistro.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_atrasRegistro.setObjectName("btn_atrasRegistro")
        self.stackedWidget.addWidget(self.page_registro)
        self.page_adminCreaRepo = QtWidgets.QWidget()
        self.page_adminCreaRepo.setObjectName("page_adminCreaRepo")
        self.btn_crearRepoPrincipal = QtWidgets.QPushButton(self.page_adminCreaRepo)
        self.btn_crearRepoPrincipal.setGeometry(QtCore.QRect(370, 300, 281, 31))
        self.btn_crearRepoPrincipal.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_crearRepoPrincipal.setObjectName("btn_crearRepoPrincipal")
        self.btn_administrarRepositorioPrincipal = QtWidgets.QPushButton(self.page_adminCreaRepo)
        self.btn_administrarRepositorioPrincipal.setGeometry(QtCore.QRect(370, 370, 281, 31))
        self.btn_administrarRepositorioPrincipal.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_administrarRepositorioPrincipal.setObjectName("btn_administrarRepositorioPrincipal")
        self.label_7 = QtWidgets.QLabel(self.page_adminCreaRepo)
        self.label_7.setGeometry(QtCore.QRect(430, 160, 171, 41))
        self.label_7.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_adminCreaRepo)
        self.page_userCreaRepo = QtWidgets.QWidget()
        self.page_userCreaRepo.setObjectName("page_userCreaRepo")
        self.label_8 = QtWidgets.QLabel(self.page_userCreaRepo)
        self.label_8.setGeometry(QtCore.QRect(430, 140, 171, 41))
        self.label_8.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_8.setObjectName("label_8")
        self.btn_crearRepoUser = QtWidgets.QPushButton(self.page_userCreaRepo)
        self.btn_crearRepoUser.setGeometry(QtCore.QRect(380, 260, 271, 31))
        self.btn_crearRepoUser.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_crearRepoUser.setObjectName("btn_crearRepoUser")
        self.btn_administrarCarpetasUser = QtWidgets.QPushButton(self.page_userCreaRepo)
        self.btn_administrarCarpetasUser.setGeometry(QtCore.QRect(340, 350, 341, 31))
        self.btn_administrarCarpetasUser.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_administrarCarpetasUser.setObjectName("btn_administrarCarpetasUser")
        self.stackedWidget.addWidget(self.page_userCreaRepo)
        self.page_carpetasUser = QtWidgets.QWidget()
        self.page_carpetasUser.setObjectName("page_carpetasUser")
        self.label_9 = QtWidgets.QLabel(self.page_carpetasUser)
        self.label_9.setGeometry(QtCore.QRect(440, 60, 171, 41))
        self.label_9.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_carpetasUser)
        self.page_administrarCarpetasUser = QtWidgets.QWidget()
        self.page_administrarCarpetasUser.setObjectName("page_administrarCarpetasUser")
        self.label_10 = QtWidgets.QLabel(self.page_administrarCarpetasUser)
        self.label_10.setGeometry(QtCore.QRect(280, 150, 471, 41))
        self.label_10.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_10.setObjectName("label_10")
        self.btn_asignarPermisos = QtWidgets.QPushButton(self.page_administrarCarpetasUser)
        self.btn_asignarPermisos.setGeometry(QtCore.QRect(420, 480, 211, 31))
        self.btn_asignarPermisos.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_asignarPermisos.setObjectName("btn_asignarPermisos")
        self.btn_commit = QtWidgets.QPushButton(self.page_administrarCarpetasUser)
        self.btn_commit.setGeometry(QtCore.QRect(420, 280, 211, 31))
        self.btn_commit.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_commit.setObjectName("btn_commit")
        self.btn_update = QtWidgets.QPushButton(self.page_administrarCarpetasUser)
        self.btn_update.setGeometry(QtCore.QRect(420, 340, 211, 31))
        self.btn_update.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_update.setObjectName("btn_update")
        self.btn_recuperarArchivos = QtWidgets.QPushButton(self.page_administrarCarpetasUser)
        self.btn_recuperarArchivos.setGeometry(QtCore.QRect(420, 410, 211, 31))
        self.btn_recuperarArchivos.setStyleSheet("background-color: rgb(255, 172, 56);\n"
"font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.btn_recuperarArchivos.setObjectName("btn_recuperarArchivos")
        self.stackedWidget.addWidget(self.page_administrarCarpetasUser)
        self.page_recuperacionArchivos = QtWidgets.QWidget()
        self.page_recuperacionArchivos.setObjectName("page_recuperacionArchivos")
        self.label_13 = QtWidgets.QLabel(self.page_recuperacionArchivos)
        self.label_13.setGeometry(QtCore.QRect(280, 50, 461, 41))
        self.label_13.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_13.setObjectName("label_13")
        self.stackedWidget.addWidget(self.page_recuperacionArchivos)
        self.page_asignarPermisosUser = QtWidgets.QWidget()
        self.page_asignarPermisosUser.setObjectName("page_asignarPermisosUser")
        self.label_11 = QtWidgets.QLabel(self.page_asignarPermisosUser)
        self.label_11.setGeometry(QtCore.QRect(280, 160, 481, 51))
        self.label_11.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 38px;\n"
"font-weight: bold;")
        self.label_11.setObjectName("label_11")
        self.text_usuarioPermiso = QtWidgets.QLineEdit(self.page_asignarPermisosUser)
        self.text_usuarioPermiso.setGeometry(QtCore.QRect(490, 290, 191, 31))
        self.text_usuarioPermiso.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: ebrima;\n"
"color:rgb(0, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.text_usuarioPermiso.setObjectName("text_usuarioPermiso")
        self.label_12 = QtWidgets.QLabel(self.page_asignarPermisosUser)
        self.label_12.setGeometry(QtCore.QRect(380, 290, 111, 21))
        self.label_12.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.label_12.setObjectName("label_12")
        self.check_crear = QtWidgets.QCheckBox(self.page_asignarPermisosUser)
        self.check_crear.setGeometry(QtCore.QRect(370, 380, 81, 21))
        self.check_crear.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.check_crear.setObjectName("check_crear")
        self.check_modificar = QtWidgets.QCheckBox(self.page_asignarPermisosUser)
        self.check_modificar.setGeometry(QtCore.QRect(510, 380, 121, 21))
        self.check_modificar.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.check_modificar.setObjectName("check_modificar")
        self.check_eliminar = QtWidgets.QCheckBox(self.page_asignarPermisosUser)
        self.check_eliminar.setGeometry(QtCore.QRect(680, 380, 121, 21))
        self.check_eliminar.setStyleSheet("font-family: ebrima;\n"
"color:rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.check_eliminar.setObjectName("check_eliminar")
        self.stackedWidget.addWidget(self.page_asignarPermisosUser)
        Git.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Git)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 26))
        self.menubar.setObjectName("menubar")
        Git.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Git)
        self.statusbar.setObjectName("statusbar")
        Git.setStatusBar(self.statusbar)

        self.retranslateUi(Git)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Git)

        self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registro))
        self.btn_atrasRegistro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_inicio))
        self.btn_registrarse.clicked.connect(lambda: usuarios.login.registrarUsuario(self.text_usuarioRegistro.text(),self.text_passwordRegistro.text()))
        self.btn_iniciarSesion.clicked.connect(lambda: usuarios.login.autenficarUsuario(self.text_usuario.text(),self.text_password.text()))
        self.btn_crearRepoPrincipal.clicked.connect(lambda: carpeta.carpeta.crearCapeta)

    def retranslateUi(self, Git):
        _translate = QtCore.QCoreApplication.translate
        Git.setWindowTitle(_translate("Git", "Git"))
        self.btn_iniciarSesion.setText(_translate("Git", "Iniciar sesión"))
        self.label.setText(_translate("Git", "Bienvenido a Git Papus"))
        self.label_2.setText(_translate("Git", "Usuario:"))
        self.label_3.setText(_translate("Git", "Password:"))
        self.btn_registrar.setText(_translate("Git", "Registrarse"))
        self.label_4.setText(_translate("Git", "Password:"))
        self.label_5.setText(_translate("Git", "Usuario:"))
        self.label_6.setText(_translate("Git", "Registro"))
        self.btn_registrarse.setText(_translate("Git", "Registrarse"))
        self.btn_atrasRegistro.setText(_translate("Git", "Atrás"))
        self.btn_crearRepoPrincipal.setText(_translate("Git", "Crear Repositorio Principal"))
        self.btn_administrarRepositorioPrincipal.setText(_translate("Git", "Administrar Repositorio"))
        self.label_7.setText(_translate("Git", "Opciones"))
        self.label_8.setText(_translate("Git", "Opciones"))
        self.btn_crearRepoUser.setText(_translate("Git", "Crear carpeta repositorio"))
        self.btn_administrarCarpetasUser.setText(_translate("Git", "Administrar carpetas"))
        self.label_9.setText(_translate("Git", "Carpetas"))
        self.label_10.setText(_translate("Git", "Administracion de carpeta"))
        self.btn_asignarPermisos.setText(_translate("Git", "Asignar permisos"))
        self.btn_commit.setText(_translate("Git", "Commit"))
        self.btn_update.setText(_translate("Git", "Update"))
        self.btn_recuperarArchivos.setText(_translate("Git", "Recuperar archivos"))
        self.label_13.setText(_translate("Git", "Recuperación de archivos"))
        self.label_11.setText(_translate("Git", "Asignar permisos a usuario"))
        self.label_12.setText(_translate("Git", "Usuario:"))
        self.check_crear.setText(_translate("Git", "Crear"))
        self.check_modificar.setText(_translate("Git", "Modificar"))
        self.check_eliminar.setText(_translate("Git", "Eliminar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Git = QtWidgets.QMainWindow()
    ui = Ui_Git()
    ui.setupUi(Git)
    Git.show()
    sys.exit(app.exec_())
