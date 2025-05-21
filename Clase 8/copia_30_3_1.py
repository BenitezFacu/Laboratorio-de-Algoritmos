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