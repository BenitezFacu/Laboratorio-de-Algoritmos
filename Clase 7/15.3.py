import os
os.system('cls')

diccionario = {"lista" : "sirve para guardar valores",
               "valores" : "sirve para guardar algún dato",
               "+" : "sirve para sumar",
               "-" : "sirve para restar",
               "/" : "sirve para dividir"}

for a in diccionario:
    print(f"{a}: {diccionario[a]}\n")