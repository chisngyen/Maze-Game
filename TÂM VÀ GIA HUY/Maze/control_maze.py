# easy = [20, 34, 6]
# medium = [40, 17, 4]
# hard = [100, 7, 2]
class Control:
	def __init__(self):
		self.tom = (0, 0)
		self.jerry = (0, 0)
		self.house = (0, 0)
		self.level = "  easy"
		self.size = 20
		self.cell = 34
		self.thickness = 6
		self.thickness_bar = 10
		self.coor = 4
		self.mode = "Player"
		self.back_win = [False, False, False]
		self.play = False
		self.load = ""
		self.time = 0
