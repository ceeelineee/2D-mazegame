import pygame
from collectables import Collectable 
from settings import *
from tile import Tile
from player import Player
from endGame import Exit
from debug import debug

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.collectable_sprites = pygame.sprite.Group()
		self.end_game_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Tile((x,y),"tree",[self.visible_sprites,self.obstacle_sprites])
				if col == 's':
					Tile((x,y),"stone",[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.collectable_sprites,self.end_game_sprites)
				if col == 'c':
					Collectable("coin",(x + TILESIZE//2 ,y + TILESIZE//2),10,[self.visible_sprites,self.collectable_sprites])
				if col == 'h':
					Collectable("diamond",(x + TILESIZE//2 ,y + TILESIZE//2),50,[self.visible_sprites,self.collectable_sprites])
				if col == 'b':
					Collectable("bomb",(x + TILESIZE//2 ,y + TILESIZE//2),-40,[self.visible_sprites,self.collectable_sprites])
				if col == 'h':
					Collectable("health",(x + TILESIZE//2 ,y + TILESIZE//2),0,[self.visible_sprites,self.collectable_sprites])
				if col == 'e':
					Exit((x + TILESIZE//2 ,y + TILESIZE//2),[self.visible_sprites,self.end_game_sprites])
					

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
