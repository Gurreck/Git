import json
import sys
import Funciones.Mensajes as sms
from PyQt5 import QtWidgets
import os
data = {}
data['usuarios'] = []
class login:
    def leerUsuarios():
        with open('Usuarios/usuarios.txt') as file:
           global data
           data = json.load(file)

    def registrarUsuario(nombre, password):
        bandera = True
        if nombre and password:
            global data
            data['usuarios'].append({
                'nombre' : nombre,
                'password': password,
                'numero': 0,
                'creado': 'No'
            })
            with open('Usuarios/usuarios.txt') as file:
                info = json.load(file)
                for usuario in info['usuarios']:
                    if(usuario['nombre'] == nombre):
                        bandera = False

            if bandera == True:   
                with open('Usuarios/usuarios.txt', 'w') as outfile:          
                   outfile.write(json.dumps(data))
                   sms.MessageBox(QtWidgets.QWidget).show_message(2,'Registro','Usuario registrado con exito')
            else:
                sms.MessageBox(QtWidgets.QWidget).show_message(1,'Error','Lo sentimos, ya existe un usuario registrado con ese nombre')