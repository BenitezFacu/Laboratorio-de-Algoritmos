import os
os.system('cls')

class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} es una {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

restaurante_1 = Restaurante("Big pizza", "pizzería")
restaurante_2 = Restaurante("Mostaza", "cadena de comida rápida")
restaurante_3 = Restaurante("Mcdonald's", "cadena de comida rápida")

restaurante_1.describir_restaurante()
restaurante_2.describir_restaurante()
restaurante_3.describir_restaurante()