import pygame 
from settings import *

class Collectable(pygame.sprite.Sprite):
	def __init__(self,name,pos,score,groups):
		super().__init__(groups)
		self.name = name
		image = pygame.image.load(f'../graphics/test/{self.name}.png').convert_alpha()
		self.image = pygame.transform.scale(image, (TILESIZE - 35, TILESIZE - 35))
		self.rect = self.image.get_rect(center = pos)
		self.score = score
		self.hitbox = self.rect.inflate(0,-10)