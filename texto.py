import pygame
# Definir algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)

pygame.init()
rect_x = 50
rect_y = 50
rect_cambio_x = 15
rect_cambio_y = 5
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
	pantalla.fill(NEGRO)
	pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
	pygame.draw.rect(pantalla, ROJO, [rect_x + 10, rect_y + 10 , 30, 30])
	rect_x += rect_cambio_x
	rect_y += rect_cambio_y
	if rect_y > 718 or rect_y < 0:
		rect_cambio_y = rect_cambio_y * -1
	if rect_x > 1024 or rect_x < 0:
		rect_cambio_x = rect_cambio_x * -1
	pygame.display.flip()
reloj.tick(50)