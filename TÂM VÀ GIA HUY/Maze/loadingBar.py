import pygame
import const, menu, draw_const, game

pygame.init()
pygame.mixer.pre_init()
clock = pygame.time.Clock()

class Image(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('img/tom/TomJerry1.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry2.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry3.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry4.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry5.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry6.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry7.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry8.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry9.png'))
		self.sprites.append(pygame.image.load('img/tom/TomJerry10.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self, speed):
		if self.attack_animation:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

class Tom_Run():
    def __init__(self, screen):
        self.screen = screen
        self.x = 200
        Tom = pygame.image.load("img\\assets\\tom.png")
        Tom = pygame.transform.scale(Tom, size = (50, 60))
        Jerry = pygame.image.load("img\\assets\\jerry.png")
        self.Jerry = pygame.transform.scale(Jerry, size = (40, 50))
        self.Tom = Tom

    def draw(self):
        self.screen.blit(self.Tom, (self.x, 560))
        self.screen.blit(self.Jerry, (820, 560))

    def update(self):
        self.x = self.x + 2
        if self.x + 50 + 60 > const.WIDTH:
            self.x = const.WIDTH - 200 - 50
    
    def check_run(self):
        if self.x == const.WIDTH - 200 - 50:
            return True
        else:
            return False

class Loading():
	def __init__(self, screen, BG):
		self.screen = screen
		self.BG = BG
		self.LOADING_BG = pygame.image.load("img/assets/LoadingBarBG.png")
		self.LOADING_BG_RECT = self.LOADING_BG.get_rect(center = (540, 600))

	def loading_screen(self):
		moving_sprites = pygame.sprite.Group()
		image = Image(320, 140)
		moving_sprites.add(image)

		animation_speed = 0.04 

		tom_run = Tom_Run(self.screen)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game.Game().quit()
			
			self.screen.blit(self.BG, (0, 0))

			draw_const.Draw().draw_text_center(const.WIDTH//2, 120, const.get_font(100), "#FFEFD5", "MAZE GAME")

			if not tom_run.check_run():
				image.attack()

				self.screen.blit(self.LOADING_BG, self.LOADING_BG_RECT)

				tom_run.draw()
				tom_run.update()
			else:
				pygame.time.wait(1000)
				menu.MENU.main_menu()
						
			moving_sprites.draw(self.screen)
			moving_sprites.update(animation_speed)

			draw_const.Draw().draw_text_center(const.WIDTH//2, 555, const.get_font(30), "yellow", "LOADING ...")

			pygame.display.update()
			clock.tick(200)

