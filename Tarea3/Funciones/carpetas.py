import os
class carpeta:
    def crearCapeta():
        directorio = "/repositorio"
        try:
            os.mkdir(directorio)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio)