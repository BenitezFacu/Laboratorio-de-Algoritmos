import os
os.system('cls')

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(f"Tu nombre es: {nombre.capitalize()}")
print(f"Tu apellido es: {apellido.casefold()}")

#El capitalize() produce que la primera letra del string que introdujiste sea mayúscula
#El casefold() produce que toda el string ingresado este en minúsculaa