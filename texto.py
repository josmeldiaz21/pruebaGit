import pygame
import math
# Definir algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)

pygame.init()

dimensiones = (1024, 768)
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("Josmel")

salir = False

reloj = pygame.time.Clock()

while not salir:
	for evento in pygame.event.get():
	    if evento.type == pygame.QUIT:
	        print("El usuario solicitó salir.")
	        salir = True
	pantalla.fill(BLANCO)

	# Selecciona la fuente. Fuente Default, tamaño 25 pt.
	fuente = pygame.font.Font(None, 25)
	 
	# Reproduce el texto. "True" significa texto suavizado(anti-aliased).
	# El color es Negro. Recordemos que ya hemos definido anteriormente la variable NEGRO
	# como una lista de (0, 0, 0)
	# Observación: Esta línea crea una imagen de las letras,
	# Pero aún no la pone sobre la pantalla.
	texto = fuente.render("Mi texto", True, NEGRO)
	 
	# Coloca la imagen del texto sobre la pantalla en 250 x 250
	pantalla.blit(texto, [250, 250])
	pygame.display.flip()

reloj.tick(20)
pygame.quit()