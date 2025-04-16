import os
os.system('cls')

lugares_favoritos = {
    "Mateo" : "Berlín",
    "Joaco" : "París",
    "Franco" : "Venecia"
}

for a in lugares_favoritos:
    print(f"{a} : {lugares_favoritos[a]}")