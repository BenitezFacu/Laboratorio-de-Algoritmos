import os
os.system('cls')

class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} es una {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} esta abierto.")

    def establecer_clientes_atendidos(self, NuevosClientes):
        self.clientes_atendidos = NuevosClientes
        print(f"Clientes atendidos establecidos a: {self.clientes_atendidos}")

    def incrementar_clientes_atendidos(self, clientes_adicionales):
        self.clientes_atendidos += clientes_adicionales
        print(f"Clientes atendidos incrementados. Ahora son: {self.clientes_atendidos}")

restaurante = Restaurante("Big pizza", "Pizzería")

print(f"Clientes atendidos al inicio: {restaurante.clientes_atendidos}")
restaurante.clientes_atendidos = 50
print(f"Clientes atendidos después de modificar: {restaurante.clientes_atendidos}")
restaurante.establecer_clientes_atendidos(100)
restaurante.incrementar_clientes_atendidos(30)