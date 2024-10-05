import pygame
import time
import sys
import const
from color_maze import Color
from draw_const import Draw
color = Color()

class Win:
	def __init__(self, color_text, color_del):
		self.screen = const.screen
		self.color_text = color_text
		self.color_del = color_del
		self.sizeFont = 70
		self.sizefont = 30
		self.font = 24
	def Win_game(self, x = 100, y = 150, x1 = 500, y1 = 370):
		Draw().draw_img(x, y, "img\\menu\\1.png", size = (x1, y1))
		pygame.draw.rect(self.screen, self.color_del, (x + 20, y + 20, x1 - 40, y1 - 40), 0)
		Draw().draw_text("WIN GAME", x + 60, y + 50, self.color_text, self.sizeFont)
		pygame.display.update()
	def Score_time(self, time_draw, x = 370, y = 275, color = color.Yellow):
		Draw().draw_text("Score: ", x - 120, y, color, self.sizefont)
		Draw().draw_text(time_draw, x, y, color, self.sizefont)
		pygame.display.update()
	def New_game(self, x = 235, y = 310, x1 = 240, y1 = 60):
		k = pygame.draw.rect(self.screen, self.color_del, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\green.png", size = (x1, y1))
		Draw().draw_text("New game", x + 48, y + 18, self.color_text, self.font)
		pygame.display.update()
		return k

	def Restart_game(self, x = 235, y = 375, x1 = 240, y1 = 60):
		k = pygame.draw.rect(self.screen, self.color_del, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\blue_dark.png", size = (x1, y1))
		Draw().draw_text("Restart game", x + 16, y + 18, self.color_text, self.font)
		pygame.display.update()
		return k
	def Quit_game(self, x = 235, y = 440, x1 = 240, y1 = 60):
		k = pygame.draw.rect(self.screen, self.color_del, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\red.png", size = (x1, y1))
		Draw().draw_text("QUIT GAME", x + 40, y + 18, self.color_text, self.font)
		pygame.display.update()
		return k
