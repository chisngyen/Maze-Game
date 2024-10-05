import pygame
import sys
import json
import time
from create_maze import *
import const, game
from control_maze import Control
import random_point
from character import *
from color_maze import Color
from create_menu_mini import *
from create_save import *
from draw_const import Draw
from create_menu_player import *
from create_menu_bot import *
from algorithm import Algorithm
from create_win import Win

namefile = "data.json"

color = Color()

FONT_14 = 14
FONT_16 = 16
FONT_20 = 20
FONT_24 = 24
FONT_30 = 30
FONT_70 = 70

color_wall = color.Black
color_road = color.White
colorBar = color.Black
colorIn = color.Silver_light
color_text = color.Black
color_text_level = color.Black
color_text_mode = color.Black
color_text_spawn = color.Black
color_text_randmaze = color.Black
color_text_start = color.Black
color_text_load = color.Black
color_text_quit = color.Black
color_delete = color.White
color_delete_maze = color.Black
color_text_yesno = color.Black
color_text_suggest = color.Black
color_text_tab = color.Black
color_backtrack = color.Teal
color_scan = color.Teal
Control = Control()
DrawMaze = DrawMaze(Control.coor, Control.coor)
TableMenu = TableMenu(Control.thickness_bar, colorBar, colorIn)
Level = Level(color_text_level, colorIn, Control.thickness_bar, Control.level)
Mode = Mode(color_text_mode, colorIn, Control.thickness_bar, Control.mode)
Spawn = Spawn(color_text_spawn, colorIn, Control.thickness_bar)
RandMaze = RandMaze(color_text_randmaze, colorIn)
StartGame = StartGame(color_text_start, colorIn)
Load = Load(color_text_load, colorIn)
Quit = Quit(color_text_quit, colorIn, Control.thickness_bar)
YesNo = YesNo(color_text_yesno, colorIn)
Win = Win(color_text, color.Gray)

Tom = Tom(0, 0, 28, 28, Control.cell, Control.thickness, Control.coor, color_delete)
House = House(0, 0, 28, 28, Control.cell, Control.thickness, Control.coor, color_delete)
Jerry = Jerry(0, 0, 28, 28, Control.cell, Control.thickness, Control.coor, color_delete)
def Delete_draw(x, y, size1, size2, color):
	pygame.draw.rect(const.screen, color, (x, y, size1, size2), 0)
	pygame.display.update()
def createMaze(size):
	newmaze = CreateMaze(size)
	newmaze.create()
	newmaze.destroy()
	return newmaze.coordinate
def level():
	easy_pos = Level.easy()
	medium_pos = Level.medium()
	hard_pos = Level.hard()
	return easy_pos, medium_pos, hard_pos
def mode():
	player_pos = Mode.player()
	bot_pos = Mode.bot()
	return player_pos, bot_pos
def spawn():
	rand_pos = Spawn.random()
	mouse_pos = Spawn.mouse()
	return rand_pos, mouse_pos
def tranform_data():
	Tom.cell = Control.cell
	Tom.thickness = Control.thickness
	Tom.width = Control.cell - Control.thickness
	Tom.height = Control.cell - Control.thickness
	House.cell = Control.cell
	House.thickness = Control.thickness
	House.width = Control.cell - Control.thickness
	House.height = Control.cell - Control.thickness
	Jerry.cell = Control.cell
	Jerry.thickness = Control.thickness
	Jerry.width = Control.cell - Control.thickness
	Jerry.height = Control.cell - Control.thickness

def Solve_mouse(mouse, size, cell, thicknes, coor):
	if mouse[0] <= coor or mouse[1] <= coor or mouse[0] > size*cell + thicknes + coor or mouse[1] > size*cell + thicknes + coor:
		return False
	else:
		return True
def mouse_choice(size, cell, thickness, coor):
	pos_begin_Tom = (Tom.x, Tom.y)
	pos_begin_House = (House.x, House.y)
	pos_begin_Jerry = (Jerry.x, Jerry.y)
	Spawn.delete()
	Spawn.notification()
	count = 0
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.Game().quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if Solve_mouse(event.pos, size, cell, thickness, coor):
						if count == 0:
							Tom.delete()
							House.delete()
							House.x = (event.pos[0] - thickness - coor)//cell
							House.y = (event.pos[1] - thickness - coor)//cell
							Tom.x, Tom.y = House.x, House.y
							Tom.draw()
							House.draw()
							count += 1
						else:
							Jerry.delete()
							Jerry.x = (event.pos[0] - thickness - coor)//cell
							Jerry.y = (event.pos[1] - thickness - coor)//cell
							if (Jerry.x, Jerry.y) == (House.x, House.y):
								Spawn.delete()
								Spawn.error()
								time.sleep(1)
								Spawn.delete()
								Spawn.notification()
								Tom.delete()
								House.delete()
								Jerry.delete()
								(Tom.x, Tom.y) = pos_begin_Tom
								(House.x, House.y) = pos_begin_House
								(Jerry.x, Jerry.y) = pos_begin_Jerry
								Tom.draw()
								House.draw()
								Jerry.draw()
							else:
								Spawn.delete()
								Tom.draw()
								House.draw()
								Jerry.draw()
								Control.tom = (Tom.x, Tom.y)
								Control.House = (House.x, House.y)
								Control.Jerry = (Jerry.x, Jerry.y)
								running = False
	Spawn.draw()
	Spawn.random()
	Spawn.mouse()

def readdata(namefile):
	file = open(namefile, "r")
	data = json.load(file)
	file.close()
	return data

def Back_game(x, y, x1, y1, size_font, color1 = colorIn, color2 = color_text):
	k = pygame.draw.rect(const.screen, color1, (x, y, x1, y1), 0)
	Draw().draw_img(x, y, "img\\menu\\green1.png", size = (x1, y1))
	Draw().draw_text("Back", x + 6, y + 7, color2, size_font)
	pygame.display.update()
	return k
def Is_save(name, account, x = 730, y = 600, x1 = 60, y1 = 30, color1 = color.Blue, color2 = colorIn, color3 = color_text):
	Draw().draw_text("One account can only save five files.", x, y, color1, FONT_14)
	Draw().draw_text("Do you want to save insert files?", x, y + 30, color1, FONT_14)
	ye_ = YesNo.Yes(x + 60, y + 70, x1, y1)
	no_ = YesNo.No(x + 230, y + 70, x1, y1)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.Game().quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if ye_.collidepoint(event.pos):
						Delete_draw(720, 200, 350, 500, colorIn)
						load_game_name = Oversave_Or_Load(account, namefile, colorIn).solve()
						
						if len(load_game_name) <= 0:
							Delete_draw(720, 600, 350, 100, colorIn)
							Draw().draw_text("Save is failure", x, 600, color.Red, FONT_20)
							pygame.display.update()
							time.sleep(1)
							Delete_draw(720, 200, 350, 500, colorIn)
							return False
						else:
							Delete_draw(720, 200, 350, 500, colorIn)
							file = open(name, "r")
							data = json.load(file)
							file.close()
							data_side = data[account]
							data_side.pop(load_game_name)
							with open(name, "w") as file_:
								json.dump(data, file_, indent = 4)
							return True
					if no_.collidepoint(event.pos):
						Delete_draw(720, 600, 350, 100, colorIn)
						Draw().draw_text("Save is failure", x, 600, color.Red, FONT_20)
						pygame.display.update()
						time.sleep(1)
						Delete_draw(720, 600, 350, 100, colorIn)
						return False
def Find(account, namelink, nameFile, x = 730, y = 600, color1 = color.Red):
	try:
		count = 0
		file = open(namelink, "r")
		data = json.load(file)
		file.close()
		data_side = data[account]
		for i, j in data_side.items():
			count += 1
			if i == nameFile:
				Draw().draw_text("Error: name already exists", x, y, color1, FONT_16)
				pygame.display.update()
				time.sleep(1)
				Delete_draw(720, 600, 350, 100, colorIn)
				return False
		if count >= 5:
			kq = Is_save(namelink, account)
			if kq == False:
				return False
		return True
	except:
		print("error")
		return True
def Select_name(x = 730, y = 600, x1 = 120, y1 = 30, color1 = colorIn, color2 = color_text):
	k = pygame.draw.rect(const.screen, color1, (x + 140, y, x1, y1), 2)
	Draw().draw_img(x + 140, y, "img\\menu\\green1.png", size = (x1, y1))
	pygame.draw.rect(const.screen, colorIn, (x + 140 + 4, y + 4, x1 - 8, y1 - 8), 0)
	Draw().draw_text("Select name: ", x, y + 10, color2, FONT_16)
	pygame.display.update()
	return k
def Input_name(color1 = color_text, color2 = color.Blue, color3 = colorIn, color4 = color.Red):
	Delete_draw(720, 600, 350, 100, colorIn)
	k1 = Back_game(750, 640, 60, 30, FONT_20)
	k2 = Select_name()
	go = True
	while go:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.Game().quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if k1.collidepoint(event.pos):
						Delete_draw(720, 600, 350, 100, color3)
						string = ""
						return string
					if k2.collidepoint(event.pos):
						Select_name(color2 = color4)
						string = ""
						namefile = ""
						running = True
						while running:
							for event_ in pygame.event.get():
								if event_.type == pygame.QUIT:
									pygame.quit()
									sys.exit()
								if event_.type == pygame.MOUSEBUTTONDOWN:
									if event_.button == 1:
										if k1.collidepoint(event_.pos):
											Delete_draw(720, 600, 350, 100, color3)
											string = ""
											return string
								if event_.type == pygame.KEYDOWN:
									if event_.key == pygame.K_BACKSPACE:
										if len(string) > 0:
											string = string[:-1]
											Delete_draw(875, 604, 110, 20, color3)
											Draw().draw_text_normal(string, 875, 608, color1, FONT_20)
											pygame.display.update()

									if event_.key == pygame.K_RETURN:
										namefile = string
										if len(namefile) <= 0:
											string = ""
											Delete_draw(871, 590, 110, 22, color3)
										else:
											Delete_draw(720, 600, 350, 100, color3)
											return namefile
									else:
										if len(string) <= 10 and ((event_.key >= 65 and event_.key <= 90) or (event_.key >= 97 and event_.key <= 122)):
											string += chr(event_.key)
											Draw().draw_text_normal(string, 875, 608, color1, FONT_20)
											pygame.display.update()

def search(data, account):
	for i, j in data.items():
		if account == i:
			return True
	return False

def Save_game(account, coordinate_space, main_point, begin_point, end_point, nameFile, daytime, times, stack, mode, level, name = "data.json"):
	try:
		dic = {nameFile: {"main": main_point, "begin": begin_point, "finish": end_point, "time": daytime, "times": times, "stack": stack, "mode": mode, "level": level, "data": coordinate_space}}
		file = open(name, "r")
		data = json.load(file)
		if search(data, account):
			data[account].update(dic)
		else:
			data[account] = dic
		file.close()
		with open(name, "w") as fileData:
			json.dump(data, fileData, indent = 4)
	except:
		file = open(name, "w")
		json.dump({account: {nameFile: {"main": main_point, "begin": begin_point, "finish": end_point, "time": daytime, "times": times, "stack": stack, "mode": mode, "level": level, "data": coordinate_space}}}, file, indent = 4)
		file.close()

def Draw_point(x, y, color, thicknes, cell, coor):
	pygame.draw.rect(const.screen, color, (x*cell + thicknes + coor, y*cell + thicknes + coor, cell - thicknes, cell - thicknes), 0)
	pygame.display.update()
def Suggest_solve(coordinate_space):
	coordinate_space_copy = coordinate_space.copy()
	algo = Algorithm(coordinate_space_copy, [], (Tom.x, Tom.y), (Tom.x, Tom.y), (Tom.x, Tom.y), (Jerry.x, Jerry.y), Control.cell, Control.thickness, Control.coor, color.Yellow, color.Red)
	x, y = (Tom.x, Tom.y)
	while (x, y) != (Jerry.x, Jerry.y):
		x, y = algo.astar()
		algo.main_pos = (x, y)
	a, b = (Jerry.x, Jerry.y)
	Draw_point(a, b, color_backtrack, Control.thickness, Control.cell, Control.coor)
	kq = []
	kq.append((a, b))
	while (a, b) != (Tom.x, Tom.y):
		if algo.coordinate[a, b, 0] == 1:
			a = a - 1
			kq.append((a, b))
		elif algo.coordinate[a, b, 1] == 1:
			a = a + 1
			kq.append((a, b))
		elif algo.coordinate[a, b, 2] == 1:
			b = b - 1
			kq.append((a, b))
		elif algo.coordinate[a, b, 3] == 1:
			b = b + 1
			kq.append((a, b))
		Draw_point(a, b, color_backtrack, Control.thickness, Control.cell, Control.coor)
	return kq

def Rank_save(account, level, time_total, namefile = "rank.json"):
	try:
		file = open(namefile, "r")
		data = json.load(file)
		file.close()
		exist = True
		for i, j in data.items():
			if i == account:
				exist = False
		if exist:
			data[account] = {"level": [level], "time": [time_total]}
		else:
			data[account]["level"].append(level)
			data[account]["time"].append(time_total)
		with open(namefile, "w") as w_file:
			json.dump(data, w_file, indent = 4)
	except:
		temp1 = []
		temp2 = []
		temp1.append(level)
		temp2.append(time_total)
		data = {account: {"level": temp1, "time": temp2}}
		with open(namefile, "w") as w_file:
			json.dump(data, w_file, indent = 4)

def player(maze, account):
	Level.draw()
	Level.draw_text()
	Mode.draw()
	Mode.draw_text()
	time_begin = time.time()
	table = TimeTable(time_begin, times = Control.time)
	suggest = Suggest(color_text_suggest, colorIn)
	tab = Tab(color_text_tab, colorIn)
	sug_pos = suggest.draw()
	tab_pos = tab.draw()
	click_tab = False
	running = True
	timelost = 0
	k = []
	while running:
		keys = pygame.key.get_pressed()
		Tom.delete()
		Jerry.delete()
		House.delete()
		Tom.move(keys, maze)
		Control.tom = (Tom.x, Tom.y) 
		Tom.draw()
		Jerry.draw()
		House.draw()
		table.draw()
		time.sleep(0.1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.Game().quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE:
					click_tab = True
					break
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if sug_pos.collidepoint(event.pos):
						if len(k) > 0:
							for i in k:
								x, y = i
								Draw_point(x, y, color_road, Control.thickness, Control.cell, Control.coor)
							k = []
						else:
							k = Suggest_solve(maze)
						Tom.draw()
						House.draw()
						Jerry.draw()
					if tab_pos.collidepoint(event.pos):
						click_tab = True
						break
		if click_tab:
			click_tab = False
			resume_pos = tab.resume()
			save_pos = tab.save()
			quit_pos = tab.quit()
			run = True
			time_lost_begin = time.time()
			while run:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE:
							tab.delete_all()
							run = False
					if event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							if tab_pos.collidepoint(event.pos):
								tab.delete_all()
								run = False
							if resume_pos.collidepoint(event.pos):
								tab.delete_all()
								run = False
							if save_pos.collidepoint(event.pos):
								tab.delete_quit()
								named_tuple = time.localtime()
								daytime = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
								arr = maze.tolist()
								nameFile = Input_name()
								if len(nameFile) > 0:
									if Find(account, "data.json", nameFile):
										Save_game(account, arr, (Tom.x, Tom.y), (House.x, House.y), (Jerry.x, Jerry.y), nameFile, daytime, table.time_total, Tom.stack, "Player", Control.level)
										Delete_draw(720, 600, 350, 100, colorIn)
										Draw().draw_text("Save is success", 740, 620, color.Green, FONT_20)
										pygame.display.update()
										time.sleep(1)
										Delete_draw(720, 600, 350, 100, colorIn)
								tab.delete_all()
								run = False
								suggest.draw()
								tab.draw()
							if quit_pos.collidepoint(event.pos):
								tab.delete_quit()
								tab.notification()
								yes = YesNo.Yes(800, 650)
								no = YesNo.No(930, 650)
								yesno = True
								while yesno:
									for event_yesno in pygame.event.get():
										if event_yesno.type == pygame.QUIT:
											pygame.quit()
											sys.exit()
										if event_yesno.type == pygame.MOUSEBUTTONDOWN:
											if event_yesno.button == 1:
												if yes.collidepoint(event_yesno.pos):
													yesno = False
													run = False
													running = False
													Control.back_win[1] = True
													TableMenu.delete()
												if no.collidepoint(event_yesno.pos):
													tab.delete_noti()
													tab.quit()
													yesno = False
			time_lost_end = time.time()
			timelost += time_lost_end - time_lost_begin
			table.lost_time = timelost

		if (Tom.x, Tom.y) == (Jerry.x, Jerry.y):
			Win.Win_game()
			Rank_save(account, Control.level, table.time_total)
			Win.Score_time(table.string_time)
			new_pos = Win.New_game()
			restart = Win.Restart_game()
			quit_pos = Win.Quit_game()
			run = True
			while run:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							if new_pos.collidepoint(event.pos):
								Control.back_win[0] = True
								table.time_total = 0
								run = False
							if restart.collidepoint(event.pos):
								Control.back_win[1] = True
								table.time_total = 0
								run = False
							if quit_pos.collidepoint(event.pos):
								Control.back_win[2] = True
								run = False
			running = False
	Tom.stack = []

def bot(account, maze):
	Level.draw()
	Level.draw_text()
	Mode.draw()
	Mode.draw_text()
	Algorithms = AlgorithmMenu(color_text, colorIn, Control.thickness_bar)
	main_pos  = (Tom.x, Tom.y)
	algorithm = Algorithm(maze, Tom.stack, main_pos, (Tom.x, Tom.y), (House.x, House.y), (Jerry.x, Jerry.y), Control.cell, Control.thickness, Control.coor, color_scan, color.Red)
	alg = Algorithms.draw()
	Algorithms.draw_text()
	Pauses = Pause(color_text, colorIn, color.Red, color.Black, Control.thickness_bar)
	pause_pos = Pauses.draw_unp()
	Pauses.delete_pause()
	Pauses.draw_p()
	resume_pos = Pauses.resume()
	save_pos = Pauses.save()
	quit_pos = Pauses.quit()
	Speeds = Speed(color_text, colorIn, color.Black)
	Speeds.draw()
	arr1 = Speeds.arrow1()
	arr2 = Speeds.arrow2()
	arr3 = Speeds.arrow3()
	if len(algorithm.stack) > 0:
		algorithm.draw_scan()
	pygame.display.update()
	pause = True
	running = True
	while running:
		time.sleep(Speeds.speed)
		if main_pos == (Jerry.x, Jerry.y):
			backtrack = algorithm.back_track()
			while len(backtrack) > 0:
				temp = backtrack.pop()
				if len(backtrack) > 0:
					temp1 = backtrack[-1]
					Draw_point(temp1[0][0], temp1[0][1], color_road, Control.thickness, Control.cell, Control.coor)
				Tom.delete()
				Tom.move_bot(temp)
				Tom.draw()
				House.draw()
				Jerry.delete()
				Jerry.draw()
				time.sleep(Speeds.speed)
			Jerry.draw()
			time.sleep(1)
			Win.Win_game()
			new_pos = Win.New_game()
			restart = Win.Restart_game()
			quit_pos = Win.Quit_game()
			run = True
			while run:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							if new_pos.collidepoint(event.pos):
								Control.back_win[0] = True
								run = False
							if restart.collidepoint(event.pos):
								Control.back_win[1] = True
								run = False
							if quit_pos.collidepoint(event.pos):
								Control.back_win[2] = True
								run = False
			algorithm.stack = []
			running = False
		if running == False:
			break
		if pause == False:
			if Algorithms.algorithm == " dfs":
				main_pos = algorithm.dfs()
				algorithm.main_pos = main_pos
				Draw_point(main_pos[0], main_pos[1], color_scan, Control.thickness, Control.cell, Control.coor)
			elif Algorithms.algorithm == " bfs":
				main_pos = algorithm.bfs()
				algorithm.main_pos = main_pos
				Draw_point(main_pos[0], main_pos[1], color_scan, Control.thickness, Control.cell, Control.coor)
			else:
				main_pos = algorithm.astar()
				algorithm.main_pos = main_pos
				Draw_point(main_pos[0], main_pos[1], color_scan, Control.thickness, Control.cell, Control.coor)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.Game().quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
					if pause:
						Pauses.delete_pause()
						Pauses.delete_all()
						Pauses.draw_unp()
						pause = False
					else:
						Pauses.delete_pause()
						Pauses.delete_all()
						Pauses.draw_p()
						Pauses.resume()
						Pauses.save()
						Pauses.quit()
						pause = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if resume_pos.collidepoint(event.pos) and pause:
						Pauses.delete_pause()
						Pauses.delete_all()
						Pauses.draw_unp()
						pause = False
					if save_pos.collidepoint(event.pos) and pause:
						Pauses.delete_quit()
						named_tuple = time.localtime()
						daytime = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
						arr = maze.tolist()
						nameFile = Input_name()
						if len(nameFile) > 0:
							if Find(account, "data.json", nameFile):
								Save_game(account, arr, (Tom.x, Tom.y), (House.x, House.y), (Jerry.x, Jerry.y), nameFile, daytime, 0, algorithm.stack, "  bot", Control.level)
								Delete_draw(720, 600, 350, 100, colorIn)
								Draw().draw_text("Save is success", 740, 620, color.Green, FONT_20)
								pygame.display.update()
								time.sleep(1)
								Delete_draw(720, 600, 350, 100, colorIn)
						Pauses.delete_all()
						Pauses.resume()
						Pauses.save()
						Pauses.quit()
					if quit_pos.collidepoint(event.pos) and pause:
						Pauses.delete_quit()
						Pauses.notification()
						yes = YesNo.Yes(800, 650)
						no = YesNo.No(930, 650)
						yesno = True
						while yesno:
							for event_yesno in pygame.event.get():
								if event_yesno.type == pygame.QUIT:
									pygame.quit()
									sys.exit()
								if event_yesno.type == pygame.MOUSEBUTTONDOWN:
									if event_yesno.button == 1:
										if yes.collidepoint(event_yesno.pos):
											yesno = False
											running = False
											Control.back_win[1] = True
											TableMenu.delete()
										if no.collidepoint(event_yesno.pos):
											Pauses.delete_noti()
											Pauses.quit()
											yesno = False

					if pause_pos.collidepoint(event.pos):
						if pause:
							Pauses.delete_pause()
							Pauses.delete_all()
							Pauses.draw_unp()
							pause = False
						else:
							Pauses.delete_pause()
							Pauses.delete_all()
							Pauses.draw_p()
							Pauses.resume()
							Pauses.save()
							Pauses.quit()
							pause = True
					if arr1.collidepoint(event.pos):
						Speeds.speed = 0.1
					if arr2.collidepoint(event.pos):
						Speeds.speed = 0.01
					if arr3.collidepoint(event.pos):
						Speeds.speed = 0.00001
					Speeds.arrow1()
					Speeds.arrow2()
					Speeds.arrow3()
					if alg.collidepoint(event.pos):
						Algorithms.delete()
						dfs_pos = Algorithms.Dfs()
						astar_pos = Algorithms.Astar()
						bfs_pos = Algorithms.Bfs()
						go = True
						while go:
							for event_alg in pygame.event.get():
								if event_alg.type == pygame.QUIT:
									pygame.quit()
									sys.exit()
								if event_alg.type == pygame.MOUSEBUTTONDOWN:
									if event_alg.button == 1:
										if dfs_pos.collidepoint(event_alg.pos):
											Algorithms.algorithm = " dfs"
										if astar_pos.collidepoint(event_alg.pos):
											Algorithms.algorithm = "  a*"
										if bfs_pos.collidepoint(event_alg.pos):
											Algorithms.algorithm = " bfs"
										Algorithms.delete()
										Algorithms.draw_text()
										go = False
	Tom.stack = []

def clear_maze_load(maze):
	maze[maze == 1] = 0

def Play_game(account = "GUEST", NameLoad = ""):
	const.screen.fill("black")
	if len(NameLoad) > 0:
		Control.load = NameLoad
		data = readdata(namefile)
		temp = data[account][NameLoad]
		(Tom.x, Tom.y) = temp["main"]
		(House.x, House.y) = temp["begin"]
		(Jerry.x, Jerry.y) = temp["finish"]
		Control.tom = temp["main"]
		Control.house = temp["begin"]
		Control.jerry = temp["finish"]
		Control.time = temp["times"]
		Tom.stack = temp["stack"]
		Control.mode = temp["mode"]
		Control.level = temp["level"]
		arr = temp["data"]
		maze = np.array(arr)
		if Control.level == "  easy":
			Control.cell = 34
			Control.thickness = 6
			Control.size = 20
		elif Control.level == "medium":
			Control.cell = 17
			Control.thickness = 4
			Control.size = 40
		else:
			Control.cell = 7
			Control.thickness = 2
			Control.size = 100
		tranform_data()
		Level.level = Control.level
		Mode.mode = Control.mode
		DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
		Tom.draw()
		House.draw()
		Jerry.draw()
		Control.play = True
		level_pos = Level.draw()
		Level.draw_text()
		mode_pos = Mode.draw()
		Mode.draw_text()
		Spawn.draw()
		rand_pos, mouse_pos = spawn()
		randmaze_pos = RandMaze.draw()
		start_pos = StartGame.draw()
		load_pos = Load.draw()
		quit_pos = Quit.draw()
		TableMenu.draw()
		TableMenu.delete()
	else:
		maze = createMaze(Control.size)
		Control.house, Control.tom, Control.jerry = random_point.random_spawn(Control.size)
		(Tom.x, Tom.y) = Control.tom
		(House.x, House.y) = Control.house
		(Jerry.x, Jerry.y) = Control.jerry
		DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
		Tom.draw()
		House.draw()
		Jerry.draw()
		TableMenu.draw()
		level_pos = Level.draw()
		Level.draw_text()
		mode_pos = Mode.draw()
		Mode.draw_text()
		Spawn.draw()
		rand_pos, mouse_pos = spawn()
		randmaze_pos = RandMaze.draw()
		start_pos = StartGame.draw()
		load_pos = Load.draw()
		quit_pos = Quit.draw()
	running = True
	while running:
		if Control.play:
			Control.play = False
			if Control.mode == "Player":
				mazecopy = maze.copy()
				TableMenu.delete()
				player(mazecopy, account)
				if Control.back_win[0]:
					DrawMaze.delete_all(maze, Control.coor, Control.cell, Control.thickness, color_delete_maze)
					maze = createMaze(Control.size)
					Control.house, Control.tom, Control.jerry = random_point.random_spawn(Control.size)
					(Tom.x, Tom.y) = Control.tom
					(House.x, House.y) = Control.house
					(Jerry.x, Jerry.y) = Control.jerry
					DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
					Tom.draw()
					House.draw()
					Jerry.draw()
					Control.play = True
					Control.back_win[0] = False
				if Control.back_win[1]:
					TableMenu.delete()
					(Tom.x, Tom.y) = (House.x, House.y)
					DrawMaze.delete_all(maze, Control.coor, Control.cell, Control.thickness, color_delete_maze)
					DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
					Tom.draw()
					House.draw()
					Jerry.draw()
					Level.draw()
					Level.draw_text()
					Mode.draw()
					Mode.draw_text()
					Spawn.draw()
					Spawn.random()
					Spawn.mouse()
					RandMaze.draw()
					StartGame.draw()
					Load.draw()
					Quit.draw()
					Control.back_win[1] = False
				if Control.back_win[2]:
					running = False
					Control.back_win[2] = False
			else:
				mazecopy = maze.copy()
				TableMenu.delete()
				bot(account, mazecopy)
				if Control.back_win[0]:
					DrawMaze.delete_all(maze, Control.coor, Control.cell, Control.thickness, color_delete_maze)
					maze = createMaze(Control.size)
					Control.house, Control.tom, Control.jerry = random_point.random_spawn(Control.size)
					(Tom.x, Tom.y) = Control.tom
					(House.x, House.y) = Control.house
					(Jerry.x, Jerry.y) = Control.jerry
					DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
					Tom.draw()
					House.draw()
					Jerry.draw()
					Control.play = True
					Control.back_win[0] = False
				if Control.back_win[1]:
					clear_maze_load(maze)
					TableMenu.delete()
					(Tom.x, Tom.y) = (House.x, House.y)
					DrawMaze.delete_all(maze, Control.coor, Control.cell, Control.thickness, color_delete_maze)
					DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
					Tom.draw()
					House.draw()
					Jerry.draw()
					Level.draw()
					Level.draw_text()
					Mode.draw()
					Mode.draw_text()
					Spawn.draw()
					Spawn.random()
					Spawn.mouse()
					RandMaze.draw()
					StartGame.draw()
					Load.draw()
					Quit.draw()
					Control.back_win[1] = False
				if Control.back_win[2]:
					running = False
					Control.back_win[2] = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.Game().quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if level_pos.collidepoint(event.pos):
						Level.delete()
						easy_pos, medium_pos, hard_pos = level()
						run_level = True
						select = False
						while run_level:
							for event_level in pygame.event.get():
								if event_level.type == pygame.QUIT:
									pygame.quit()
									sys.exit()
								if event_level.type == pygame.MOUSEBUTTONDOWN:
									if event_level.button == 1:
										if easy_pos.collidepoint(event_level.pos):
											if Control.level != "  easy":
												tempthickness = Control.thickness
												tempcell = Control.cell
												select = True
												Level.level = "  easy"
												Control.level = "  easy"
												Control.thickness = 6
												Control.cell = 34
												Control.size = 20
										elif medium_pos.collidepoint(event_level.pos):
											if Control.level != "medium":
												tempthickness = Control.thickness
												tempcell = Control.cell
												select = True
												Level.level = "medium"
												Control.level = "medium"
												Control.thickness = 4
												Control.cell = 17
												Control.size = 40
										elif hard_pos.collidepoint(event_level.pos):
											if Control.level != "  hard":
												tempthickness = Control.thickness
												tempcell = Control.cell
												select = True
												Level.level = "  hard"
												Control.level = "  hard"
												Control.thickness = 2
												Control.cell = 7
												Control.size = 100
										Level.delete()
										Level.draw_text()
										run_level = False
										if select:
											tranform_data()
											DrawMaze.delete_all(maze, Control.coor, tempcell, tempthickness, color_delete_maze)
											maze = createMaze(Control.size)
											DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
											Control.house, Control.tom, Control.jerry = random_point.random_spawn(Control.size)
											(Tom.x, Tom.y) = Control.tom
											(House.x, House.y) = Control.house
											(Jerry.x, Jerry.y) = Control.jerry
											Tom.draw()
											House.draw()
											Jerry.draw()
					if mode_pos.collidepoint(event.pos):
						Mode.delete()
						player_pos, bot_pos = mode()
						run_mode = True
						while run_mode:
							for event_mode in pygame.event.get():
								if event_mode.type == pygame.QUIT:
									pygame.quit()
									sys.exit()
								if event_mode.type == pygame.MOUSEBUTTONDOWN:
									if event_mode.button == 1:
										if player_pos.collidepoint(event_mode.pos):
											Mode.mode = "Player"
											Control.mode = "Player"
										elif bot_pos.collidepoint(event_mode.pos):
											Mode.mode = "  Bot"
											Control.mode = "  Bot"
										Mode.delete()
										Mode.draw_text()
										run_mode = False

					if rand_pos.collidepoint(event.pos):
						Tom.delete()
						House.delete()
						Jerry.delete()
						Control.house, Control.tom, Control.jerry = random_point.random_spawn(Control.size)
						(Tom.x, Tom.y) = Control.tom
						(House.x, House.y) = Control.house
						(Jerry.x, Jerry.y) = Control.jerry
						Tom.draw()
						House.draw()
						Jerry.draw()
					if mouse_pos.collidepoint(event.pos):
						mouse_choice(Control.size, Control.cell, Control.thickness, Control.coor)

					if randmaze_pos.collidepoint(event.pos):
						DrawMaze.delete_all(maze, Control.coor, Control.cell, Control.thickness, color_delete_maze)
						maze = createMaze(Control.size)
						DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
						Control.house, Control.tom, Control.jerry = random_point.random_spawn(Control.size)
						(Tom.x, Tom.y) = Control.tom
						(House.x, House.y) = Control.house
						(Jerry.x, Jerry.y) = Control.jerry
						Tom.draw()
						House.draw()
						Jerry.draw()
					if start_pos.collidepoint(event.pos):
						Control.play = True
					if load_pos.collidepoint(event.pos):
						nameload = Oversave_Or_Load(account, namefile, colorIn).solve()
						if len(nameload) <= 0:
							Oversave_Or_Load(account, namefile, colorIn).delete()
							Spawn.draw()
							Spawn.random()
							Spawn.mouse()
							RandMaze.draw()
							StartGame.draw()
							Load.draw()
						else:
							DrawMaze.delete_all(maze, Control.coor, Control.cell, Control.thickness, color_delete_maze)
							data = readdata(namefile)
							temp = data[account][nameload]
							(Tom.x, Tom.y) = temp["main"]
							(House.x, House.y) = temp["begin"]
							(Jerry.x, Jerry.y) = temp["finish"]
							Control.tom = temp["main"]
							Control.house = temp["begin"]
							Control.jerry = temp["finish"]
							Control.time = temp["times"]
							Tom.stack = temp["stack"]
							Control.mode = temp["mode"]
							Control.level = temp["level"]

							arr = temp["data"]
							maze = np.array(arr)
							if Control.level == "  easy":
								Control.cell = 34
								Control.thickness = 6
								Control.size = 20
							elif Control.level == "medium":
								Control.cell = 17
								Control.thickness = 4
								Control.size = 40
							else:
								Control.cell = 7
								Control.thickness = 2
								Control.size = 100
							tranform_data()
							Level.level = Control.level
							Mode.mode = Control.mode
							DrawMaze.draw(maze, Control.cell, Control.thickness, color_wall, color_road)
							Tom.draw()
							House.draw()
							Jerry.draw()
							Control.play = True
					if quit_pos.collidepoint(event.pos):
						Quit.delete_down()
						Quit.notification()
						yes = YesNo.Yes(800, 650)
						no = YesNo.No(930, 650)
						yesno = True
						while yesno:
							for event_yesno in pygame.event.get():
								if event_yesno.type == pygame.QUIT:
									pygame.quit()
									sys.exit()
								if event_yesno.type == pygame.MOUSEBUTTONDOWN:
									if event_yesno.button == 1:
										if yes.collidepoint(event_yesno.pos):
											yesno = False
											running = False
										if no.collidepoint(event_yesno.pos):
											Quit.delete_down()
											Quit.draw()
											yesno = False


