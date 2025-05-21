import os
os.system('cls')

with open("Clase 8\learning_python.txt", "r") as file:
    lineas = file.readlines()
    print("Archivo línea por línea: ")
    for linea in lineas:
        print(linea.strip())

with open("Clase 8\learning_python.txt", "r") as file:
    print("Archivo con cambio: ")
    for linea in lineas:
        print(linea.replace("Python", "C").strip())