import pygame
import time
import sys
import const
from color_maze import Color
from draw_const import Draw
from create_menu_mini import YesNo
import game
import json
color = Color()
colorIn = color.White
colorBar = color.Black
color_text = color.Black
FONT_14 = 14
FONT_16 = 16
FONT_20 = 20
FONT_24 = 24
def Open_load(account, Fileload, namefile):
	try:
		file = open(namefile, "r")
		data = json.load(file)
		file.close()
		temp = data[account]
		for i, j in temp.items():
			h = j["mode"]
			k = j["level"]
			Fileload.append([i, h, k])
		if len(Fileload) <= 0:
			return False
		else:
			return True
	except:
		return False
def Solve_load(Fileload, x = 770, y = 300, x1 = 100, y1 = 30, color1 = color_text, color2 = colorIn):
	coordinate_space = []
	for j in Fileload:
		i = j[0]
		a = j[1]
		b = j[2]
		k = pygame.draw.rect(const.screen, color2, (x, y, x1, y1), 0)
		Draw().draw_img(x, y, "img\\menu\\yellow.png", size = (x1, y1))
		Draw().draw_text_normal(i, x + 8, y + 6, color1, FONT_20)
		Draw().draw_text_normal(a, x + 8 + 110, y + 6, color1, FONT_20)
		Draw().draw_text_normal(b, x + 8 + 190, y + 6, color1, FONT_20)
		y = y + 50
		coordinate_space.append(k)
		pygame.display.update()
	return coordinate_space
def Table_load(account, x = 740, y = 200, x1 = 310, y1 = 400, color1 = colorIn, color2 = color.Yellow, color3 = color_text):
	Draw().draw_img(x, y, "img\\menu\\credits.png", size = (x1, y1))
	pygame.draw.rect(const.screen, color1, (x + 20, y + 20, x1 - 40, y1 - 40), 0)
	Draw().draw_text(account, 780, 230, color3, FONT_16)
	Draw().draw_text("Load", 880, 225, color3, FONT_24)
	Draw().draw_img(772, 255, "img\\menu\\blue_dark.png", size = (60, 25))
	Draw().draw_text("Name", 780, 260, color2, FONT_14)
	Draw().draw_img(882, 255, "img\\menu\\blue_dark.png", size = (60, 25))
	Draw().draw_text("Mode", 890, 260, color2, FONT_14)
	Draw().draw_img(961, 255, "img\\menu\\blue_dark.png", size = (60, 25))
	Draw().draw_text("Level", 970, 260, color2, FONT_14)
	pygame.display.update()
def Back_load(x = 760, y = 540, x1 = 60, y1 = 30, color1 = color_text, color2 = colorIn):
	k = pygame.draw.rect(const.screen, color2, (x, y, x1, y1), 0)
	Draw().draw_img(x, y, "img\\menu\\red.png", size = (x1, y1))
	Draw().draw_text("Back", x + 9, y + 7, color1, FONT_16)
	pygame.display.update()
	return k

def Is_load(text, x = 778, y = 500, x1 = 140, y1 = 40, color1 = color.Red, color2 = colorIn):
	pygame.draw.rect(const.screen, color2, (x + 100, y, x1, y1), 0)
	Draw().draw_text(text, x + 115, y, color1, FONT_14)
	pygame.display.update()
	
class Oversave_Or_Load:
	def __init__(self, account, namefile, colorIn):
		self.screen = const.screen
		self.namefile = namefile
		self.colorIn = colorIn
		self.account = account
		self.Fileload = []
		self.pos = []
	def solve(self):
		Table_load(self.account)
		temp = Open_load(self.account, self.Fileload, self.namefile)
		index = 0
		if temp:
			while True:
				Table_load(self.account)
				self.pos = Solve_load(self.Fileload)
				b_load = Back_load()
				running = True
				while running:
					true_false_load = []
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_ESCAPE:
								return ""
						if event.type == pygame.QUIT:
							game.Game().quit()
						if event.type == pygame.MOUSEBUTTONDOWN:
							if event.button == 1:
								for i in self.pos:
									if i.collidepoint(event.pos):
										true_false_load.append(True)
									else:
										true_false_load.append(False)
								for i in range(len(true_false_load)):
									if true_false_load[i]:
										Draw().draw_text_normal(self.Fileload[i][0], 778, 6 + 300 + 50*i, color.Red, FONT_20)
										Is_load("Are you sure?", y = 300 + 50*i)
										ye_ = YesNo(color_text, colorIn).Yes(778 + 120, 320 + 50*i, 30, 20, z = 0, h = 4, sizefont = FONT_14)
										no_ = YesNo(color_text, colorIn).No(778 + 200, 320 + 50*i, 30, 20, z = 4, h = 4, sizefont = FONT_14)
										go = True
										while go:
											for event1 in pygame.event.get():
												if event1.type == pygame.MOUSEBUTTONDOWN:
													if event1.button == 1:
														if ye_.collidepoint(event1.pos):
															return self.Fileload[i][0]
														if no_.collidepoint(event1.pos):
															running = False
															go = False
												if event1.type == pygame.QUIT:
													game.Game().quit()
								if b_load.collidepoint(event.pos):
									return ""
		else:
			b_load = Back_load()
			while True:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							if b_load.collidepoint(event.pos):
								return ""
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							return ""
					if event.type == pygame.QUIT:
							game.Game().quit()
	def delete(self):
		pygame.draw.rect(self.screen, self.colorIn, (740, 200, 310, 400), 0)
		pygame.display.update()
