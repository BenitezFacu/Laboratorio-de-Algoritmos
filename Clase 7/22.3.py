import os
os.system('cls')

def describir_ciudad(ciudad, pais = "españa"):
    print(f"{ciudad} está en {pais}")

describir_ciudad(ciudad = "Madrid")
describir_ciudad(ciudad = "Barcelona")
describir_ciudad(ciudad = "Buenos Aires", pais = "Argentina")