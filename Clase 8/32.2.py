import os
os.system('cls')

with open("Clase 8\learning_python.txt", "r") as file:
    contenido = file.read()
    print("Archivo de una sola vez: ")
    print(contenido)

with open("Clase 8\learning_python.txt", "r") as file:
    lineas = file.readlines()
    print("Archivo línea por línea: ")
    for linea in lineas:
        print(linea.strip())