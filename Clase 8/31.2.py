import os, random
os.system('cls')

lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "b", "c", "d", "e"]

a = (random.sample(lista, 4))

print(f"Cualquiera que tenga estos 4 números o letras gana un premio, {a}")