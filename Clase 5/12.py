import os
os.system('cls')

pizzas = ["Muzzarella", "Fugazzetta", "Napolitana"]

pizzas_amigos = ["Muzzarella", "Fugazzetta", "Napolitana"]

for a in range(2):
    if a < 1:
        pregunta = input("Agrega una nueva pizza: ")
        pizzas.append(pregunta)
    else:
        pregunta_2 = input("Agrega una nueva pizza: ")
        pizzas_amigos.append(pregunta_2)

for a in range(4):
    print(f"Mis pizzas favoritas son: {pizzas[a]}")

for a in range(4):
    print(f"Laz pizzas favoritas de mi amigo/a son: {pizzas_amigos[a]}")

print(pizzas)
print(pizzas_amigos)