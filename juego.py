
import pygame

# Inicializar Pygame
pygame.init()

# Definir colors
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Tamaño de la ventana
ANCHO = 800
ALTO = 600

# Crear la ventana
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mover Círculo")

# Coordenadas iniciales del círculo
x = ANCHO // 2
y = ALTO // 2
radio = 40
velocidad = 10

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Obtener teclas presionadas
    teclas = pygame.key.get_pressed()
    
    # Mover círculo
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Limitar movimiento del círculo a los bordes de la ventana
    if x - radio < 0:
        x = radio
    if x + radio > ANCHO:
        x = ANCHO - radio
    if y - radio < 0:
        y = radio
    if y + radio > ALTO:
        y = ALTO - radio

    # Rellenar pantalla de blanco
    screen.fill(BLANCO)
    
    # Dibujar círculo
    pygame.draw.circle(screen, ROJO, (x, y), radio)
    
    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()
