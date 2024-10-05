import pygame
import time
import sys
import const
from color_maze import Color
from draw_const import Draw
color = Color()

class MenuPlayer:
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
def Solve_time(time_begin, times, lost_time):
		temp = time.time()
		time_total = round(temp - time_begin + times - lost_time)
		minutes = time_total//60
		sec = time_total%60
		string = ""
		if minutes <= 9:
			string += "0"
			if minutes <= 0:
				string += "0:"
			else:
				string += str(minutes)
				string += ":"
		else:
			string += str(minutes)
			string += ":"
		if sec <= 9:
			string += "0"
			if sec <= 0:
				string += "0"
			else:
				string += str(sec)
		else:
			string += str(sec)
		return string, time_total
	
def draw_table(x = 770, y = 230, x1 = 250, y1 = 120):
	Draw().draw_img(x, y, "img\\menu\\credits.png", size = (x1, y1))
	pygame.display.update()
def draw_text(string_time, x = 800, y = 260, color_time = color.Yellow, sizeFont = 70):
	Draw().draw_text(string_time, x, y, color_time, sizeFont)
	pygame.display.update()
class TimeTable:
	def __init__(self, time_begin, times = 0, time_total = 0, lost_time = 0):
		self.screen = const.screen
		self.time_total = time_total
		self.time_dilay = time_total - 1
		self.times = times
		self.time_begin = time_begin
		self.lost_time = lost_time
		self.string_time = "00:00"
	def draw(self):
		self.string_time, self.time_total = Solve_time(self.time_begin, self.times, self.lost_time)
		if self.time_dilay != self.time_total:
			self.time_dilay = self.time_total
			draw_table()
			draw_text(self.string_time)
class Suggest:
	def __init__(self, color_text, colorIn, x = 720, y = 370, x1 = 140, y1 = 40):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.path = "img\\menu\\blue_white.png"
		self.sizeFont = 24
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text("Suggest", self.x + 10, self.y + 10, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def delete(self):
		pygame.display.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		pygame.display.update()
class Tab:
	def __init__(self, color_text, colorIn, x = 720, y = 420, x1 = 140, y1 = 40):
		self.screen = const.screen
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.color_text = color_text
		self.colorIn = colorIn
		self.path = "img\\menu\\blue_white.png"
		self.path_resume = "img\\menu\\blue_deep.png"
		self.path_save = "img\\menu\\yellow.png"
		self.path_quit = "img\\menu\\red.png"
		self.sizeFont = 24
	def draw(self):
		k = pygame.draw.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
		Draw().draw_img(self.x, self.y, self.path, size = (self.x1, self.y1))
		Draw().draw_text("Tab", self.x + 43, self.y + 10, self.color_text, self.sizeFont)
		pygame.display.update()
		return k
	def delete(self):
		pygame.display.rect(self.screen, self.colorIn, (self.x, self.y, self.x1, self.y1), 0)
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
	def delete_all(self, x = 800, y = 480, x1 = 200, y1 = 180):
		pygame.draw.rect(self.screen, self.colorIn, (x, y, x1, y1), 0)
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
