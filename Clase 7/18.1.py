import os
os.system('cls')

personas = int(input("Cuantas personas hay en tu grupo para cenar: "))

if personas > 8:
    print("Vas a tener que esperar por una mesa")
else:
    print("Tu mesa está lista")