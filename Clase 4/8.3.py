import os
os.system('cls')

lista = []

for a in range (3):
    personas = input("Ingrese el nombre de una persona que te gustaría invitar a cenar: ")
    lista.append(personas)

print(lista)

print("Hay una mesa más grade y ahora puedes elegir a 3 nuevos invitados")

for a in range (3):
    personas = input("Ingrese el nombre de una persona que te gustaría invitar a cenar: ")
    if a == 0:
        lista.insert(0, personas)
    elif a == 1:
        lista.insert(3, personas)
    else:
        lista.append(personas)

print(lista)

eleccion = int(input("A quien queres mandarle un mensaje (1/2/3/4/5/6): "))

print(f"Hola {lista[eleccion - 1]}, te gustaría venir a comer?")