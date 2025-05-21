import os
os.system('cls')

with open("Clase 8\pi_millon.txt", "r") as file:
    numeros = file.read()

fecha = input("Ingresa tu cumpleaños, en la forma ddmmaa: ")

if fecha in numeros:
    print("Tu cumpleaños aparece en los primeros un millón dígitos de pi")
else:
    print("Tu cumpleaños no aparece en los primeros un millón dígitos de pi")