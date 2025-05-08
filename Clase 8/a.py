#28.1
class Restaurante:
    def __init__(self, NombreRestaurante, TipoCocina):
        self.NombreRestaurante = NombreRestaurante
        self.TipoCocina = TipoCocina
        self.ClientesAtendidos = 0  

    def DescribirRestaurante(self):
        print(f"Restaurante: {self.NombreRestaurante}")
        print(f"Tipo de Cocina: {self.TipoCocina}")

    def AbrirRestaurante(self):
        print(f"El restaurante {self.NombreRestaurante} está abierto.")

    def EstablecerClientesAtendidos(self, NuevosClientes):
        self.ClientesAtendidos = NuevosClientes
        print(f"Clientes atendidos establecidos a: {self.ClientesAtendidos}")

    def IncrementarClientesAtendidos(self, ClientesAdicionales):
        self.ClientesAtendidos += ClientesAdicionales
        print(f"Clientes atendidos incrementados. Ahora son: {self.ClientesAtendidos}")

restaurante = Restaurante("La Parrilla de Juan", "Cocina Argentina")
print(f"Clientes atendidos al inicio: {restaurante.ClientesAtendidos}")
restaurante.ClientesAtendidos = 50
print(f"Clientes atendidos después de modificar: {restaurante.ClientesAtendidos}")
restaurante.EstablecerClientesAtendidos(100)
restaurante.IncrementarClientesAtendidos(30)

#28.2
class Usuario:
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.CorreoElectronico = CorreoElectronico
        self.Ciudad = Ciudad
        self.IntentosLogin = 0 

    def DescribirUsuario(self):
        print(f"Nombre: {self.Nombre} {self.Apellido}")
        print(f"Edad: {self.Edad}")
        print(f"Correo Electrónico: {self.CorreoElectronico}")
        print(f"Ciudad: {self.Ciudad}")

    def SaludarUsuario(self):
        print(f"¡Hola, {self.Nombre}! Bienvenido a tu perfil.")

    def IncrementarIntentosLogin(self):
        self.IntentosLogin += 1
        print(f"Intentos de login incrementados. Ahora son: {self.IntentosLogin}")

    def ReiniciarIntentosLogin(self):
        self.IntentosLogin = 0
        print(f"Intentos de login reiniciados. Ahora son: {self.IntentosLogin}")

usuario1 = Usuario("Juan", "Perez", 35, "juan@email.com", "Lima")

usuario1.IncrementarIntentosLogin()
usuario1.IncrementarIntentosLogin()
usuario1.IncrementarIntentosLogin()

print(f"Intentos de login después de incrementos: {usuario1.IntentosLogin}")

usuario1.ReiniciarIntentosLogin()
print(f"Intentos de login después de reiniciar: {usuario1.IntentosLogin}")

#29.1
class Restaurante:
    def __init__(self, NombreRestaurante, TipoCocina):
        self.NombreRestaurante = NombreRestaurante
        self.TipoCocina = TipoCocina
        self.ClientesAtendidos = 0

    def DescribirRestaurante(self):
        print(f"Restaurante: {self.NombreRestaurante}")
        print(f"Tipo de Cocina: {self.TipoCocina}")

    def AbrirRestaurante(self):
        print(f"El restaurante {self.NombreRestaurante} está abierto.")

    def EstablecerClientesAtendidos(self, NuevosClientes):
        self.ClientesAtendidos = NuevosClientes
        print(f"Clientes atendidos establecidos a: {self.ClientesAtendidos}")

    def IncrementarClientesAtendidos(self, ClientesAdicionales):
        self.ClientesAtendidos += ClientesAdicionales
        print(
            f"Clientes atendidos incrementados. Ahora son: {self.ClientesAtendidos}")


class PuestoDeHelados(Restaurante):
    def __init__(self, NombreRestaurante, TipoCocina, Sabores):
        super().__init__(NombreRestaurante, TipoCocina)
        self.Sabores = Sabores

    def MostrarSabores(self):
        print("Sabores de helado disponibles:")
        for sabor in self.Sabores:
            print(f"- {sabor}")


Puesto = PuestoDeHelados("Helados de la Abuela", "Heladería", [
                         "Vainilla", "Chocolate", "Fresa", "Menta", "Café"])
Puesto.MostrarSabores()

#29.2
class Restaurante:
    def __init__(self, NombreRestaurante, TipoCocina):
        self.NombreRestaurante = NombreRestaurante
        self.TipoCocina = TipoCocina
        self.ClientesAtendidos = 0

    def DescribirRestaurante(self):
        print(f"Restaurante: {self.NombreRestaurante}")
        print(f"Tipo de Cocina: {self.TipoCocina}")

    def AbrirRestaurante(self):
        print(f"El restaurante {self.NombreRestaurante} está abierto.")

    def EstablecerClientesAtendidos(self, NuevosClientes):
        self.ClientesAtendidos = NuevosClientes
        print(f"Clientes atendidos establecidos a: {self.ClientesAtendidos}")

    def IncrementarClientesAtendidos(self, ClientesAdicionales):
        self.ClientesAtendidos += ClientesAdicionales
        print(
            f"Clientes atendidos incrementados. Ahora son: {self.ClientesAtendidos}")


class PuestoDeHelados(Restaurante):
    def __init__(self, NombreRestaurante, TipoCocina, Sabores):
        super().__init__(NombreRestaurante, TipoCocina)
        self.Sabores = Sabores

    def MostrarSabores(self):
        print("Sabores de helado disponibles:")
        for sabor in self.Sabores:
            print(f"- {sabor}")


Puesto = PuestoDeHelados("Helados de la Abuela", "Heladería", [
                         "Vainilla", "Chocolate", "Fresa", "Menta", "Café"])
Puesto.MostrarSabores()

#29.3
class Usuario:
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.CorreoElectronico = CorreoElectronico
        self.Ciudad = Ciudad
        self.IntentosLogin = 0

    def DescribirUsuario(self):
        print(f"Nombre: {self.Nombre} {self.Apellido}")
        print(f"Edad: {self.Edad}")
        print(f"Correo Electrónico: {self.CorreoElectronico}")
        print(f"Ciudad: {self.Ciudad}")

    def SaludarUsuario(self):
        print(f"¡Hola, {self.Nombre}! Bienvenido a tu perfil.")

    def IncrementarIntentosLogin(self):
        self.IntentosLogin += 1
        print(
            f"Intentos de login incrementados. Ahora son: {self.IntentosLogin}")

    def ReiniciarIntentosLogin(self):
        self.IntentosLogin = 0
        print(
            f"Intentos de login reiniciados. Ahora son: {self.IntentosLogin}")


class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def MostrarPrivilegios(self):
        print(f"Privilegios:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


class Administrador(Usuario):
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad, Privilegios):
        super().__init__(Nombre, Apellido, Edad, CorreoElectronico, Ciudad)
        self.Privilegios = Privilegios

    def MostrarPrivilegios(self):
        self.Privilegios.MostrarPrivilegios()


privilegios_admin = Privilegios([
    "Puede Agregar Publicaciones",
    "Puede Eliminar Publicaciones",
    "Puede Bloquear Usuarios",
    "Puede Editar Publicaciones",
    "Puede Ver Estadísticas",
    "Puede Gestionar Comentarios",
    "Puede Agregar Imágenes",
    "Puede Modificar Perfil",
    "Puede Ver Perfil De Otros Usuarios",
    "Puede Enviar Mensajes Privados"
])

Admin = Administrador("Santino", "Rodriguez", 16,
                      "santinorofu@gmail.com", "CABA", privilegios_admin)

Admin.MostrarPrivilegios()

#29.4
class Bateria:
    def __init__(self, capacidad_bateria=40):
        self.capacidad_bateria = capacidad_bateria

    def describir_bateria(self):
        print(f"Este auto tiene una batería de {self.capacidad_bateria} kWh.")

    def obtener_autonomia(self):
        if self.capacidad_bateria == 40:
            rango = 150
        elif self.capacidad_bateria == 65:
            rango = 225
        print(f"Este auto tiene una autonomía de {rango} kilómetros.")

    def actualizar_bateria(self):
        if self.capacidad_bateria != 65:
            print("Actualizando la batería a 65 kWh...")
            self.capacidad_bateria = 65
        else:
            print("La batería ya tiene el tamaño máximo de 65 kWh.")


class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_nombre_descriptivo(self):
        return f"{self.marca} {self.modelo} {self.año}"


class AutoElectrico(Auto):

    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()


mi_leaf = AutoElectrico('Nissan', 'Leaf', 2024)

print(mi_leaf.obtener_nombre_descriptivo())

mi_leaf.bateria.describir_bateria()
mi_leaf.bateria.obtener_autonomia()
mi_leaf.bateria.actualizar_bateria()
mi_leaf.bateria.obtener_autonomia()

#30.1
from Ejercicio_30_1_Extension import Restaurante
mi_restaurante = Restaurante("La Pizzería de Juan", "Cocina Italiana")
mi_restaurante.DescribirRestaurante()

#30.2
from Ejercicio_30_2_Extension import Administrador, Privilegios

privilegios_admin = Privilegios([
    "Puede Agregar Publicaciones",
    "Puede Eliminar Publicaciones",
    "Puede Bloquear Usuarios",
    "Puede Editar Publicaciones",
    "Puede Ver Estadísticas",
    "Puede Gestionar Comentarios",
    "Puede Agregar Imágenes",
    "Puede Modificar Perfil",
    "Puede Ver Perfil De Otros Usuarios",
    "Puede Enviar Mensajes Privados"
])

Admin = Administrador("Santino", "Rodriguez", 16,
                      "santinorofu@gmail.com", "CABA", privilegios_admin)
Admin.MostrarPrivilegios()

#30.3
from Ejercicio_30_3_2_Extension import Administrador, Privilegios

privilegios_admin = Privilegios([
    "Puede Agregar Publicaciones",
    "Puede Eliminar Publicaciones",
    "Puede Bloquear Usuarios",
    "Puede Editar Publicaciones",
    "Puede Ver Estadísticas",
    "Puede Gestionar Comentarios",
    "Puede Agregar Imágenes",
    "Puede Modificar Perfil",
    "Puede Ver Perfil De Otros Usuarios",
    "Puede Enviar Mensajes Privados"
])

Admin = Administrador("Santino", "Rodriguez", 16,
                      "santinorofu@gmail.com", "CABA", privilegios_admin)
Admin.MostrarPrivilegios()

#31.1
import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


die_6 = Die(6)

print("Tiradas del dado de 6 caras:")
for _ in range(10):
    print(die_6.roll_die())

die_10 = Die(10)

print("\nTiradas del dado de 10 caras:")
for _ in range(10):
    print(die_10.roll_die())

die_20 = Die(20)

print("\nTiradas del dado de 20 caras:")
for _ in range(10):
    print(die_20.roll_die())

#31.2
import random

elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
ganadores = random.sample(elementos, 4)

print(
    f"¡Cualquier boleto que tenga estos 4 números o letras gana un premio: {ganadores}!")

#31.3
import random

Elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
MiTicekt = [7, 'B', 3, 'D']
Intentos = 0

while True:
    Ticket = random.sample(Elementos, 4)
    Intentos += 1
    if Ticket == MiTicekt:
        break

print(
    f"¡Ganaste! El boleto {MiTicekt} fue generado después de {Intentos} Intentos.")

#31.4
import random

# Generar un número aleatorio entre 1 y 10 (inclusive)
# random.randint(a, b) genera un número entero aleatorio entre a y b, donde ambos límites están incluidos.
numero_aleatorio = random.randint(1, 10)

# Imprimir el número aleatorio generado
# La función print muestra en consola el valor del número generado.
print(f"El número aleatorio generado es: {numero_aleatorio}")

#32.1
with open("1MillonPI.txt", "r") as file:
    Digitos = file.read()

Fecha = input(
    "Ingresa Tu Cumpleaños En La Forma ddmmaa: ")

if Fecha in Digitos:
    print(
        f"¡Sí! La secuencia {Fecha} aparece en los primeros un millón de dígitos de Pi.")
else:
    print(
        f"No, la secuencia {Fecha} no aparece en los primeros un millón de dígitos de Pi.")
    
#32.2
NombreArchivo = "learning_python.txt"
with open(NombreArchivo, "w") as Archivo:
    Archivo.write("En Python podés crear funciones para reutilizar código.\n")
    Archivo.write(
        "En Python podés trabajar con estructuras de datos como listas y diccionarios.\n")
    Archivo.write(
        "En Python podés manejar archivos para leer y escribir información.\n")
    Archivo.write(
        "En Python podés usar bucles para repetir tareas de forma eficiente.\n")
    Archivo.write(
        "En Python podés utilizar bibliotecas externas para ampliar funcionalidades.\n")

with open(NombreArchivo, "r") as Archivo:
    Contenido = Archivo.read()
    print("Lectura del archivo de una sola vez:")
    print(Contenido)

with open(NombreArchivo, "r") as Archivo:
    Lineas = Archivo.readlines()
    print("Lectura del archivo línea por línea:")
    for Linea in Lineas:
        print(Linea.strip())

#32.3

NombreArchivo = "learning_python.txt"
with open(NombreArchivo, "w") as Archivo:
    Archivo.write("En Python podés crear funciones para reutilizar código.\n")
    Archivo.write(
        "En Python podés trabajar con estructuras de datos como listas y diccionarios.\n")
    Archivo.write(
        "En Python podés manejar archivos para leer y escribir información.\n")
    Archivo.write(
        "En Python podés usar bucles para repetir tareas de forma eficiente.\n")
    Archivo.write(
        "En Python podés utilizar bibliotecas externas para ampliar funcionalidades.\n")

with open(NombreArchivo, "r") as Archivo:
    Contenido = Archivo.read()
    print("Lectura del archivo de una sola vez:")
    print(Contenido)

with open(NombreArchivo, "r") as Archivo:
    Lineas = Archivo.readlines()
    print("Lectura del archivo línea por línea:")
    for Linea in Lineas:
        print(Linea.strip())

with open(NombreArchivo, "r") as Archivo:
    print("Lectura del archivo con reemplazo de 'Python' por 'C':")
    for Linea in Archivo:
        print(Linea.replace("Python", "C").strip())

#30.1 - extension
class Restaurante:
    def __init__(self, NombreRestaurante, TipoCocina):
        self.NombreRestaurante = NombreRestaurante
        self.TipoCocina = TipoCocina
        self.ClientesAtendidos = 0

    def DescribirRestaurante(self):
        print(f"Restaurante: {self.NombreRestaurante}")
        print(f"Tipo de Cocina: {self.TipoCocina}")

    def AbrirRestaurante(self):
        print(f"El restaurante {self.NombreRestaurante} está abierto.")

    def EstablecerClientesAtendidos(self, NuevosClientes):
        self.ClientesAtendidos = NuevosClientes
        print(f"Clientes atendidos establecidos a: {self.ClientesAtendidos}")

    def IncrementarClientesAtendidos(self, ClientesAdicionales):
        self.ClientesAtendidos += ClientesAdicionales
        print(
            f"Clientes atendidos incrementados. Ahora son: {self.ClientesAtendidos}")

#30.2 - extension
class Usuario:
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.CorreoElectronico = CorreoElectronico
        self.Ciudad = Ciudad
        self.IntentosLogin = 0

    def DescribirUsuario(self):
        print(f"Nombre: {self.Nombre} {self.Apellido}")
        print(f"Edad: {self.Edad}")
        print(f"Correo Electrónico: {self.CorreoElectronico}")
        print(f"Ciudad: {self.Ciudad}")

    def SaludarUsuario(self):
        print(f"¡Hola, {self.Nombre}! Bienvenido a tu perfil.")

    def IncrementarIntentosLogin(self):
        self.IntentosLogin += 1
        print(
            f"Intentos de login incrementados. Ahora son: {self.IntentosLogin}")

    def ReiniciarIntentosLogin(self):
        self.IntentosLogin = 0
        print(
            f"Intentos de login reiniciados. Ahora son: {self.IntentosLogin}")


class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def MostrarPrivilegios(self):
        print(f"Privilegios:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


class Administrador(Usuario):
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad, Privilegios):
        super().__init__(Nombre, Apellido, Edad, CorreoElectronico, Ciudad)
        self.Privilegios = Privilegios

    def MostrarPrivilegios(self):
        self.Privilegios.MostrarPrivilegios()

#30.3.1 - extension
class Usuario:
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.CorreoElectronico = CorreoElectronico
        self.Ciudad = Ciudad
        self.IntentosLogin = 0

    def DescribirUsuario(self):
        print(f"Nombre: {self.Nombre} {self.Apellido}")
        print(f"Edad: {self.Edad}")
        print(f"Correo Electrónico: {self.CorreoElectronico}")
        print(f"Ciudad: {self.Ciudad}")

    def SaludarUsuario(self):
        print(f"¡Hola, {self.Nombre}! Bienvenido a tu perfil.")

    def IncrementarIntentosLogin(self):
        self.IntentosLogin += 1
        print(
            f"Intentos de login incrementados. Ahora son: {self.IntentosLogin}")

    def ReiniciarIntentosLogin(self):
        self.IntentosLogin = 0
        print(
            f"Intentos de login reiniciados. Ahora son: {self.IntentosLogin}")
        
#30.3.2 - extension
from Ejercicio_30_3_1_Extension import Usuario


class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def MostrarPrivilegios(self):
        print(f"Privilegios:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


class Administrador(Usuario):
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad, Privilegios):
        super().__init__(Nombre, Apellido, Edad, CorreoElectronico, Ciudad)
        self.Privilegios = Privilegios

    def MostrarPrivilegios(self):
        self.Privilegios.MostrarPrivilegios()