import os
os.system('cls')

import os
os.system('cls')

def construir_perfil(nombre, apellido, **info_usuario):
    perfil = {}
    perfil["nombre"] = nombre
    perfil["apellido"] = apellido
    
    for clave, valor in info_usuario.items():
        perfil[clave] = valor
    
    return perfil

perfil_usuario = construir_perfil(
    "Tu Nombre", "Tu Apellido", 
    edad=25, ciudad="Buenos Aires", profesion="Programador"
)

print(perfil_usuario)
