import os
os.system('cls')

class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} es una {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto.")

    def establecer_clientes_atendidos(self, NuevosClientes):
        self.clientes_atendidos = NuevosClientes
        print(f"Clientes atendidos establecidos a: {self.clientes_atendidos}")

    def incrementar_clientes_atendidos(self, clientes_adicionales):
        self.clientes_atendidos += clientes_adicionales
        print(f"Clientes atendidos establecidos a: {self.clientes_atendidos}")