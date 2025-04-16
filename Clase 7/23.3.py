import os
os.system('cls')

def hacer_album(artista, titulo, canciones = None):
    album = {"artista" : artista, "titulo" : titulo}
    if canciones:
        album["canciones"] = canciones
    return album

while True:
    pregunta = input("Quiere elegir un artista con un album suyo? (y/n): ")
    if pregunta == "y":
        artista = input("Ingrese el nombre de un artista: ", )
        titulo = input("Ingrese el nombre de un álbum del artista: ")
        album = hacer_album(artista = artista, titulo = titulo)
        print(album)
    elif pregunta == "n":
        break
    else:
        print("Dato ingresado erróneo")