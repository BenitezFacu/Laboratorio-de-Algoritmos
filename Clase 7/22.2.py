import os
os.system('cls')

def hacer_camiseta(tamaño = "grande", texto = "me encanta python"):
    print(f"El tamaño de tu camiseta es {tamaño}")
    print(f"El mensaje de tu camiseta es {texto}")

hacer_camiseta()
hacer_camiseta(tamaño = "mediano")
hacer_camiseta(tamaño = "pequeña", texto = "solari")