import pygame
import time
import sys
import const
from color_maze import Color
from draw_const import Draw
color = Color()
def Is_instack(x, y, stack):
	for i in stack:
		if (x, y) == i[0]:
			return False
	return True
def Hx(x, y, finish_point):
	sum_ = abs(x - finish_point[0]) + abs(y - finish_point[1])
	return sum_
def Draw_point(x, y, color, thicknes, cell, coor):
	pygame.draw.rect(const.screen, color, (x*cell + thicknes + coor, y*cell + thicknes + coor, cell - thicknes, cell - thicknes), 0)
	pygame.display.update()
class Algorithm:
	def __init__(self, coordinate, stack, main_pos, tom_pos, house_pos, jerry_pos, cell, thickness, coor, color_scan, color_backtrack):
		self.screen = const.screen
		self.coordinate = coordinate
		self.stack = stack
		self.main_pos = main_pos
		self.tom_pos = tom_pos
		self.house_pos = house_pos
		self.jerry_pos = jerry_pos
		self.cell = cell
		self.thickness = thickness
		self.coor = coor
		self.color_scan = color_scan
		self.color_backtrack = color_backtrack
		self.count = 0 
	def dfs(self):
		x, y = self.main_pos
		if (x, y) == self.house_pos and self.coordinate[x, y, :].tolist().count(1) == 0:
			if self.coordinate[x, y, 0] == 0:
				self.stack.append(((x - 1, y), 1, 1))
			if self.coordinate[x, y, 1] == 0:
				self.stack.append(((x + 1, y), 0, 1))
			if self.coordinate[x, y, 2] == 0:
				self.stack.append(((x, y - 1), 3, 1))
			if self.coordinate[x, y, 3] == 0:
				self.stack.append(((x, y + 1), 2, 1))
		while (x, y) != self.jerry_pos:
			temp = self.stack.pop()
			x, y = temp[0]
			self.coordinate[x, y, temp[1]] = 1
			if self.coordinate[x, y, 0] == 0 and self.coordinate[x - 1, y, :].tolist().count(1) == 0 and Is_instack(x - 1, y, self.stack):
				self.stack.append(((x - 1, y), 1, temp[2] + 1))
			if self.coordinate[x, y, 1] == 0 and self.coordinate[x + 1, y, :].tolist().count(1) == 0 and Is_instack(x + 1, y, self.stack):
				self.stack.append(((x + 1, y), 0, temp[2] + 1))
			if self.coordinate[x, y, 2] == 0 and self.coordinate[x, y - 1, :].tolist().count(1) == 0 and Is_instack(x, y - 1, self.stack):
				self.stack.append(((x, y - 1), 3, temp[2] + 1))
			if self.coordinate[x, y, 3] == 0 and self.coordinate[x, y + 1, :].tolist().count(1) == 0 and Is_instack(x, y + 1, self.stack):
				self.stack.append(((x, y + 1), 2, temp[2] + 1))
			return (x, y)
	def astar(self):
		x, y = self.main_pos
		if (x, y) == self.house_pos and self.coordinate[x, y, :].tolist().count(1) == 0:
			if self.coordinate[x, y, 0] == 0:
				self.stack.append(((x - 1, y), 1, 1))
			if self.coordinate[x, y, 1] == 0:
				self.stack.append(((x + 1, y), 0, 1))
			if self.coordinate[x, y, 2] == 0:
				self.stack.append(((x, y - 1), 3, 1))
			if self.coordinate[x, y, 3] == 0:
				self.stack.append(((x, y + 1), 2, 1))
		min_ = self.stack[0][2] + Hx(self.stack[0][0][0], self.stack[0][0][1], self.jerry_pos)
		index = 0
		while (x, y) != self.jerry_pos:
			for i, j in enumerate(self.stack):
				fx = j[2] + Hx(j[0][0], j[0][1], self.jerry_pos)
				if fx <= min_:
					min_ = fx
					index = i
			temp = self.stack.pop(index)
			x, y = temp[0]
			self.coordinate[x, y, temp[1]] = 1
			if self.coordinate[x, y, 0] == 0 and self.coordinate[x - 1, y, :].tolist().count(1) == 0 and Is_instack(x - 1, y, self.stack):
				self.stack.append(((x - 1, y), 1, temp[2] + 1))
			if self.coordinate[x, y, 1] == 0 and self.coordinate[x + 1, y, :].tolist().count(1) == 0 and Is_instack(x + 1, y, self.stack):
				self.stack.append(((x + 1, y), 0, temp[2] + 1))
			if self.coordinate[x, y, 2] == 0 and self.coordinate[x, y - 1, :].tolist().count(1) == 0 and Is_instack(x, y - 1, self.stack):
				self.stack.append(((x, y - 1), 3, temp[2] + 1))
			if self.coordinate[x, y, 3] == 0 and self.coordinate[x, y + 1, :].tolist().count(1) == 0 and Is_instack(x, y + 1, self.stack):
				self.stack.append(((x, y + 1), 2, temp[2] + 1))
			return (x, y)
	def bfs(self):
		x, y = self.main_pos
		if (x, y) == self.house_pos and self.coordinate[x, y, :].tolist().count(1) == 0:
			if self.coordinate[x, y, 0] == 0:
				self.stack.append(((x - 1, y), 1, 1))
			if self.coordinate[x, y, 1] == 0:
				self.stack.append(((x + 1, y), 0, 1))
			if self.coordinate[x, y, 2] == 0:
				self.stack.append(((x, y - 1), 3, 1))
			if self.coordinate[x, y, 3] == 0:
				self.stack.append(((x, y + 1), 2, 1))
		while (x, y) != self.jerry_pos:
			temp = self.stack.pop(0)
			x, y = temp[0]
			self.coordinate[x, y, temp[1]] = 1
			if self.coordinate[x, y, 0] == 0 and self.coordinate[x - 1, y, :].tolist().count(1) == 0 and Is_instack(x - 1, y, self.stack):
				self.stack.append(((x - 1, y), 1, temp[2] + 1))
			if self.coordinate[x, y, 1] == 0 and self.coordinate[x + 1, y, :].tolist().count(1) == 0 and Is_instack(x + 1, y, self.stack):
				self.stack.append(((x + 1, y), 0, temp[2] + 1))
			if self.coordinate[x, y, 2] == 0 and self.coordinate[x, y - 1, :].tolist().count(1) == 0 and Is_instack(x, y - 1, self.stack):
				self.stack.append(((x, y - 1), 3, temp[2] + 1))
			if self.coordinate[x, y, 3] == 0 and self.coordinate[x, y + 1, :].tolist().count(1) == 0 and Is_instack(x, y + 1, self.stack):
				self.stack.append(((x, y + 1), 2, temp[2] + 1))
			return (x, y)
	def draw_scan(self):
		size = self.coordinate.shape[0]
		for i in range(size):
			for j in range(size):
				if ((i, j) != self.house_pos or (i, j) != self.jerry_pos) and self.coordinate[i, j, :].tolist().count(1) >=1:
					pygame.draw.rect(self.screen, self.color_scan, (i*self.cell + self.thickness + self.coor, j*self.cell + self.thickness + self.coor, self.cell - self.thickness, self.cell - self.thickness))
	def back_track(self):
		x, y = self.jerry_pos
		temp = []
		while (x, y) != self.house_pos:
			Draw_point(x, y, self.color_backtrack, self.thickness, self.cell, self.coor)
			if self.coordinate[x, y, 0] == 1:
				x = x - 1
				temp.append(((x, y), "r"))
			elif self.coordinate[x, y, 1] == 1:
				x = x + 1
				temp.append(((x, y), "l"))
			elif self.coordinate[x, y, 2] == 1:
				y = y - 1
				temp.append(((x, y), "d"))
			elif self.coordinate[x, y, 3] == 1:
				y = y + 1
				temp.append(((x, y), "u"))
		return temp

		