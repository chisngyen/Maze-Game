import pygame
import time
import sys
import const
from color_maze import Color
from draw_const import Draw
color = Color()

class MenuBot:
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
class AlgorithmMenu:
	def __init__(self,color_text, colorIn, thickness, x = 792, y = 230, x1 = 210, y1 = 50):
		self.screen = const.screen
		self.algorithm = " dfs"
		self.thickness = thickness
		self.colorIn = colorIn
		self.color_text = color_text
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.path = "img\\menu\\blue.png"
		self.path_dfs = "img\\menu\\green1.png"
		self.path_astar = "img\\menu\\yellow.png"
		self.path_bfs = "img\\menu\\red.png"
		self.text = "algorithms"
		self.sizeFont = 24
		self.sizefont = 20
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text(self.text, self.x + 17, self.y + 14, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def draw_text(self):
		Draw().draw_text(self.algorithm, self.x + 79, self.y + 67, self.color_text, self.sizefont)
		pygame.display.update()
	def delete(self):
		pygame.draw.rect(self.screen, self.colorIn, (710 + self.thickness, 270 + self.thickness, 1080 - 710 - 2*self.thickness, 50), 0)
		pygame.display.update()
	def Dfs(self, x = 745, y = 286, x1 = 80, y1 = 40):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_dfs, size = (x1, y1))
		Draw().draw_text("dfs", x + 18, y + 11, self.color_text, self.sizefont)
		pygame.display.update()
		return k
	def Astar(self, x = 855, y = 286, x1 = 80, y1 = 40):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_astar, size = (x1, y1))
		Draw().draw_text("a*", x + 28, y + 11, self.color_text, self.sizefont)
		pygame.display.update()
		return k
	def Bfs(self, x = 964, y = 286, x1 = 80, y1 = 40):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_bfs, size = (x1, y1))
		Draw().draw_text("bfs", x + 18, y + 11, self.color_text, self.sizefont)
		pygame.display.update()
		return k
class Pause:
	def __init__(self, color_text, colorIn, color_pause, color_unpause, thickness):
		self.screen = const.screen
		self.status = True
		self.color_text = color_text
		self.colorIn = colorIn
		self.color_pause = color_pause
		self.color_unpause = color_unpause
		self.path_resume = "img\\menu\\blue_deep.png"
		self.path_save = "img\\menu\\yellow.png"
		self.path_quit = "img\\menu\\red.png"
		self.thickness = thickness
		self.sizeFont = 24
	def draw_p(self, x = 760, y = 420, r = 15):
		pygame.draw.circle(self.screen, self.color_pause, (x, y), r, 0)
		Draw().draw_text("Pause", x - 35, y + 30, self.color_pause, self.sizeFont)
		pygame.display.update()
	def draw_unp(self, x = 748, y = 407, x1 = 10, y1 = 25):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1 + x1 + x1//2, y1), 0)
		pygame.draw.rect(self.screen, self.color_unpause, (x, y, x1, y1), 0)
		pygame.draw.rect(self.screen, self.color_unpause, (x + x1 + x1//2, y, x1, y1), 0)
		pygame.display.update()
		return k
	def delete_pause(self, x = 710, y = 407, x1 = 100, y1 = 80):
		pygame.draw.rect(self.screen, self.colorIn, (710 + self.thickness, y - 5, x1, y1), 0)
		pygame.display.update()
	def resume(self, x = 800, y = 480, x1 = 200, y1 = 50):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_resume, size = (x1, y1))
		Draw().draw_text("resume", x + 45, y + 14, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def save(self, x = 800, y = 540, x1 = 200, y1 = 50):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_save, size = (x1, y1))
		Draw().draw_text("save", x + 60, y + 14, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def quit(self, x = 800, y = 600, x1 = 200, y1 = 50):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, self.path_quit, size = (x1, y1))
		Draw().draw_text("quit", x + 60, y + 14, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def delete_all(self, x = 800, y = 480, x1 = 200):
		pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, 720 - 480 - self.thickness*2), 0)
		pygame.display.update()
	def delete_quit(self, x = 800, y = 600, x1 = 200, y1 = 50):
		pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
		pygame.display.update()
	def notification(self, color_qus = color.Red, x = 770, y = 600, size = 20):
		Draw().draw_text("Do you want return?", x, y, color_qus, size)
		pygame.display.update()
	def delete_noti(self, x = 720, y = 600):
		pygame.draw.rect(self.screen, self.colorIn, (x, y, 350, 110), 0)
		pygame.display.update()

class Speed:
	def __init__(self, color_text, colorIn, color_arrow, x = 720, y = 340, x1 = 100, y1 = 50):
		self.screen = const.screen
		self.path = "img\\menu\\blue_dark.png"
		self.speed = 0.1
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.sizeFont = 24
		self.path_1 = "img\\menu\\green2.png"
		self.path_2 = "img\\menu\\yellow.png"
		self.path_3 = "img\\menu\\orange.png"
		self.color_arrow = color_arrow
		self.color_exp = color.Red
	def draw(self):
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text("SPEED", self.x + 10, self.y + 14, self.color_text, self.sizeFont)
		pygame.display.update()
	def arrow1(self, x = 840, y = 350, z = 25, h = 15):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, z + 15, h + 15), 0)
		Draw().draw_img(x, y, self.path_1, size = (z + 15, h + 15))
		x = x + 8
		y = y + 6
		if self.speed - 0.1 < 0.0000001:
			pygame.draw.polygon(self.screen, self.color_exp, ((x, y), (x, y + h), (x + z, y + h//2)))
		else:
			pygame.draw.polygon(self.screen, self.color_arrow, ((x, y), (x, y + h), (x + z, y + h//2)))
		pygame.display.update()
		return k
	def arrow2(self, x = 920, y = 350, z = 25, h = 15):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, z + 15, h + 15), 0)
		Draw().draw_img(x, y, self.path_2, size = (z + 15, h + 15))
		x = x + 9
		y = y + 6
		if self.speed - 0.01 < 0.0000001:
			pygame.draw.line(self.screen, self.color_exp, (x - 3, y), (x - 3, y + h), 2)
			pygame.draw.polygon(self.screen, self.color_exp, ((x, y), (x, y + h), (x + z, y + h//2)))
		else:
			pygame.draw.line(self.screen, self.color_arrow, (x - 3, y), (x - 3, y + h), 2)
			pygame.draw.polygon(self.screen, self.color_arrow, ((x, y), (x, y + h), (x + z, y + h//2)))
		pygame.display.update()
		return k
	def arrow3(self, x = 1000, y = 350, z = 25, h = 15):
		k = pygame.draw.rect(self.screen, self.colorIn, (x, y, z + 15, h + 15), 0)
		Draw().draw_img(x, y, self.path_3, size = (z + 15, h + 15))
		x = x + 10
		y = y + 6
		if self.speed - 0.00001 < 0.0000001:
			pygame.draw.line(self.screen, self.color_exp, (x - 3, y), (x - 3, y + h), 1)
			pygame.draw.line(self.screen, self.color_exp, (x - 6, y), (x - 6, y + h), 2)
			pygame.draw.polygon(self.screen, self.color_exp, ((x, y), (x, y + h), (x + z, y + h//2)))
		else:
			pygame.draw.line(self.screen, self.color_arrow, (x - 3, y), (x - 3, y + h), 1)
			pygame.draw.line(self.screen, self.color_arrow, (x - 6, y), (x - 6, y + h), 2)
			pygame.draw.polygon(self.screen, self.color_arrow, ((x, y), (x, y + h), (x + z, y + h//2)))
		pygame.display.update()
		return k


