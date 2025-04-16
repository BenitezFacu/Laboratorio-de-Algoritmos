import os
os.system('cls')

lista = []

for a in range(5):
    pregunta = input("Ingrese un lugar al cual le gustaría ir: ")
    lista.append(pregunta)

for a in range(5):
    print(f"{lista[a]}")