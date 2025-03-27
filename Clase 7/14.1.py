import os
os.system('cls')

lista = ["a","b","c","d","admin"]

for a in lista:
    if a != "admin":
        print(f"Hola {a}")
    else:
        print("Hola admin, ¿querés ver un informe de estado?")