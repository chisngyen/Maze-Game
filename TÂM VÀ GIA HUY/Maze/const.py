import pygame
pygame.init()
#creen size, FPS and background
WIDTH = 1080
HEIGHT = 720
FPS = 30

#Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#BACKGROUND
BG = pygame.transform.scale(pygame.image.load("img\\background\\bg.png"), size = (WIDTH, HEIGHT))
BG1 = pygame.transform.scale(pygame.image.load("img\\background\\nen1.png"), size = (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load("img\\background\\nen2.png"), size = (WIDTH, HEIGHT))

#Get font
def get_font(size): 
    font = pygame.font.Font("font\\SuperMario256.ttf", size)
    return font
def get_font_(size): 
    font = pygame.font.SysFont("Consolas", size, bold = True)
    return font

#Màu input
color_active = pygame.Color('#00FA9A')
color_passive = pygame.Color('#F5F5DC')

