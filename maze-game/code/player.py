import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites,collectable_sprites,end_game_sprites):
		super().__init__(groups)
		image = pygame.image.load('../graphics/test/player.png').convert_alpha()
		self.image = pygame.transform.scale(image, (TILESIZE - 20, TILESIZE - 20))
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-26)
	  
		self.score = 0
		self.coins = 0
		self.health = 100
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font('freesansbold.ttf', 20)
		self.direction = pygame.math.Vector2()
		self.speed = 5
		self.obstacle_sprites = obstacle_sprites
		self.collectable_sprites = collectable_sprites
		self.end_game_sprites = end_game_sprites
  

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		for sprite in self.obstacle_sprites:
		 	if sprite.type == "stone" and sprite.hitbox.colliderect(self.hitbox):
		 		if keys[pygame.K_SPACE]:
						sprite.kill()


	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()
		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center
		

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right
					if sprite.type == "stone" and pygame.key.get_pressed()[pygame.K_SPACE]:
						self.health -= 10
						sprite.kill()

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom
					if sprite.type == "stone" and pygame.key.get_pressed()[pygame.K_SPACE]:
						self.health -= 10
						sprite.kill()
      
		#collectables logic
		for sprite in self.collectable_sprites:
			if self.rect.colliderect(sprite.rect):
				self.score += sprite.score
				print(self.score)
				if sprite.name == "coin":
					self.coins += 1
				if sprite.name == "bomb":
					self.health -= 25
				if sprite.name == "health" and self.health < 100:
					self.health += 10
				sprite.kill()

		for sprite in self.end_game_sprites:
			pass
      
        	

	def update(self):
		self.input()
		self.move(self.speed)
		self.score_text = self.font.render(f'Score: {self.score}', True, white, black)
		self.score_textRect = self.score_text.get_rect()
		self.display_surface.blit(self.score_text, (10, 20))
  
		self.coins_text = self.font.render(f'Coins: {self.coins}', True, white, black)
		self.coins_textRect = self.coins_text.get_rect()
		self.display_surface.blit(self.coins_text, (10, 40))
  
		self.health_text = self.font.render(f'health: {self.health}', True, white, black)
		self.health_textRect = self.health_text.get_rect()
		self.display_surface.blit(self.health_text, (10, 60))