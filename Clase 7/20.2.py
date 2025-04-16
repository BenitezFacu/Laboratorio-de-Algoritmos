import os
os.system('cls')

pedidos_sandwiches = ["sandwich de milanesa", "sandwich de pastrón", "sandwich de pastrón", "sandwich de pastrón"]

print("La sanguchería se quedó sin sanguches de pastrón")

for a in range(2):
    for b in pedidos_sandwiches:
        if b == "sandwich de pastrón":
            pedidos_sandwiches.remove(b)
print(pedidos_sandwiches)