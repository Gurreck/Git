import json
import sys
import Funciones.Mensajes as sms
from PyQt5 import QtWidgets
data = {}
data['usuarios'] = []
class login:
    def leerUsuarios():
        with open('Usuarios/usuarios.txt') as file:
           global data
           data = json.load(file)

    def registrarUsuario(nombre, password):
        if nombre and password:
            global data
            data['usuarios'].append({
                'nombre' : nombre,
                'password': password
            })
            with open('Usuarios/usuarios.txt', 'w') as outfile:
                outfile.write(json.dumps(data))
            sms.MessageBox(QtWidgets.QWidget).show_message(2)
    def autenficarUsuario(nombre, password):
        with open('Usuarios/usuarios.txt') as file:
            data = json.load(file)
            for usuario in data['usuarios']:
                if(usuario['nombre']==nombre and usuario['password']==password):
                    print("Autenticado")
                    break
                else:
                    print("No autenticado")