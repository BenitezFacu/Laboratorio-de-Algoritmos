import os
os.system('cls')

class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
        self.Login = 0 

    def describirUsuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido:{self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"ciudad: {self.ciudad}")

    def saludar_usuario(self):
        print(f"Bienvenido a tu perfil {self.nombre}.")

    def incrementar_intentos_login(self):
        self.Login += 1
        print(f"Logins hechos: {self.Login}")

    def reiniciar_intentos_login(self):
        self.Login = 0
        print(f"Logins reiniciados a: {self.Login}")


usuario_1 = Usuario("Franco", "Chichizola", 19, "Montevideo")

usuario_1.incrementar_intentos_login()
usuario_1.incrementar_intentos_login()

print(f"Intentos de login: {usuario_1.Login}")

usuario_1.reiniciar_intentos_login()
print(f"Intentos de login: {usuario_1.Login}")