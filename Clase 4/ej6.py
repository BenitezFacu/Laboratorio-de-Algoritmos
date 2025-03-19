import os
os.system('cls')

lista = ["BMX", "Urbana", "Plegable", "De montana"]

print(lista)

pregunta = int(input("Cual fue tu primer bicicleta (1/2/3/4): "))

print(f"Tu primer bicicleta fue de: {lista[pregunta - 1]}")