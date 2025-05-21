import os
os.system('cls')

from copia_30_3_1 import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad, ciudad, privilegios):
        super().__init__(nombre, apellido, edad, ciudad)
        self.privilegios = Privilegios(privilegios)

class Privilegios():
    def __init__(self, privilegios):
        self.privilegios = privilegios
    
    def mostrar_privilegios(self):
        print(privilegios)

privilegios = [
    "Puede eliminar publicaciones",
    "Puede bloquear usuarios",
    "Puede agregar publicaciones"
]