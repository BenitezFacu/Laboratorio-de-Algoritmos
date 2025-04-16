import os, pygame
os.system('cls')

pygame.init()

blanco = (255, 255, 255)
negro = (0, 0, 0)

Ancho, Alto = 800, 600

pantalla = pygame.display.set_mode((Ancho, Alto)) 
pygame.display.set_caption('skibidi invaders') 

bicho = pygame.image.load('Personajes/skibidi_bicho.png')
flecha = pygame.image.load('Personajes/flecha.png')
fondo = pygame.image.load('Fondos/fondo.jpg')
fondo_2 = pygame.image.load('Fondos/fondo_2.png')
fondo_3 = pygame.image.load('Fondos/fondo_3.png')
bala = pygame.image.load('Personajes/bala.png')

nueva_flecha = pygame.transform.scale(flecha, (50, 50))
nuevo_fondo = pygame.transform.scale(fondo, (800, 600))
nuevo_fondo_2 = pygame.transform.scale(fondo_2, (800, 600))
nuevo_fondo_3 = pygame.transform.scale(fondo_3, (800, 600))

fuente = pygame.font.Font("Caligrafías/Gameplay.ttf", 72)
fuente_2 = pygame.font.Font("Caligrafías/Gameplay.ttf", 36)

texto = fuente.render("SPACE INVADERS", True, blanco)
texto_2 = fuente_2.render("Jugar", True, blanco)
texto_3 = fuente_2.render("Tutorial", True, blanco)

seleccion = 0
skibidi = True

class nave:
    def __init__(self, x, y , velocidad):
        self.image = pygame.image.load('Personajes/skibidi_nave.png')
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

    def moverse(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 700:
            self.rect.x = 700
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class bala:
    def __init__(self, x, y, velocidad):
        self.image = pygame.image.load("Personajes/bala.png")
        self.image = pygame.transform.scale(self.image, (25 , 50))
        self.velocidad = velocidad
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def disparar(self):
        self.rect.y -= self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class Alien:
    def __init__(self, x, y, velocidad):
        self.image = pygame.image.load('Personajes/bicho_1.png')
        self.image = pygame.transform.scale(self.image, (45, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

    def movimiento(self, dx, bajar):
        self.rect.x += dx
        if bajar:
            self.rect.y += 20

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class Alien_1:
    def __init__(self, x, y, velocidad):
        self.image = pygame.image.load("Personajes/bicho_2.png")
        self.image = pygame.transform.scale(self.image, (45, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

    def movimiento(self, dx, bajar):
        self.rect.x += dx
        if bajar:
            self.rect.y += 20

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class Alien_2:
    def __init__(self, x, y, velocidad):
        self.image = pygame.image.load("Personajes/bicho_3.png")
        self.image = pygame.transform.scale(self.image, (45, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

    def movimiento(self, dx, bajar):
        self.rect.x += dx
        if bajar:
            self.rect.y += 20

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)        

aliens = []
contador = 0

for a in range(24):
    if a < 8:
        contador += 1
        aliens.append(Alien(50 + contador * 75, 100, 5))
    elif a < 16:
        contador += 1
        aliens.append(Alien_1(50 + contador * 75, 150, 5))
    else:
        contador += 1
        aliens.append(Alien_2(50 + contador * 75, 200, 5))
        
    if a == 7 or a == 15:
        contador = 0 

nave = nave(Ancho // 2 - 25, Alto - 100, 5)

alien_velocidad = 3
tiempo_ultimo_disparo = 0
cooldown_disparo = 500

balas = []

fondo_actual = nuevo_fondo

mostrar_textos = True
mostrar_nave = False
bajar_una_fila = False

while skibidi:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            skibidi = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                if seleccion < 1:
                    seleccion += 1
            if evento.key == pygame.K_UP:
                if seleccion > 0:
                    seleccion -= 1
            if seleccion == 0:
                if evento.key == pygame.K_RETURN:
                    if fondo_actual == nuevo_fondo:
                        fondo_actual = nuevo_fondo_2
                        mostrar_textos = False
                        mostrar_nave = True
            if seleccion == 1:
                if evento.key == pygame.K_RETURN:
                    if fondo_actual == nuevo_fondo:
                        fondo_actual = nuevo_fondo_3
                        mostrar_textos = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and mostrar_nave:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - tiempo_ultimo_disparo > cooldown_disparo:
                    nueva_bala = bala(nave.rect.centerx - 11, nave.rect.y, 10)
                    balas.append(nueva_bala)
                    tiempo_ultimo_disparo = tiempo_actual

    pantalla.fill(negro)
    pantalla.blit(fondo_actual,(0, 0))

    if mostrar_textos:
        pantalla.blit(texto, (60, 50))
        pantalla.blit(texto_2, (325, 250))
        pantalla.blit(texto_3, (300, 400))
        if seleccion == 0:
            pantalla.blit(nueva_flecha, (260, 245))
        elif seleccion == 1:
            pantalla.blit(nueva_flecha, (230, 395))
    
    if mostrar_nave:
        keys = pygame.key.get_pressed()
        nave.moverse(keys)
        nave.dibujar(pantalla)
        for alien in aliens:
            if alien.rect.x >= 740 or alien.rect.x <= 0:
                alien_velocidad *= -1
                bajar_una_fila = True
                break
        for alien in aliens:
            alien.movimiento(alien_velocidad, bajar_una_fila)
            alien.dibujar(pantalla)
        bajar_una_fila = False
        for a in balas:
            a.disparar()
            a.dibujar(pantalla)
        for bala_obj in balas[:]:
            for alien in aliens[:]:
                if bala_obj.rect.colliderect(alien.rect):
                    balas.remove(bala_obj)
                    aliens.remove(alien)
                    break

    pygame.display.flip()

    pygame.time.Clock().tick(60)
    
pygame.quit()