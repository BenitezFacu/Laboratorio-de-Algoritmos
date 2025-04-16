import os
os.system('cls')

def sandwich(*a):
    print("El sándwich está siendo preparado con los siguientes ingredientes:")
    for b in a:
        print(b)

ingrediente = input("Ingrese un ingrediente: ")
ingrediente_2 = input("Ingrese un ingrediente: ")
ingrediente_3 = input("Ingrese un ingrediente: ")
ingrediente_4 = input("Ingrese un ingrediente: ")
ingrediente_5 = input("Ingrese un ingrediente: ")
ingrediente_6 = input("Ingrese un ingrediente: ")

sandwich(ingrediente)
sandwich(ingrediente_2, ingrediente_3)
sandwich(ingrediente_4, ingrediente_5, ingrediente_6)