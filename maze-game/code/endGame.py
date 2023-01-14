import pygame 
from settings import *

class Exit(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		image = pygame.image.load('../graphics/test/exit.png').convert_alpha()
		self.image = pygame.transform.scale(image, (TILESIZE, TILESIZE))
		
		self.rect = self.image.get_rect(center = pos)
		self.hitbox = self.rect.inflate(0,-10)