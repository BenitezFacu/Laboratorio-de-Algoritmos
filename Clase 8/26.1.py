import os
os.system('cls')

from printing_functions import imprimir_modelos, mostrar_modelos_completados

diseños_no_imprimidos = ['rojo', 'azul', 'verde']
modelos_completados = []

imprimir_modelos(diseños_no_imprimidos, modelos_completados)
mostrar_modelos_completados(modelos_completados)