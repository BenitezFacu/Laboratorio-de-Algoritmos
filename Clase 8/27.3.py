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

usuario_1 = Usuario("Joaquin", "Piñeiro", 27, "Buenos Aires")
usuario_2 = Usuario("Franco", "Chichizola", 19, "Montevideo")
usuario_3 = Usuario("Leo", "Borgo", 42, "Barcelona")

usuario_1.saludar_usuario()
usuario_1.describir_usuario()

usuario_2.saludar_usuario()
usuario_2.describir_usuario()

usuario_3.saludar_usuario()
usuario_3.describir_usuario()