import pygame
import const

class Draw:
	def __init__(self):
		self.screen = const.screen
		
	def draw_img(self, x, y, path, size):
		image = pygame.image.load(path).convert_alpha()
		image = pygame.transform.scale(image, size = size)
		image_rect = image.get_rect(topleft = (x, y))
		self.screen.blit(image, image_rect)
		pygame.display.update()

	def draw_text(self, text, x, y, color, size):
		font = const.get_font(size)
		surface = font.render(text, True, color)
		rect = surface.get_rect(topleft = (x, y))
		self.screen.blit(surface, rect)

	def draw_text_normal(self, text, x, y, color, size):
		font = pygame.font.Font(None, size)
		surface = font.render(text, True, color)
		self.screen.blit(surface, (x, y))

	def draw_text_center(self, x, y, font, color, text):
		surface = font.render(text, True, color)
		rect = surface.get_rect(center = (x, y))
		self.screen.blit(surface, rect)
	
	def draw_box(self, x, y, path, size):
		image = pygame.image.load(path).convert_alpha()
		image = pygame.transform.scale(image, size = size)
		image_rect = image.get_rect(center = (x, y))
		self.screen.blit(image, image_rect)