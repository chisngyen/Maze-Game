import pygame
import time
import sys
import const
from color_maze import Color
from draw_const import Draw
color = Color()
class TableMenu:
	def __init__(self, thickness, colorBar, colorIn, x = 710, y = 0, x1 = 370, y1 = 720):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.thickness = thickness
		self.colorBar = colorBar
		self.colorIn = colorIn
	def draw(self):
		pygame.draw.rect(self.screen, self.colorBar, (self.x, self.y, self.x1, self.y1), 0)
		pygame.draw.rect(self.screen, self.colorIn, (self.x + self.thickness, self.y + self.thickness, self.x1 - 2*self.thickness, self.y1 - 2*self.thickness), 0)
		pygame.display.update()
	def delete(self):
		pygame.draw.rect(self.screen, self.colorIn, (self.x + self.thickness, self.y + self.thickness, self.x1 - 2*self.thickness, self.y1 - 2*self.thickness), 0)
		pygame.display.update()
class Level:
	def __init__(self, color_text, colorIn, thickness, level, x = 830, y = 35, x1 = 140, y1 = 40):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.thickness = thickness
		self.text = "Level"
		self.level = level
		self.path = "img\\menu\\blue_white.png"
		self.path_easy = "img\\menu\\green.png"
		self.path_medium = "img\\menu\\yellow.png"
		self.path_hard = "img\\menu\\red.png"
		self.sizeFont = 24
		self.sizefont = 20
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 33, self.y + 10, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def draw_text(self):
		Draw().draw_text(self.level, self.x + 25, self.y + 51, self.color_text, self.sizefont)
		pygame.display.update()
	def delete(self, x = 710, y = 70):
		pygame.draw.rect(self.screen, self.colorIn, (x  + self.thickness, y + self.thickness, 1080 - x - 2*self.thickness, 50), 0)
		pygame.display.update()
	def easy(self, x = 757, y = 80, x1 = 64, y1 = 30):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_easy, size = (x1, y1))
		Draw().draw_text("easy", x + 6, y + 6, self.color_text, self.sizefont)
		pygame.display.update()
		return k
	def medium(self, x = 847, y = 80, x1 = 108, y1 = 30):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_medium, size = (x1, y1))
		Draw().draw_text("medium", x + 8, y + 6, self.color_text, self.sizefont)
		pygame.display.update()
		return k
	def hard(self, x = 980, y = 80, x1 = 66, y1 = 30):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_hard, size = (x1, y1))
		Draw().draw_text("hard", x + 6, y + 6, self.color_text, self.sizefont)
		pygame.display.update()
		return k
class Mode:
	def __init__(self, color_text, colorIn, thickness, mode, x = 830, y = 130, x1 = 140, y1 = 40):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.thickness = thickness
		self.text = "Mode"
		self.mode = mode
		self.path = "img\\menu\\blue_white.png"
		self.path_player = "img\\menu\\green.png"
		self.path_bot = "img\\menu\\red.png"
		self.sizeFont = 24
		self.sizefont = 20
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 30, self.y + 10, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def draw_text(self):
		Draw().draw_text(self.mode, self.x + 28, self.y + 51, self.color_text, self.sizefont)
		pygame.display.update()
	def delete(self, x = 710, y = 165):
		pygame.draw.rect(self.screen, self.colorIn, (x  + self.thickness, y + self.thickness, 1080 - x - 2*self.thickness, 50), 0)
		pygame.display.update()
	def player(self, x = 770, y = 176, x1 = 92, y1 = 30):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_player, size = (x1, y1))
		Draw().draw_text("player", x + 8, y + 7, self.color_text, self.sizefont)
		pygame.display.update()
		return k
	def bot(self, x = 940, y = 176, x1 = 92, y1 = 30):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_bot, size = (x1, y1))
		Draw().draw_text("bot", x + 25, y + 7, self.color_text, self.sizefont)
		pygame.display.update()
		return k
class Spawn:
	def __init__(self, color_text, colorIn, thickness, x = 830 , y = 230, x1 = 140, y1 = 40):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.text = "Spawn"
		self.thickness = thickness
		self.path = "img\\menu\\blue_white.png"
		self.sizeFont = 24
		self.sizefont = 20
		self.mimifont = 16
	def draw(self):
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 25, self.y + 10, self.color_text, self.sizeFont)
		pygame.display.update()
	def delete(self, x = 710, y = 265):
		pygame.draw.rect(self.screen, self.colorIn, (x  + self.thickness, y + self.thickness, 1080 - x - 2*self.thickness, 60), 0)
		pygame.display.update()
	def random(self, x = 750, y = 290, x1 = 130, y1 = 40):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\yellow.png", size = (x1, y1))
		Draw().draw_text("random", x + 18, y + 10, self.color_text, self.sizefont)
		pygame.display.update()
		return k
	def mouse(self, x = 920, y = 290, x1 = 130, y1 = 40):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\blue.png", size = (x1, y1))
		Draw().draw_text("mouse", x + 24, y + 10, self.color_text, self.sizefont)
		pygame.display.update()
		return k
	def notification(self, colorblue = color.Blue,x =  755, y = 300):
		Draw().draw_text("Please click mouse in maze!", x, y, colorblue, self.mimifont)
		pygame.display.update()
	def error(self, colorred = color.Red, x = 800, y = 311):
		Draw().draw_text("Error: it overlaps!", x, y, colorred, self.mimifont)
		pygame.display.update()

class RandMaze:
	def __init__(self, color_text, colorIn, x = 775, y = 370, x1 = 240, y1 = 60):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.text = "random maze"
		self.path = "img\\menu\\blue_white.png"
		self.sizeFont = 24
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 20, self.y + 18, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def delete(self):
		pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		pygame.display.update()
class StartGame:
	def __init__(self, color_text, colorIn, x = 775, y = 450, x1 = 240, y1 = 60):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.text = "Start Game"
		self.path = "img\\menu\\green.png"
		self.sizeFont = 24
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 30, self.y + 18, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def delete(self):
		pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		pygame.display.update()
class Load:
	def __init__(self, color_text, colorIn, x = 775, y = 530, x1 = 240, y1 = 60):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.text = "Load game"
		self.path = "img\\menu\\yellow.png"
		self.sizeFont = 24
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 40, self.y + 18, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def delete(self):
		pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		pygame.display.update()
class Quit:
	def __init__(self, color_text, colorIn, thickness, x = 775, y = 610, x1 = 240, y1 = 60):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.thickness = thickness
		self.text = "Quit Game"
		self.path = "img\\menu\\red.png"
		self.sizeFont = 24
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 40, self.y + 18, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def delete(self):
		pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		pygame.display.update()
	def delete_down(self):
		pygame.draw.rect(self.screen, self.colorIn, (710 + self.thickness, self.y - 10, 1080 - 710 - 2*self.thickness, 720 - self.y - 2*self.thickness), 0)
		pygame.display.update()
	def notification(self, x = 730, y = 600, size = 20):
		Draw().draw_text("Do you want return menu?", x, y, color.Red, size)
		pygame.display.update()
class YesNo:
	def __init__(self, color_text, colorIn):
		self.screen = const.screen
		self.color_text = color_text
		self.colorIn = colorIn
	def Yes(self, x, y, x1 = 60, y1 = 30, z = 5, h = 7, sizefont = 24):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\green.png", size = (x1, y1))
		Draw().draw_text("Yes", x + z, y + h, self.color_text, sizefont)
		pygame.display.update()
		return k
	def No(self, x, y, x1 = 60, y1 = 30, z = 13, h = 7, sizefont = 24):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\red.png", size = (x1, y1))
		Draw().draw_text("No", x + z, y + h, self.color_text, sizefont)
		pygame.display.update()
		return k

