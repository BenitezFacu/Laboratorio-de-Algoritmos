import os
os.system('cls')

class restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} es una {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto.")

class puesto_de_helados(restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores de helado disponibles:")
        print(self.sabores)


puesto = puesto_de_helados("La Nona", "Heladería", ["Vainilla","Chocolate","Dulce de leche", "Granizado"])
puesto.mostrar_sabores()