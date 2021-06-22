import os
import sys
import shutil
import Funciones.login as log
class carpeta:
    
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
    def cargarArchivo(nombre, direccion_origen):
        print("entro")
        directorio_temporal = 'repositorio/'+nombre+'/temporal'
        try:
            shutil.copy(direccion_origen, directorio_temporal)
            print("Correcto")
        except:
            print("Falló")
            print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")