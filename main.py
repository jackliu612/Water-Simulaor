import pygame

WIDTH = 500
HEIGHT = 500

pygame.init()

size = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	pygame.time.Clock().tick(60)
	screen.fill('black')
	pygame.draw.circle(screen, (245, 213, 29), (250, 250), 10)
	pygame.display.flip()

