import pygame
import random


class Drop:

	def __init__(self, x_vel, r):
		self._pos = pygame.math.Vector2(100, 100)
		self._r = r
		self._vel = pygame.math.Vector2(x_vel, 0)
		self._acc = pygame.math.Vector2(0, .2)
		self.bounced = False

	@classmethod
	def from_random(cls, x_vel):
		# return cls(random.random()*x_max, 0, random.random()*(r_max-r_min)+r_min)
		return cls(x_vel, random.random()*5+5)

	def x(self):
		return self._pos.x

	def y(self):
		return self._pos.y

	def r(self):
		return self._r

	def pos(self):
		return self._pos

	def update(self):
		self._pos += self._vel
		self._vel += self._acc
