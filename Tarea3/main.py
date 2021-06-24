from PyQt5 import QtWidgets, uic

import sys
import Funciones.login as usuarios
from Funciones.carpetas import carpeta
from Funciones.permisos import permiso
import json
import Funciones.Mensajes as sms
import Funciones.carpetas as carp
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import Funciones.moverArchivo as archivo
app = QtWidgets.QApplication([])

win = uic.loadUi("View/Inicio.ui")
usuarios.login.leerUsuarios()

banderaAutenticado = False
def verificarCreacionRepositorio(nombre):
    bandera = False
    with open('Usuarios/usuarios.txt') as file:
        data = json.load(file)
        for usuario in data['usuarios']:
            if(usuario['nombre']==nombre and usuario['creado'] == 'Si'):
                bandera = True
        if(bandera==True):
            global win
            
            if(nombre == 'admin'):
                win.btn_crearRepoPrincipal.hide()
            else:
                win.btn_crearRepoUser.hide()
            win.btn_administrarRepositorioUser.show()
        else:
            win.btn_administrarRepositorioUser.hide()
            
    
def autenficarUsuario(nombre, password):
    with open('Usuarios/usuarios.txt') as file:
        data = json.load(file)
        for usuario in data['usuarios']:
            if(usuario['nombre']==nombre and usuario['password']==password):
                global win
                verificarCreacionRepositorio(nombre)
                if(nombre == 'admin'):
                    win.stackedWidget.setCurrentWidget(win.page_adminCreaRepo)
                else:
                    win.stackedWidget.setCurrentWidget(win.page_userCreaRepo)
                print("Autenticado")
                global banderaAutenticado
                banderaAutenticado= True
                break
        if(banderaAutenticado == False):
            sms.MessageBox(QtWidgets.QWidget).show_message(1,'Error','Usuario o contraseña incorrectos')

def validarPermisos():
    global tipoPermiso
    if(win.check_lectura.isChecked()):
        tipoPermiso = 'lectura'
    if(win.check_escritura.isChecked()):
        tipoPermiso = 'escritura'

win.btn_registrar.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_registro))
win.btn_registrar.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_registro))
win.btn_atrasRegistro.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_inicio))
win.btn_registrarse.clicked.connect(lambda: usuarios.login.registrarUsuario(win.text_usuarioRegistro.text(),win.text_passwordRegistro.text()))
win.btn_iniciarSesion.clicked.connect(lambda: autenficarUsuario(win.text_usuario.text(),win.text_password.text()))

#Botones de atras ventanas
win.btn_atrasOpcionesAdmin.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_inicio))
win.btn_atrasOpcionesUser.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_inicio))
win.btn_atrasCarpetas.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_userCreaRepo))
win.btn_atrasCarpetas.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_userCreaRepo))
win.btn_atrasAdminCarp.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_carpetas))


win.btn_crearRepoPrincipal.clicked.connect(lambda:carpeta(win).crearCapeta())
win.btn_crearRepoUser.clicked.connect(lambda:carpeta.crearCapetaUsuario(carpeta,win.text_usuario.text()))
win.btn_crearRepoUser.clicked.connect(lambda:usuarios.login.actualizarUsuarios(win.text_usuario.text()))
win.btn_crearRepoUser.clicked.connect(lambda: win.btn_crearRepoUser.hide())
win.btn_crearRepoUser.clicked.connect(lambda: win.btn_administrarRepositorioUser.show())
#win.btn_crearRepoUser.clicked.connect(lambda: win.administrarRepositorioUser)

win.btn_eliminarArchivo.clicked.connect(lambda:carpeta.eliminarFila(carpeta,win.tbContenido,win.tbCarpetas))

win.btn_administrarRepositorioUser.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_carpetas))
win.btn_administrarRepositorioUser.clicked.connect(lambda: carpeta.llenarTablaCarpetas(carpeta,win.tbCarpetas,win.text_usuario.text()))

win.btn_AdministrarCarpeta.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_administrarCarpetasUser))
win.btn_AdministrarCarpeta.clicked.connect(lambda: carpeta.llenarTabla(carpeta,win.tbContenido,win.text_usuario.text(),win.tbCarpetas))


win.btn_commit.clicked.connect(lambda:carpeta.commit(carpeta,win.text_usuario.text()))
win.btn_agregarArchivo.clicked.connect(lambda: archivo.App(win).getFileName(carp.carpSelect,win.tbContenido))

#PERMISOS

win.check_lectura.toggled.connect(lambda: validarPermisos())
win.check_escritura.toggled.connect(lambda: validarPermisos())
win.btn_asignarPermisos.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_asignarPermisosUser))
win.btn_atrasPermisos.clicked.connect(lambda: win.stackedWidget.setCurrentWidget(win.page_administrarCarpetasUser))
win.btn_crearPermiso.clicked.connect(lambda:permiso.registrarPermiso(carp.carpSelect, win.text_usuarioPermiso.text(),tipoPermiso))

win.show() 

sys.exit(app.exec())

