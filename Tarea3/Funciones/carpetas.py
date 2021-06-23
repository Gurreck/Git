from PyQt5 import QtWidgets, uic,QtGui
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import Funciones.Mensajes as sms
from os import remove
import os
import sys
import shutil
import Funciones.login as log
class carpeta():
    
    def crearCapetaUsuario(self,nombre):
        directorio = 'repositorio/'+nombre
        directorio_permanente = directorio+"/permanente"
        directorio_temporal = directorio+"/temporal"
        print("crenado")
        try:
            os.mkdir(directorio)
            os.mkdir(directorio_permanente)
            os.mkdir(directorio_temporal)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio+" y sus carpetas hijas")
    
    def llenarTabla(self,table,nombre):
        #contenidos=os.listdir(directorio_temporal)
        directorio_temporal = 'repositorio/'+nombre+'/temporal'
        contenidos=os.listdir(directorio_temporal)
        us = 0
        for elemento in contenidos:
            table.setItem(us,0, QTableWidgetItem(contenidos[us]))
            us += 1
        #table.currentItemChanged.connect(self.seleccionar(table))
    
    def eliminarFila(self,table,nombre):

        filaSeleccionada = table.selectedItems()
        directorio_temporal = 'repositorio/'+nombre+'/temporal'
        contenidos = os.listdir(directorio_temporal)

        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            print(fila)
            table.removeRow(fila)
            remove('repositorio/'+nombre+'/temporal/'+contenidos[fila])
            table.clearSelection()
        else:
            sms.MessageBox(QtWidgets.QWidget).show_message(1,'Error','Selecciones un archivo a eliminar')
    def crearCarpeta(self,directorio):
        try:
            os.mkdir(directorio)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio)
    def commit(self,nombre):
        print("entro")
        directorio_temporal = 'repositorio/'+nombre+'/temporal'
        print(directorio_temporal)
        log.login.actualizarNumeroCommit(nombre)
        directorio_permanente = 'repositorio/'+nombre+'/permanente/commit'+str(log.login.verificaNumeroCommit(nombre))
        self.crearCarpeta(self,directorio_permanente)
        print(directorio_permanente)
        contenidos=os.listdir(directorio_temporal)
        for elemento in contenidos:
            try:
                print(f"Copiando {elemento} --> {directorio_permanente} ... ", end="")
                src = os.path.join(directorio_temporal, elemento) # origen
                dst = os.path.join(directorio_permanente, elemento) # destino
                shutil.copy(src, dst)
                print("Correcto")
            except:
                print("Falló")
                print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")
    def cargarArchivo(nombre, direccion_origen,table):
        print("entro")
        directorio_temporal = 'repositorio/'+nombre+'/temporal'
        try:
            shutil.copy(direccion_origen, directorio_temporal)
            contenidos = os.listdir(directorio_temporal)
            table.clearContents()
            us = 0
            for elemento in contenidos:
               table.setItem(us,0, QTableWidgetItem(contenidos[us]))
               us += 1
               print("Correcto")
        except:
            print("Falló")
            print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")