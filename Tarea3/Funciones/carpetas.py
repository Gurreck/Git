import os
import sys
class carpeta:
    def crearCapeta():
        directorio = 'repositorio'
        print("crenado")
        try:
            print("Se creo el repositorio")
            os.mkdir(directorio)
            print("Se creo el repositorio")
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio)