import os
os.system('cls')

from copia_30_3_2 import Administrador, Privilegios

privilegios = [
    "Puede eliminar publicaciones",
    "Puede bloquear usuarios",
    "Puede agregar publicaciones"
]

admin = Administrador("Arthur", "Mitchell", 67, "Miami", privilegios)

admin.privilegios.mostrar_privilegios()