import pygame
import numpy as np
import random
import const
class CreateMaze:
	def __init__(self, size):
		self.size = size
		self.coordinate = -np.ones((size, size, 4), dtype = int)
		self.negative_ones = -np.ones((4), dtype = int)
		self.stack = []
	def create(self):
		x, y = 0, 0
		self.stack.append((x, y))
		while len(self.stack) > 0:
			space = []
			if x + 1 <= self.size - 1 and np.array_equal(self.coordinate[x + 1, y, :], self.negative_ones) and self.coordinate[x + 1, y, 0] == -1:
				space.append("right")
			if x - 1 >= 0 and np.array_equal(self.coordinate[x - 1, y, :], self.negative_ones) and self.coordinate[x - 1, y, 1] == -1:
				space.append("left")
			if y + 1 <= self.size - 1 and np.array_equal(self.coordinate[x, y + 1, :], self.negative_ones) and self.coordinate[x, y + 1, 2] == -1:
				space.append("down")
			if y - 1 >= 0 and np.array_equal(self.coordinate[x, y - 1, :], self.negative_ones) and self.coordinate[x, y - 1, 3] == -1:
				space.append("up")
			if len(space) > 0:
				chosen = (random.choice(space))
				if chosen == "right":
					self.coordinate[x, y, 1] = 0
					self.coordinate[x + 1, y, 0] = 0
					self.stack.append((x + 1, y))
					x = x + 1 
				elif chosen == "left":
					self.coordinate[x, y, 0] = 0
					self.coordinate[x - 1, y, 1] = 0
					self.stack.append((x - 1, y))
					x = x -1
				elif chosen == "down":
					self.coordinate[x, y, 3] = 0
					self.coordinate[x, y + 1, 2] = 0
					self.stack.append((x, y + 1))
					y = y + 1
				elif chosen == "up":
					self.coordinate[x, y, 2] = 0
					self.coordinate[x, y - 1, 3] = 0
					self.stack.append((x, y - 1))
					y = y - 1
			else:
				x, y = self.stack.pop()
	def destroy(self):
		quantity = self.size*self.size//5
		temp = []
		while len(temp) < quantity:
			x = random.randint(1, self.size - 2)
			y = random.randint(1, self.size - 2)
			if (x, y) not in temp:
				temp.append((x, y))
		for i in temp:
			num = random.randint(0, 3)
			if num == 0:
				self.coordinate[i[0], i[1], 0] = 0
				self.coordinate[i[0] - 1, i[1], 1] = 0
			elif num == 1:
				self.coordinate[i[0], i[1], 1] = 0
				self.coordinate[i[0] + 1, i[1], 0] = 0
			elif num == 2:
				self.coordinate[i[0], i[1], 2] = 0
				self.coordinate[i[0], i[1] - 1, 3] = 0
			elif num == 3:
				self.coordinate[i[0], i[1], 3] = 0
				self.coordinate[i[0], i[1] + 1, 2] = 0
class DrawMaze:
	def __init__(self, x, y):
		self.screen = const.screen
		self.x = x
		self.y = y
	def draw(self, coordinate, cell, thickness, color_wall, color_road):
		size = coordinate.shape[0]
		pygame.draw.rect(self.screen, color_wall, (self.x, self.y, size*cell + self.x, size*cell + self.y))
		for i in range(size):
			for j in range(size):
				if coordinate[i, j, 0] == 0:
					pygame.draw.rect(self.screen, color_road, (i*cell - cell + thickness + self.x, j*cell + thickness + self.y, 2*cell - thickness, cell - thickness), 0)
				if coordinate[i, j, 1] == 0:
					pygame.draw.rect(self.screen, color_road, (i*cell + thickness + self.x, j*cell + thickness + self.y, 2*cell - thickness, cell - thickness), 0)
				if coordinate[i, j, 2] == 0:
					pygame.draw.rect(self.screen, color_road, (i*cell + thickness + self.x, j*cell - cell + thickness + self.y, cell - thickness, 2*cell - thickness), 0)
				if coordinate[i, j, 3] == 0:
					pygame.draw.rect(self.screen, color_road, (i*cell +  thickness + self.x, j*cell + thickness + self.y, cell - thickness, 2*cell - thickness), 0)
		pygame.display.update()
	def delete(self, size, cell, thickness, color_delete):
		size = coordinate.shape[0]
		pygame.draw.rect(self.screen, color_delete, (self.x, self.y, size*cell + self.x, size*cell + self.y))
	def delete_all(self, coordinate, coor, cell, thickness, color_delete):
		size = coordinate.shape[0]
		pygame.draw.rect(self.screen, color_delete, (0 + coor, 0 + coor, size*cell + thickness, size*cell + thickness))





