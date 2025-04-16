import os
os.system('cls')

ciudades = {
    "Berlín": {
        "País" : "Alemania",
        "Población" : "3.4 millones",
        "Dato" : "El muro de berlín no era vertical"
    },
    "París" : {
        "País" : "Francia",
        "Población" : "2.1 millones",
        "Dato" : "Francia es el país más visitado del mundo"
    },
    "Venecia" : {
        "País" : "Italia",
        "Población" : "254 mil",
        "Dato" : "Venecia se construyó sobre el agua para estabilizar el suelo pantanoso"
    }
}

for info in ciudades.items():
    print(info)
