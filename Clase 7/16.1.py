import os
os.system('cls')

diccionario = {"módulo" : "Los módulos permiten organizar y reutilizar código, lo que facilita el mantenimiento y mejora el rendimiento de los programas",
               "*" : "Sirve para multiplicar",
               "diccionario" : "Los diccionarios son una estructura de datos que permiten almacenar pares de claves y valores",
               "==" : "Permite comparar si las variables introducidas a su izquierda y derecha son iguales",
               "#" : "Se usa para hacer comentarios en Python, escribiendo este símbolo al inicio de cada línea que se quiera comentar"}

for a in diccionario:
    print(f"{a} : {diccionario[a]} \n")