import os
os.system('cls')

def hacer_album(artista, titulo, canciones = None):
    album = {"artista" : artista, "titulo" : titulo}
    if canciones:
        album["canciones"] = canciones
    return album

print(hacer_album(artista = "Soda stereo", titulo = "Signos"))
print(hacer_album(artista = "Milo J", titulo = "111"))
print(hacer_album(artista = "Andrés Calamaro", titulo = "Alta suciedad"))
print(hacer_album(artista = "Gustavo Cerati", titulo = "Bocanada", canciones = 15))