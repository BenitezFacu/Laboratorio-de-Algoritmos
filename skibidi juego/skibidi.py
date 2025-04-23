import os, pygame, random
os.system('cls')

pygame.init()
pygame.mixer.init()

blanco = (255, 255, 255)
negro = (0, 0, 0)

ancho, alto = 800, 600

pantalla = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption('skibidi invaders') 

explosion_sonido = pygame.mixer.Sound('Sonidos/explosion.wav')
disparo_sonido = pygame.mixer.Sound('Sonidos/shoot.wav')
musica_sonido = pygame.mixer.Sound('Sonidos/fondo.wav')
perder_sonido = pygame.mixer.Sound('Sonidos/perder.wav')

flecha = pygame.image.load('Personajes/flecha.png')
flecha_2 = pygame.image.load('Personajes/flecha_2.png')
flecha_3 = pygame.image.load('Personajes/flecha_3.png')
fondo = pygame.image.load('Fondos/fondo_1.jpg')
fondo_2 = pygame.image.load('Fondos/fondo_2.jpg')
fondo_3 = pygame.image.load('Fondos/fondo_3.png')
fondo_4 = pygame.image.load('Fondos/fondo_4.png')

flecha = pygame.transform.scale(flecha, (500, 100))
flecha_2 = pygame.transform.scale(flecha_2, (500, 100))
flecha_3 = pygame.transform.scale(flecha_3, (500, 100))
fondo = pygame.transform.scale(fondo, (800, 600))
fondo_2 = pygame.transform.scale(fondo_2, (800, 600))
fondo_3 = pygame.transform.scale(fondo_3, (800, 600))
fondo_4 = pygame.transform.scale(fondo_4, (800, 600))

fuente = pygame.font.Font("Caligrafías/PressStart2P.ttf", 36)
texto_2 = fuente.render("Jugar", True, blanco)
texto_3 = fuente.render("Tutorial", True, blanco)

seleccion = 0
seleccion_2 = 0
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
    
    def vidas(self, aliens, nave):
        global vidas
        for a in aliens[:]:
            if nave.rect.colliderect(a.rect):
                    vidas -= 1
                    aliens.remove(a)
                    break

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
    
    def naves(self, pantalla, vidas):
        screen_width, screen_height = pantalla.get_size()
        
        base_x = screen_width - (vidas * self.image.get_width() + (vidas - 1) * 10)
        base_y = screen_height - self.image.get_height() - 10
        
        for a in range(vidas):
            pantalla.blit(self.image, (base_x + (self.image.get_width() + 10) * a, base_y))


class bala:
    def __init__(self, x, y, velocidad):
        self.image = pygame.image.load("Personajes/bala.png")
        self.image = pygame.transform.scale(self.image, (25 , 30))
        self.velocidad = velocidad
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def disparar(self):
        self.rect.y -= self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class bala_alien:
    def __init__(self, x, y, velocidad):
        self.image = pygame.image.load("Personajes/bala.png")
        self.image = pygame.transform.scale(self.image, (25 , 10))
        self.velocidad = velocidad
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def disparar(self):
        self.rect.y += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class explosion:
    def __init__(self, x, y):
        self.image = pygame.image.load('Personajes/explosion.png')
        self.image = pygame.transform.scale(self.image,(45,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo = pygame.time.get_ticks()

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class Alien:
    def __init__(self, x, y, velocidad):
        self.images = [pygame.transform.scale((pygame.image.load)('Personajes/1_1.png'), (45,30)),
        pygame.transform.scale((pygame.image.load)('Personajes/1_2.png'), (45,30))]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad
        self.animation_timer = 0
        self.current_image = 0

    def movimiento(self, dx, bajar):
        self.rect.x += self.velocidad
        if bajar:
            self.rect.y += 10

    def animar(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
            self.animation_timer = 0 

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class Alien_1:
    def __init__(self, x, y, velocidad):
        self.images = [pygame.transform.scale((pygame.image.load)('Personajes/2_1.png'), (45,30)),
        pygame.transform.scale((pygame.image.load)('Personajes/2_2.png'), (45,30))]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad
        self.animation_timer = 0
        self.current_image = 0

    def movimiento(self, dx, bajar):
        self.rect.x += self.velocidad
        if bajar:
            self.rect.y += 10

    def animar(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
            self.animation_timer = 0 

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class Alien_2:
    def __init__(self, x, y, velocidad):
        self.images = [pygame.transform.scale((pygame.image.load)('Personajes/3_1.png'), (45,30)),
        pygame.transform.scale((pygame.image.load)('Personajes/3_2.png'), (45,30))]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad
        self.animation_timer = 0
        self.current_image = 0

    def movimiento(self, dx, bajar):
        self.rect.x += self.velocidad
        if bajar:
            self.rect.y += 10

    def animar(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
            self.animation_timer = 0 

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

aliens = []
oleada = 1
contador = 0
alien_velocidad = 1

def crear_aliens(contador, alien_velocidad): #Creación de los aliens
    for a in range(24):
        if a < 8:
            contador += 1
            aliens.append(Alien(50 + contador * 75, 100, 1 + alien_velocidad))
        elif a < 16:
            contador += 1
            aliens.append(Alien_1(50 + contador * 75, 150, 1 + alien_velocidad))
        else:
            contador += 1
            aliens.append(Alien_2(50 + contador * 75, 200, 1 + alien_velocidad))
        if a == 7 or a == 15:
            contador = 0

crear_aliens(contador, alien_velocidad)
nave = nave(400, 500, 5)

tiempo_ultimo_disparo = 0
tiempo_ultimo_disparo_alien = 0
cooldown_disparo = 500
cooldown_disparo_alien = 500

balas = []
balas_aliens = []
explosiones = []

vidas = 3

fondo_actual = fondo

perder = False
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
            if seleccion == 0: #Cambio de fondo
                if evento.key == pygame.K_RETURN:
                    if fondo_actual == fondo:
                        fondo_actual = fondo_2
                        mostrar_textos = False
                        mostrar_nave = True
                        pygame.mixer.music.load("Sonidos/fondo.wav")
                        pygame.mixer.music.play(-1)
            if seleccion == 1:
                if evento.key == pygame.K_RETURN: #Cambio de fondo
                    if fondo_actual == fondo:
                        fondo_actual = fondo_3
                        mostrar_textos = False
        if evento.type == pygame.KEYDOWN: #Disparo de las balas
            if evento.key == pygame.K_SPACE and mostrar_nave:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - tiempo_ultimo_disparo > cooldown_disparo:
                    nueva_bala = bala(nave.rect.centerx - 11, nave.rect.y, 10) #Velocidad bala
                    balas.append(nueva_bala)
                    disparo_sonido.play()
                    tiempo_ultimo_disparo = tiempo_actual

    pantalla.blit(fondo_actual,(0, 0))

    if mostrar_textos: #Dibujar el texto y el fondo
        pantalla.blit(texto_2, (315 , 250))
        pantalla.blit(texto_3, (265, 400))
        if seleccion == 0:
            pantalla.blit(flecha_2, (152, 220))
        elif seleccion == 1:
            pantalla.blit(flecha, (162, 370))
    
    if mostrar_nave: #Dibujar nave y las vidas
        keys = pygame.key.get_pressed()
        nave.moverse(keys)
        nave.dibujar(pantalla)
        nave.vidas(aliens, nave)
        nave.naves(pantalla, vidas)
        if mostrar_nave and len(aliens) == 0:
            oleada += 1
            alien_velocidad += 1
            contador = 0
            crear_aliens(contador, alien_velocidad)

        for alien in aliens: #Bajar filas de los aliens
            if alien.rect.x >= 740 or alien.rect.x <= 0:
                for a in aliens:
                    a.velocidad *= -1
                bajar_una_fila = True
                break

        for alien in aliens: #Dibujar los aliens
            alien.movimiento(alien_velocidad, bajar_una_fila)
            alien.dibujar(pantalla)
            alien.animar()
        bajar_una_fila = False

        for disparo in balas: #Dibujar las balas
            disparo.disparar()
            disparo.dibujar(pantalla)

        for bala_obj in balas[:]: #Colisión bala-alien y explosión alien
            for alien in aliens[:]:
                if bala_obj.rect.colliderect(alien.rect):
                    balas.remove(bala_obj)
                    aliens.remove(alien)
                    explosiones.append(explosion(alien.rect.centerx - 20, alien.rect.centery - 15))
                    explosion_sonido.play()
                    break

        for a in explosiones[:]: #Explosión alien
            if tiempo_actual - a.tiempo > 300:
                explosiones.remove(a)
            else:
                a.dibujar(pantalla)

        tiempo_actual = pygame.time.get_ticks() #Balas de los aliens
        if len(aliens) > 0 and tiempo_actual - tiempo_ultimo_disparo_alien > cooldown_disparo_alien:
            disparar = random.choice(aliens)
            disparo_alien = bala_alien(disparar.rect.centerx, disparar.rect.centery, 5) #Velocidad bala alien
            balas_aliens.append(disparo_alien)
            tiempo_ultimo_disparo_alien = tiempo_actual

        for disparo in balas_aliens: #Dibujar las balas de los aliens
            disparo.disparar()
            disparo.dibujar(pantalla)

        for balas_alien_obj in balas_aliens[:]: #Colisión bala alien-nave
            if balas_alien_obj.rect.colliderect(nave.rect):
                balas_aliens.remove(balas_alien_obj)
                explosion_sonido.play()
                vidas -= 1
                break

    if vidas == 0:
        mostrar_nave = False
        fondo_actual = fondo_4
        pantalla.blit(fondo_actual, (0, 0))
    
        if perder == False:
            pygame.mixer.music.pause()
            perder_sonido.play()
            perder = True
    
        if seleccion_2 == 0:
            pantalla.blit(flecha_2, (-25, 325))
        elif seleccion_2 == 1:
            pantalla.blit(flecha_3, (325, 325))
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if seleccion_2 < 1:
                seleccion_2 += 1
        if keys[pygame.K_LEFT]:
            if seleccion_2 > 0:
                seleccion_2 -= 1
    
        if keys[pygame.K_RETURN]:
            if seleccion_2 == 0:
                vidas = 3
                nave.rect.x = 400
                nave.rect.y = 500
                mostrar_textos = True
                perder = False
                fondo_actual = fondo
                aliens.clear()
                balas.clear()
                balas_aliens.clear()
                contador = 0
                oleada = 1
                alien_velocidad = 1
                crear_aliens(contador, alien_velocidad)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
pygame.quit()