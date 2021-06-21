from PyQt5 import QtWidgets, uic

import sys
import Funciones.login as usuarios
import Funciones.carpetas as carpeta
import json
app = QtWidgets.QApplication([])

win = uic.loadUi("Controller/Inicio.ui")
usuarios.login.leerUsuarios()
def autenficarUsuario(nombre, password):
    with open('Usuarios/usuarios.txt') as file:
        data = json.load(file)
        for usuario in data['usuarios']:
            if(usuario['nombre']==nombre and usuario['password']==password):
                global win
                if(nombre == 'admin'):
                    win.stackedWidget.setCurrentWidget(win.page_adminCreaRepo)
                else:
                    win.stackedWidget.setCurrentWidget(win.page_userCreaRepo)
                print("Autenticado")
                break
            else:
                print("No autenticado")

win.btn_registrar.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_registro))
win.btn_registrar.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_registro))
win.btn_atrasRegistro.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_inicio))
win.btn_registrarse.clicked.connect(lambda: usuarios.login.registrarUsuario(win.text_usuarioRegistro.text(),win.text_passwordRegistro.text()))
win.btn_iniciarSesion.clicked.connect(lambda: autenficarUsuario(win.text_usuario.text(),win.text_password.text()))

win.btn_crearRepoPrincipal.clicked.connect(lambda:carpeta.carpeta.crearCapeta())
win.btn_crearRepoUser.clicked.connect(lambda:carpeta.carpeta.crearCapetaUsuario(win.text_usuario.text()))

win.btn_administrarCarpetasUser.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_administrarCarpetasUser))
win.btn_commit.clicked.connect(lambda:carpeta.carpeta.commit(win.text_usuario.text()))
win.show()

sys.exit(app.exec())

