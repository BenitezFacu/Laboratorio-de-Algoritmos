import os
os.system('cls')


Pepe = {
    "nombre" : "Pepe",
    "apellido" : "Marquez",
    "edad" : 11,
    "ciudad": "Lima",
}
Mateo = {
    "nombre" : "Mateo",
    "apellido" : "De lucca",
    "edad" : 27,
    "ciudad": "Asunción",
}
Jose = {
    "nombre" : "Jose",
    "apellido" : "Antonio",
    "edad" : 99,
    "ciudad": "Emergilda",
}
personas =[Pepe,Mateo,Jose]
for persona in personas:
    print(persona)