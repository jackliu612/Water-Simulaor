import pygame
import random
from Drop import Drop

bounce_chance = .2

WIDTH = 800
HEIGHT = 800

x_vel = 3

pygame.init()

size = (WIDTH, HEIGHT)
color = (245, 220, 29)

def draw_drop(surf, drop):
	pygame.draw.circle(surf, color, drop.pos(), drop.r())

def on_screen(drop, y_max=HEIGHT):
	return drop.y()-drop.r() < y_max

drops = [Drop.from_random(x_vel)]
for i in range(1, 200):
	for j in range(i):
		for _ in range(2):
			d = drops[j]
			drops[j].update() 
			if not on_screen(d):
				if not d.bounced and random.random()<bounce_chance:
					d._vel = d._vel.reflect(pygame.math.Vector2(0, 1))
					d._vel.scale_to_length(10)
					d.bounced = True
				else:
					drops[j] = Drop.from_random(x_vel)
			
	drops.append(Drop.from_random(x_vel))

screen = pygame.display.set_mode(size)

while True:
	left = pygame.key.get_pressed()[pygame.K_LEFT]
	right = pygame.key.get_pressed()[pygame.K_RIGHT]
	if left:
		x_vel-=.3
	if right:
		x_vel+=.3

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	pygame.time.Clock().tick(60)
	screen.fill('black')
	for (idx, d) in enumerate(drops):
		d.update()
		if not on_screen(d):
			if not d.bounced and random.random()<bounce_chance:
				d._vel = d._vel.reflect(pygame.math.Vector2(0, 1))
				d._vel.scale_to_length(10)
				d.bounced = True
			else:
				drops[idx] = Drop.from_random(x_vel)
		draw_drop(screen, d)

	pygame.display.flip()

