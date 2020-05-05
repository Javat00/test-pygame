import pygame
from pygame import mixer

# comenzamos el bucle del juego
run = True
# inicializamos pygame
pygame.init()
# muestro ventana 800x600
size = (800, 600)
screen = pygame.display.set_mode(size)
# cambiamos el titulo de la ventana
pygame.display.set_caption("chincheta_test_mov")
# inicializamos variables
black = 0, 0, 0
# crea un objeto imagen y obtengo su rectangulo
chinch = pygame.image.load("./images/chincheta.png")
chinch = pygame.transform.scale(chinch, (200, 200))
chinchf = pygame.Rect(0, 0, 0, 0)

# ponemos musica de fondo
mixer.music.load("./music/background.wav")
mixer.music.play(-1)  # si pasamos -1 se repetirá indefinidamente
while run:
    # pinto el fondo de negro, dibujo la chincheta y actualizo la pantalla
    screen.fill(black)
    screen.blit(chinch, chinchf)
    pygame.display.flip()
    pygame.time.delay(2)  # controlamos la velocidad de mov
    # capturamos los eventos que se producen
    for event in pygame.event.get():

        # descomentar si queremos saber coordenadas "print("x:" + str(chinchf.x) + " y:" + str(chinchf.y))"
        # si el evento es salir terminamos
        if event.type == pygame.QUIT:
            run = False
    #  controlamos el movimiento de la figura con las flechas y evitamos que salga de los bordes de la pantalla
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and chinchf.x > 0:
            chinchf.x -= 1
        if event.key == pygame.K_DOWN and chinchf.y < 390:
            chinchf.y += 1
        if event.key == pygame.K_UP and chinchf.y > 0:
            chinchf.y -= 1
        if event.key == pygame.K_RIGHT and chinchf.x < 595:
            chinchf.x += 1
