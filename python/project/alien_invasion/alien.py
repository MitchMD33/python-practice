import pygame 
from pygame.sprite import Sprite 

class Alien(Sprite):
	""" A class to represent a single alien in the fleet """ 

	def __init__(self, ai_game):
		""" initialize the alien and set its starting point """
		super().__init__()
		self.screen = ai_game.screen

		#Load the alien image and set its rect attribute 
		self.image = pygame.image.load('/home/mitchell/Desktop/repo/python-practice/python/project/alien_invasion/images/spaceship.bmp')
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image, (60, 60))

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position/ 
		self.x = float(self.rect.x)