import os
os.system('cls')

while True:
    edad = int(input("Ingrese su edad: "))
    if edad < 3:
        print("La entrada es gratis")
    elif edad < 12:
        print("La entrada cuesta 10$")
    else:
        print("La entrada cuesta 15$")