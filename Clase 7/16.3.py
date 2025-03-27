import os
os.system('cls')

lenguajes = {'Juan': 'python', 
            'Sara': 'c', 
            'Eduardo': 'rust',
            'Agustina': 'c#'}
personas = ["Mateo", "Juan", "Eduardo", "Marcos", "Emma"]

for a in personas:
    if a in lenguajes:
        print(f"Gracias por responder la encuesta, {a}")
    if a not in lenguajes:
        print(f"Hola {a}, responde la encuesta")
