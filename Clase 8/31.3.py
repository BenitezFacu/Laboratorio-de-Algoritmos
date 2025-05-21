import os, random
os.system('cls')

lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "b", "c", "d", "e"]
my_ticket = ["1", "2", "3", "4"]

contador = 0

while True:
    ganador = random.sample(lista, 4)
    contador += 1
    if my_ticket == ganador:
        break

print(f"El bucle tuvo que ejecutarse {contador} veces")