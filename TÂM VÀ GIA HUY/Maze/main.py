import pygame
import login
from game import Game

class StartGame(Game): 
    def __init__(self):
        super().__init__()

        pygame.display.set_caption("MAZE")
        pygame.display.set_icon(pygame.image.load("img\\assets\\icon.png").convert())
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            login.LoginScreen().run()
            pygame.display.update()

if __name__ == "__main__":
    game = StartGame()
    game.start()