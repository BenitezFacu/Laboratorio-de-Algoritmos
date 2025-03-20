import os
os.system('cls')

lista = []

for a in range (3):
    personas = input("Ingrese el nombre de una persona que te gustaría invitar a cenar: ")
    lista.append(personas)

print("Hay una mesa más grade y ahora puedes elegir a 3 nuevos invitados")

print(lista)

for a in range (3):
    nuevos = input("Ingrese el nombre de una persona que te gustaría invitar a cenar: ")
    if a == 0:
        lista.insert(0, nuevos)
    elif a == 1:
        lista.insert(3, nuevos)
    else:
        lista.append(nuevos)

print(lista)

print("Solo podes invitar a dos personas a la cena")

for a in range(4):
    print(f"{lista[5 - a]}, no puede venir a la cena ")
    lista.pop(5 - a)

print(lista)

for a in range(2):
    print(f"Hola {lista[a]}, siguen invitados a la cena")

del lista

lista = []

print(lista)