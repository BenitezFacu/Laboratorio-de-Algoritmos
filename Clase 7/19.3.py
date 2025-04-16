import os
os.system('cls')

contador = 1

while contador == 1:
    ingredientes = input("Ingrese un ingrediente para su pizza (para terminar ingrese salir): ")
    if ingredientes != "salir":
        print(f"Se ingreso {ingredientes}, a tu pizza")
    elif ingredientes == "salir":
        break
