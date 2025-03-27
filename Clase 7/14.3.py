import os
os.system('cls')

usuarios_actuales = ["A", "B", "C", "D", "E"]
usuarios_nuevos = ["a", "b", "f", "g", "h"]
usuarios_actuales = [usuario.lower() for usuario in usuarios_actuales]

for usuario in usuarios_nuevos:
    if usuario.lower() in usuarios_actuales:
        print(f"{usuario} ese nombre ya está en uso, pruebe con otro")
    else:
        print(f"Hola {usuario}, el nombre está disponible")