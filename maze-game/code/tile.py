from re import T
import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,type,groups):
		super().__init__(groups)
		self.type = type
		image = pygame.image.load(f'../graphics/test/{self.type}.png').convert_alpha()
		self.image = pygame.transform.scale(image, (TILESIZE, TILESIZE))
		if self.type == "stone":
			self.hitPoints = 25
			self.image = pygame.transform.scale(image, ((TILESIZE//2) + self.hitPoints, (TILESIZE//2) + self.hitPoints))
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)