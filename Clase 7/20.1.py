import os
os.system('cls')

pedidos_sandwiches = ["sandwich de milanesa", "sandwich completo", "sandwich de j/q"]

sandwiches_terminados = []

for a in pedidos_sandwiches:
    print(f"Preparé tu {a}")
    sandwiches_terminados.append(a)

print(sandwiches_terminados)