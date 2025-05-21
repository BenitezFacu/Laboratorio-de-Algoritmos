import os
os.system('cls')

class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

    def describir_usuario(self):
        print(f"nombre: {self.nombre}")
        print(f"apellido: {self.apellido}")
        print(f"edad: {self.edad}")
        print(f"ciudad: {self.ciudad}")

    def saludar_usuario(self):
        print(f"Bienvenido a tu perfil {self.nombre}.")

class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad, ciudad, privilegios):
        super().__init__(nombre, apellido, edad, ciudad)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(privilegios)

privilegios = [
    "Puede eliminar publicaciones",
    "Puede bloquear usuarios",
    "Puede agregar publicaciones"
]

admin = Administrador("Hector", "Estrada", 32, "Buenos Aires", privilegios)

admin.mostrar_privilegios()