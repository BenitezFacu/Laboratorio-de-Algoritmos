import os
os.system('cls')

lista  = ["a", "b", "c", "d", "e",]
mensajes_enviados = []

def mostrar_mensajes():
    for a in lista[:]:
        print(a)
        mensajes_enviados.append(a)
        a = lista.pop()

mostrar_mensajes()
print(lista)
print(mensajes_enviados)