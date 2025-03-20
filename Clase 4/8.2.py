import os, random
os.system('cls')

lista = []

for a in range (3):
    personas = input("Ingrese el nombre de una persona que te gustaría invitar a cenar: ")
    lista.append(personas)

print(lista)

print(f"{lista[1]}, no puede venir a la fiesta")
lista.pop(1)

nuevo = input("Ingrese el nombre de otro invitado: ")
lista.append(nuevo)

print(lista)

eleccion = int(input("A quien queres mandarle un mensaje (1/2/3): "))

print(f"Hola {lista[eleccion - 1]}, te gustaría venir a comer?")