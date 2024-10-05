
import pygame

class Cursor_LEFT(pygame.Rect):
    def __init__(self, image, position, size):
        self.image = pygame.transform.scale(pygame.image.load(image), size = size )
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.speed = 10 
        self.buttons = None

    def set_buttons(self, buttons, width, height):
        self.button_positions = [(button.rect.topleft[0] - width, button.rect.topleft[1] + height) for button in buttons]
        self.current_position = 0
        self.update()
    
    def update_current_position(self, buttons, pos):
        for index, button in enumerate(buttons):
            if button.check(pos):
                self.current_position = index 
                break
        self.update()

    def update(self):
         self.rect.topleft = self.button_positions[self.current_position] 

    def move_up(self):
        if self.current_position > 0:
            self.current_position -= 1
            self.update()

    def move_down(self):
        if self.current_position < len(self.button_positions) - 1:
            self.current_position += 1
            self.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Cursor_RIGHT(pygame.Rect):
    def __init__(self, image, position, size):
        self.image = pygame.transform.scale(pygame.image.load(image), size = size)
        self.rect = self.image.get_rect()
        self.rect.topright = position
        self.speed = 10 
        self.buttons = None

    def set_buttons(self, buttons, width, height):
        self.button_positions = [(button.rect.topright[0] + width, button.rect.topright[1] + height) for button in buttons]
        self.current_position = 0
        self.update()
    
    def update_current_position(self, buttons, pos):
        for index, button in enumerate(buttons):
            if button.check(pos):
                self.current_position = index 
                break
        self.update()

    def update(self):
         self.rect.topright = self.button_positions[self.current_position] 

    def move_up(self):
        if self.current_position > 0:
            self.current_position -= 1
            self.update()

    def move_down(self):
        if self.current_position < len(self.button_positions) - 1:
            self.current_position += 1
            self.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

