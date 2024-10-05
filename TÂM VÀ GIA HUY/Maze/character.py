import pygame
import const
from color_maze import Color
import time
import sys
import math
color = Color()
walkRight = [pygame.image.load('img/sprite/right/1.png'), pygame.image.load('img/sprite/right/2.png'), pygame.image.load('img/sprite/right/3.png'), pygame.image.load('img/sprite/right/4.png'), pygame.image.load('img/sprite/right/5.png'), pygame.image.load('img/sprite/right/6.png')]
walkLeft = [pygame.image.load('img/sprite/left/1.png'), pygame.image.load('img/sprite/left/2.png'), pygame.image.load('img/sprite/left/3.png'), pygame.image.load('img/sprite/left/4.png'), pygame.image.load('img/sprite/left/5.png'), pygame.image.load('img/sprite/left/6.png')]
walkUp = [pygame.image.load('img/sprite/up/1.png'), pygame.image.load('img/sprite/up/2.png'), pygame.image.load('img/sprite/up/3.png'), pygame.image.load('img/sprite/up/4.png'), pygame.image.load('img/sprite/up/5.png'), pygame.image.load('img/sprite/up/6.png')]
walkDown = [pygame.image.load('img/sprite/down/1.png'), pygame.image.load('img/sprite/down/2.png'), pygame.image.load('img/sprite/down/3.png'), pygame.image.load('img/sprite/down/4.png'), pygame.image.load('img/sprite/down/5.png'), pygame.image.load('img/sprite/down/6.png')]
charRight = pygame.image.load('img/sprite/standing/1.png')
charLeft = pygame.image.load('img/sprite/standing/2.png')
class Tom:
	def __init__(self, x, y, width, height, cell, thickness, coor, color_delete):
		self.screen = const.screen
		self.cell = cell
		self.thickness = thickness
		self.coor = coor
		self.stack = []
		self.x = x
		self.y = y
		self.color_delete = color_delete
		self.width = width
		self.height = height
		self.left = False
		self.right = False
		self.up = False
		self.down = False
		self.walkCount = 0
		self.last_walk = True
	def draw(self):
		if self.walkCount + 1 >= 12:
			self.walkCount = 0
		if self.left:
			image = pygame.transform.scale(walkLeft[self.walkCount//2], size = (self.width, self.height))
			self.screen.blit(image, (self.x*self.cell + self.thickness + self.coor,self.y*self.cell + self.thickness + self.coor))
			self.walkCount += 1
			self.last_walk = False
		elif self.right:
			image = pygame.transform.scale(walkRight[self.walkCount//2], size = (self.width, self.height))
			self.screen.blit(image, (self.x*self.cell + self.thickness + self.coor,self.y*self.cell + self.thickness + self.coor))
			self.walkCount +=1
			self.last_walk = True
		elif self.up:
			image = pygame.transform.scale(walkUp[self.walkCount//2], size = (self.width, self.height))
			self.screen.blit(image, (self.x*self.cell + self.thickness + self.coor,self.y*self.cell + self.thickness + self.coor))
			self.walkCount +=1
			self.last_walk = True
		elif self.down:
			image = pygame.transform.scale(walkDown[self.walkCount//2], size = (self.width, self.height))
			self.screen.blit(image, (self.x*self.cell + self.thickness + self.coor,self.y*self.cell + self.thickness + self.coor))
			self.walkCount +=1
			self.last_walk = True
		else:
			if self.last_walk:
				char = charRight
			else:
				char = charLeft
			image = pygame.transform.scale(char, size = (self.width, self.height))
			self.screen.blit(image, (self.x*self.cell + self.thickness + self.coor, self.y*self.cell + self.thickness + self.coor))
	def move(self, keys, coordinate):
		if keys[pygame.K_LEFT] and coordinate[self.x, self.y, 0] != -1:
			self.x -= 1
			self.left = True
			self.right = False
			if (self.x, self.y) not in self.stack:
				self.stack.append((self.x, self.y))
			else:
				self.stack.pop()
		elif keys[pygame.K_RIGHT] and coordinate[self.x, self.y, 1] != -1:
			self.x += 1
			self.right = True
			self.left = False
			if (self.x, self.y) not in self.stack:
				self.stack.append((self.x, self.y))
			else:
				self.stack.pop()
		elif keys[pygame.K_UP] and coordinate[self.x, self.y, 2] != -1:
			self.y -= 1
			self.up = True
			self.down = False
			if (self.x, self.y) not in self.stack:
				self.stack.append((self.x, self.y))
			else:
				self.stack.pop()
		elif keys[pygame.K_DOWN] and coordinate[self.x, self.y, 3] != -1:
			self.y += 1
			self.down = True
			self.up = False
			if (self.x, self.y) not in self.stack:
				self.stack.append((self.x, self.y))
			else:
				self.stack.pop()
		else:
			self.right = False
			self.left = False
			self.up = False
			self.down = False
			self.walkCount = 0
	def move_bot(self, backtrack):
		if backtrack[1] == "l":
			self.x -= 1
			self.left = True
			self.right = False
			
		elif backtrack[1] == "r":
			self.x += 1
			self.right = True
			self.left = False
			
		elif backtrack[1] == "u":
			self.y -= 1
			self.up = True
			self.down = False
			
		elif backtrack[1] == "d":
			self.y += 1
			self.down = True
			self.up = False
	def delete(self):
		pygame.draw.rect(self.screen, self.color_delete, (self.x*self.cell + self.thickness + self.coor, self.y*self.cell + self.thickness + self.coor, self.cell - self.thickness, self.cell - self.thickness), 0)
JerryImage = [pygame.image.load("img\\sprite\\jerry\\1.png"), pygame.image.load("img\\sprite\\jerry\\2.png"), pygame.image.load("img\\sprite\\jerry\\3.png"), pygame.image.load("img\\sprite\\jerry\\4.png"), pygame.image.load("img\\sprite\\jerry\\5.png"), pygame.image.load("img\\sprite\\jerry\\6.png"), pygame.image.load("img\\sprite\\jerry\\7.png"), pygame.image.load("img\\sprite\\jerry\\8.png"), pygame.image.load("img\\sprite\\jerry\\9.png")]
class Jerry:
	def __init__(self, x, y, width, height, cell, thickness, coor, color_delete):
		self.screen = const.screen
		self.cell = cell
		self.thickness = thickness
		self.coor = coor
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color_delete = color_delete
		self.count = 0
	def draw(self):
		if self.count + 1 >= 9:
			self.count = 0
		self.count += 0.5
		image = pygame.transform.scale(JerryImage[math.floor(self.count)], size = (self.width, self.height))
		self.screen.blit(image, (self.x*self.cell + self.thickness + self.coor, self.y*self.cell + self.thickness + self.coor))
		pygame.display.update()
	def delete(self):
		pygame.draw.rect(self.screen, self.color_delete, (self.x*self.cell + self.thickness + self.coor, self.y*self.cell + self.thickness + self.coor, self.cell - self.thickness, self.cell - self.thickness), 0)
		

HouseImage = pygame.image.load("img/sprite/house/house.png").convert_alpha()
class House:
	def __init__(self, x, y, width, height, cell, thickness, coor, color_delete):
		self.screen = const.screen
		self.cell = cell
		self.thickness = thickness
		self.coor = coor
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color_delete = color_delete
	def draw(self):
		image = pygame.transform.scale(HouseImage, size = (self.width, self.height))
		self.screen.blit(image, (self.x*self.cell + self.thickness + self.coor, self.y*self.cell + self.thickness + self.coor))
		pygame.display.update()
	def delete(self):
		pygame.draw.rect(self.screen, self.color_delete, (self.x*self.cell + self.thickness + self.coor, self.y*self.cell + self.thickness + self.coor, self.cell - self.thickness, self.cell - self.thickness), 0)
