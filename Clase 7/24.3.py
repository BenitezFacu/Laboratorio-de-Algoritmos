import os
os.system('cls')

lista  = ["a", "b", "c", "d", "e",]
mensajes_enviados = []

def mostrar_mensajes(lista_copia):
    for a in lista_copia:
        print(a)
        mensajes_enviados.append(a)

mostrar_mensajes(lista[:])
print(lista)
print(mensajes_enviados)