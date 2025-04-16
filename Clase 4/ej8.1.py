import os
os.system('cls')

lista = []

for a in range(3):
    personas = input("Ingrese el nombre de alguna persona: ")
    lista.append(personas)

elección = int(input("Con cual de los tres quisieras hablar (1/2/3): "))

print(f"Hola {lista[elección - 1]}")