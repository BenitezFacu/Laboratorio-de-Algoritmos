import os, pygame, random, json, time
os.system('cls')

pygame.init()
#pygame.mixer.init()

blanco = (255, 255, 255)
negro = (0, 0, 0)

ancho, alto = 800, 600

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('skibidi invaders') 

#Sonidos
explosion_sonido = pygame.mixer.Sound('Sonidos/explosion.wav')
disparo_sonido = pygame.mixer.Sound('Sonidos/shoot.wav')
musica_sonido = pygame.mixer.Sound('Sonidos/fondo.wav')
perder_sonido = pygame.mixer.Sound('Sonidos/perder.wav')

#Cargar fondos y flechas
flecha = pygame.image.load('Personajes/flecha.png')
flecha_2 = pygame.image.load('Personajes/flecha_2.png')
flecha_3 = pygame.image.load('Personajes/flecha_3.png')
flecha_4 = pygame.image.load('Personajes/flecha_4.png')
fondo = pygame.image.load('Fondos/fondo_1.jpg')
fondo_2 = pygame.image.load('Fondos/fondo_2.jpg')
fondo_3 = pygame.image.load('Fondos/fondo_3.png')

#Escalado
flecha = pygame.transform.scale(flecha, (500, 100))
flecha_2 = pygame.transform.scale(flecha_2, (500, 100))
flecha_3 = pygame.transform.scale(flecha_3, (500, 100))
fondo = pygame.transform.scale(fondo, (800, 600))
fondo_2 = pygame.transform.scale(fondo_2, (800, 600))
fondo_3 = pygame.transform.scale(fondo_3, (800, 600))

#Caligrafías
fuente = pygame.font.Font("Caligrafías/PressStart2P.ttf", 36)
fuente_2 = pygame.font.Font("Caligrafías/PressStart2P.ttf", 24)

#Textos
texto_1 = fuente_2.render("Presione esc para volver al menú", True, blanco)
texto_2 = fuente.render("Jugar", True, blanco)
texto_3 = fuente.render("Puntajes", True, blanco)
texto_4 = fuente_2.render("Puntos:", True, blanco)
texto_5 = fuente_2.render("Oleada:", True, blanco)
texto_6 = fuente.render("Salir", True, blanco)
texto_7 = fuente_2.render("Ingrese su nombre:", True, blanco)
texto_8 = fuente_2.render("Cargando Juego...", True, blanco)

seleccion = 0
seleccion_2 = 0
skibidi = True

def cargar_puntuaciones():
    try:
        with open('scores.json', 'r') as file:
            data = json.load(file)
        return data['high_scores']
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def guardar_puntuaciones(puntuaciones):
    with open('scores.json', 'w') as file:
        json.dump({"high_scores": puntuaciones}, file, indent=4)

def actualizar_puntuaciones(puntuacion_nueva, nombre_jugador):
    puntuaciones = cargar_puntuaciones()
    puntuaciones.append({"name": nombre_jugador, "score": puntuacion_nueva})
    puntuaciones.sort(key=lambda x: x['score'], reverse=True)
    if len(puntuaciones) > 5:
        puntuaciones = puntuaciones[:5]
    guardar_puntuaciones(puntuaciones)

def mostrar_scoreboard(pantalla):
    puntuaciones = cargar_puntuaciones()  # Cargar las puntuaciones guardadas
    fuente_scoreboard = pygame.font.Font("Caligrafías/PressStart2P.ttf", 24)
    texto_scoreboard = fuente_scoreboard.render("Scoreboard", True, blanco)
    pantalla.blit(texto_scoreboard, (270, 50))  # Título del scoreboard en la parte superior
    for i, puntuacion in enumerate(puntuaciones):  # Mostrar las 5 mejores puntuaciones
        texto_puntuacion = fuente_scoreboard.render(f"{i + 1}. {puntuacion['name']} - {puntuacion['score']}", True, blanco)
        pantalla.blit(texto_puntuacion, (200, 100 + (i * 30)))  # Dibujar las puntuaciones en la pantalla

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
        x = 0
        y = 550
        for a in range(vidas):
            pantalla.blit(self.image, (x + (self.image.get_width() + 10) * a, y))

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
        self.valor = 20

    def movimiento(self, bajar):
        self.rect.x += self.velocidad
        if bajar:
            self.rect.y += 5

    def animar(self): #Animación de los aliens
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
        self.valor = 15

    def movimiento(self, bajar):
        self.rect.x += self.velocidad
        if bajar:
            self.rect.y += 5

    def animar(self): #Animación de los aliens
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
        self.valor = 10

    def movimiento(self, bajar):
        self.rect.x += self.velocidad
        if bajar:
            self.rect.y += 5

    def animar(self): #Animación de los aliens
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
cd_disparo = 500
cd_disparo_alien = 500

balas = []
balas_aliens = []
explosiones = []

vidas = 3
puntaje = 0
fondo_actual = fondo

perder = False
mostrar_textos = True
mostrar_nave = False
bajar_una_fila = False
scoreaboard = False
menu = True

nombre = ""
clock = pygame.time.Clock()

while skibidi:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            skibidi = False
        elif evento.type == pygame.KEYDOWN:
            if menu == True:
                Ingrese_nombre = True
                if evento.key == pygame.K_DOWN:
                    if seleccion < 2:
                        seleccion += 1
                if evento.key == pygame.K_UP:
                    if seleccion > 0:
                        seleccion -= 1
                if seleccion == 0: #Cambio de fondo
                    if evento.key == pygame.K_RETURN:
                        while Ingrese_nombre == True: #Ingreso de nombre
                            clock.tick(60)
                            pantalla.blit(fondo_2, (0, 0))
                            for evento in pygame.event.get():
                                if evento.type == pygame.QUIT:
                                    pygame.quit()
                                elif evento.type == pygame.KEYDOWN:
                                    if evento.key == pygame.K_RETURN:
                                        Ingrese_nombre = False
                                    elif evento.key == pygame.K_BACKSPACE:
                                        nombre = nombre[:-1]
                                    else:
                                        nombre += evento.unicode
                            usuario = fuente_2.render(nombre, True, blanco)
                            pantalla.blit(texto_7, (25, 285))
                            pantalla.blit(usuario, (475, 285))
                            pygame.display.update()
                        pantalla.blit(fondo_2, (0, 0))
                        pantalla.blit(texto_8, (200, 290))
                        pygame.display.update()
                        time.sleep(2)
                        fondo_actual = fondo_2
                        mostrar_textos = False
                        mostrar_nave = True
                        mostrar_nave_2 = False
                        pygame.mixer.music.load("Sonidos/fondo.wav")
                        pygame.mixer.music.play(-1)
                        scoreaboard = False
                        menu = False
                if seleccion == 1:
                    if evento.key == pygame.K_RETURN: #Cambio de fondo
                        fondo_actual = fondo_2
                        mostrar_textos = False
                        scoreaboard = True
                        Ingrese_nombre = True
                if seleccion == 2:
                    if evento.key == pygame.K_RETURN:
                        skibidi = False
                if evento.key == pygame.K_ESCAPE and seleccion == 1:
                    mostrar_scoreboard_flag = False  # Dejar de mostrar el scoreboard
                    seleccion = 0 

        if evento.type == pygame.KEYDOWN: #Disparo de las balas
            if evento.key == pygame.K_SPACE and mostrar_nave:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - tiempo_ultimo_disparo > cd_disparo:
                    nueva_bala = bala(nave.rect.centerx - 11, nave.rect.y, 10) #Velocidad bala
                    balas.append(nueva_bala)
                    disparo_sonido.play()
                    tiempo_ultimo_disparo = tiempo_actual
        if evento.type == pygame.KEYDOWN: #Volver al menú
            if evento.key == pygame.K_ESCAPE:
                if scoreaboard:
                    fondo_actual = fondo
                    scoreaboard = False
                    mostrar_textos = True
                    seleccion = 0

    pantalla.blit(fondo_actual,(0, 0))

    if mostrar_textos: #Dibujar el texto y el fondo
        pantalla.blit(texto_2, (315 , 250))
        pantalla.blit(texto_3, (270, 340))
        pantalla.blit(texto_6, (315, 440))
        if seleccion == 0:
            pantalla.blit(flecha_2, (152, 220))
        elif seleccion == 1:
            pantalla.blit(flecha, (162, 310))
        elif seleccion == 2:
            pantalla.blit(flecha_2, (152, 410))
    
    if scoreaboard == True:
        mostrar_scoreboard(pantalla)
        pantalla.blit(texto_1, (20, 500))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pantalla.blit(fondo_actual, (0, 0))
    
    if mostrar_nave == True: #Dibujar nave y las vidas
        keys = pygame.key.get_pressed()
        nave.moverse(keys)
        nave.dibujar(pantalla)
        nave.vidas(aliens, nave)
        nave.naves(pantalla, vidas)
        pantalla.blit(texto_4, (25, 25))
        puntos = fuente_2.render(str(puntaje), True, blanco)
        pantalla.blit(puntos, (200, 25))
        pantalla.blit(texto_5, (575, 25))
        oleadas = fuente_2.render(str(oleada), True, blanco)
        pantalla.blit(oleadas, (750, 25))
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
            alien.movimiento(bajar_una_fila)
            alien.dibujar(pantalla)
            alien.animar()
        bajar_una_fila = False

        for disparo in balas: #Dibujar las balas
            disparo.disparar()
            disparo.dibujar(pantalla)

        for a in balas[:]: #Colisión bala-alien y explosión alien
            for alien in aliens[:]:
                if a.rect.colliderect(alien.rect):
                    balas.remove(a)
                    aliens.remove(alien)
                    explosiones.append(explosion(alien.rect.centerx - 20, alien.rect.centery - 15))
                    explosion_sonido.play()
                    puntaje += alien.valor
                    break

        for a in explosiones[:]: #Explosión alien
            if tiempo_actual - a.tiempo > 300:
                explosiones.remove(a)
            else:
                a.dibujar(pantalla)

        tiempo_actual = pygame.time.get_ticks() #Balas de los aliens
        if len(aliens) > 0 and tiempo_actual - tiempo_ultimo_disparo_alien > cd_disparo_alien:
            disparar = random.choice(aliens)
            disparo_alien = bala_alien(disparar.rect.centerx, disparar.rect.centery, 5) #Velocidad bala alien
            balas_aliens.append(disparo_alien)
            tiempo_ultimo_disparo_alien = tiempo_actual

        for disparo in balas_aliens: #Dibujar las balas de los aliens
            disparo.disparar()
            disparo.dibujar(pantalla)

        for a in balas_aliens[:]: #Colisión bala alien-nave
            if a.rect.colliderect(nave.rect):
                balas_aliens.remove(a)
                explosion_sonido.play()
                vidas -= 1
                break

    if vidas == 0:
        mostrar_nave = False
        fondo_actual = fondo_3
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
                actualizar_puntuaciones(puntaje, nombre)
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
                puntaje = 0
                menu = True
                nombre = ""
            if seleccion_2 == 1:
                actualizar_puntuaciones(puntaje, nombre)
                mostrar_scoreboard(pantalla)
                skibidi = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
pygame.quit()