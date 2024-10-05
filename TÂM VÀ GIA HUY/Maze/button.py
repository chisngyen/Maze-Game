import SOUND

effect = SOUND.Effect()

class Button:
	def __init__(self, image , pos, text_input, font, base_color, color):
		self.image = image 
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.pos = pos
		self.font = font
		self.base_color, self.color = base_color, color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkWithSound(self, position):
		if self.rect.collidepoint(position):
			effect.run()
			return True
		return False

	def check(self, position):
		if self.rect.collidepoint(position):
			return True
		return False

	def changeColor(self, position):
		if self.rect.collidepoint(position):
			self.text = self.font.render(self.text_input, True, self.color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)



