import pygame
import menu, const
from button import Button
from loadingBar import Loading
from game import Game
from draw_const import Draw
from cursor import *

pygame.init()

class InputHandler:
    def __init__(self, text, active, font, color_active, color_passive, hidden, INPUT_RECT):
        self.text = text
        self.font = font
        self.color_active = color_active
        self.color_passive = color_passive
        self.active = active
        self.color = color_passive
        self.hidden = hidden
        self.rect = INPUT_RECT

    def handler_text(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 11 and self.rect.w <= 200:
                        self.text += event.unicode

    def handler_box(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.color_active
            else:
                self.active = False
                self.color = self.color_passive
                
        elif self.active and event.type in (pygame.KEYDOWN, pygame.KEYUP):
            self.handler_text(event)
            
        if not self.active:
            self.color = self.color_passive
    
    def input_surface(self, is_hidden):
        if self.hidden is not None:
            if is_hidden:
                text = self.font.render("*"*len(self.text), True, self.color)
            else:
                text = self.font.render(self.text, True, self.color)
        else:
            text = self.font.render(self.text, True, self.color)
        self.rect.w = max(200, text.get_width() + 10)
        pygame.draw.rect(const.screen, self.color, self.rect, 2)
        const.screen.blit(text, (self.rect.x + 5, self.rect.y + 5))

class NAME:
    def __init__(self) :
        self.name = None
Name = NAME()

class LoginScreen:
    def __init__(self):
        self.load()

    def load(self):
        self.LOG_IN_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\blue_dark.png"), size = (270, 100)), pos = (const.WIDTH//2, 380), 
                            text_input = "LOG IN", font = const.get_font(50), base_color = "#FFF5EE", color = "#B0C4DE")
        self.SIGN_UP_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\orange.png"), size = (270, 100)), pos = (const.WIDTH//2, 500), 
                            text_input = "SIGN UP", font=const.get_font(50), base_color = "#FFF5EE", color = "#FAA460")
        self.GUEST_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\green1.png"), size = (270, 100)), pos = (const.WIDTH//2, 620), 
                            text_input = "GUEST", font=const.get_font(50), base_color = "#FFF5EE", color = "#D0E9A8") 
        
        self.cursor_left = Cursor_LEFT('img/keyboard/nut.png' , self.LOG_IN_BUTTON.pos, size = (70, 40))
        self.cursor_right = Cursor_RIGHT('img/keyboard/nut2.png' , self.LOG_IN_BUTTON.pos, size = (70, 40))

        self.cursor_left.set_buttons([self.LOG_IN_BUTTON, self.SIGN_UP_BUTTON, self.GUEST_BUTTON], width = 60, height = 25)
        self.cursor_right.set_buttons([self.LOG_IN_BUTTON, self.SIGN_UP_BUTTON, self.GUEST_BUTTON], width = 45, height = 25)
        
    def run(self):
        while True:
            self.events()
            self.display()
            pygame.display.update()

    def events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.cursor_left.move_up()
            self.cursor_right.move_up()
            pygame.time.wait(150)  
        if keys[pygame.K_DOWN]:
            self.cursor_left.move_down()
            self.cursor_right.move_down()
            pygame.time.wait(150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game().quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.LOG_IN_BUTTON.checkWithSound(event.pos):
                        Log_in().run()
                    if self.SIGN_UP_BUTTON.checkWithSound(event.pos):
                        Sign_Up().run()
                    if self.GUEST_BUTTON.checkWithSound(event.pos):
                        Name.name = "GUEST"
                        Loading(const.screen, const.BG).loading_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.cursor_left.current_position == 0 or self.cursor_right.current_position == 0:
                        Log_in().run()
                    elif self.cursor_left.current_position == 1 or self.cursor_right.current_position == 1:
                        Sign_Up().run()
                    elif self.cursor_left.current_position == 2 or self.cursor_right.current_position == 2:
                        Name.name = "GUEST"
                        Loading(const.screen, const.BG).loading_screen()

    def display(self):
        const.screen.blit(const.BG1, (0, 0))

        Draw().draw_text_center(const.WIDTH//2 + 240, 200, const.get_font(60), "#FFEFD5", "TOM AND JERRY")
        Draw().draw_text_center(const.WIDTH//2 + 110, 120, const.get_font(110), "#FFEFD5", "MAZE GAME")

        for button in [self.LOG_IN_BUTTON, self.SIGN_UP_BUTTON, self.GUEST_BUTTON]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(const.screen)
        
        self.cursor_left.update_current_position([self.LOG_IN_BUTTON, self.SIGN_UP_BUTTON, self.GUEST_BUTTON], pygame.mouse.get_pos())
        self.cursor_right.update_current_position([self.LOG_IN_BUTTON, self.SIGN_UP_BUTTON, self.GUEST_BUTTON], pygame.mouse.get_pos())

        self.cursor_left.draw(const.screen) 
        self.cursor_right.draw(const.screen)  

class Sign_Up:
    def __init__(self):
        self.is_hidden = True
        self.load()
        self.parameters()
        self.check = 0
        self.user = {}
        
    def load(self):
        self.BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (180, 70)), pos = (const.WIDTH//2 - 100, 490), 
                                text_input = "BACK", font = const.get_font(40), base_color = "#FFFFF0", color = "#FF6347")
        self.SUBMIT_BUTTON = Button(image =pygame.transform.scale(pygame.image.load("img\\menu\\green.png"), size = (200, 70)), pos=(const.WIDTH//2 + 100, 490), 
                                text_input = "SUBMIT", font = const.get_font(40), base_color = "#FFFFF0", color = "#AFFFE0")
        self.HIDDEN_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\blue.png"), size = (100, 40)), pos = (const.WIDTH//2 + 255, 365), 
                                text_input = "SHOW", font = const.get_font(23), base_color = "#FFFFF0", color = "#AFEEEE")
    
    def parameters(self):
        user_text = ""
        pass_text = ""
        confirm_text = ""
        USERNAME_RECT = pygame.Rect(const.WIDTH//2 - 10, 290, 200 ,40)
        PASSWORD_RECT = pygame.Rect(const.WIDTH//2 - 10, 340, 200 ,40)
        CONFIRM_RECT = pygame.Rect(const.WIDTH//2 - 10, 390, 200 ,40)
        active = [False, False, False]
        self.is_hidden = True
        font = pygame.font.Font("font\\Pixel Sans Serif.ttf", 16)

        self.username = InputHandler(user_text, active[0], font, const.color_active, const.color_passive, None, USERNAME_RECT)
        self.password = InputHandler(pass_text, active[0], font, const.color_active, const.color_passive, not None, PASSWORD_RECT)
        self.confirm = InputHandler(confirm_text, active[0], font, const.color_active, const.color_passive, not None, CONFIRM_RECT)

    def run(self):
        while True:
            self.events()
            self.display()
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game().quit()
 
            for handler in [self.username, self.password, self.confirm]:
                handler.handler_box(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.BACK_BUTTON.checkWithSound(event.pos):
                        LoginScreen().run()
                    if self.SUBMIT_BUTTON.checkWithSound(event.pos):
                        self.submit_signup(self.username.text, self.password.text, self.confirm.text, "Users.txt")
                        if self.check == 1:
                            Name.name = str(self.username.text)
                            Loading(const.screen, const.BG).loading_screen()
                    if self.HIDDEN_BUTTON.checkWithSound(event.pos):
                        self.is_hidden = not self.is_hidden
                        if self.is_hidden:
                            self.HIDDEN_BUTTON.text_input = "SHOW" 
                        else:
                            self.HIDDEN_BUTTON.text_input = " HIDE"
    
    def display(self):
        const.screen.blit(const.BG, (0, 0))

        Draw().draw_box(const.WIDTH//2 + 25, const.HEIGHT//2 - 10, "img\\menu\\fram.png", (700, 600))
        Draw().draw_text_center(const.WIDTH//2, 200, const.get_font(100), "#FFEFD5", "SIGN UP")

        k = 0
        for name in ["USERNAME", "PASSWORD", "CONFIRM"]:
            handler = const.get_font(25).render(name, True, '#FFEFD5')
            const.screen.blit(handler, (const.WIDTH//2 - 180, 300 + k))
            k += 50

        for button in [self.BACK_BUTTON, self.SUBMIT_BUTTON, self.HIDDEN_BUTTON]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(const.screen)

        for handler in [self.username, self.password, self.confirm]:
            handler.input_surface(self.is_hidden)
    
    def get_User(self):
        try:
            fileUser = "Users.txt"
            with open(fileUser, "r+") as f:
                    users = f.readlines()
                    for user in users:
                        fields = user.split(",")
                        self.user[fields[0]] = fields[1]
        except:
            Exception
    
    def submit_signup(self, username, password, confirm, fileUser):
        self.get_User()
        try:
            password = password + "\n"
            confirm = confirm + "\n"
            with open(fileUser, "a") as f:
                if len(username) == 0 or len(password) == 0:
                    Draw().draw_text_center(const.WIDTH//2 + 20, const.HEIGHT//2 + 210, const.get_font(40), "red", "SIGNUP INFO MISSING")
                    self.check = 0
                elif username in self.user:
                    Draw().draw_text_center(const.WIDTH//2 + 20, const.HEIGHT//2 + 210, const.get_font(40), "red", "USERNAME ALREADY TAKEN")
                    self.check = 0
                else:
                    if len(confirm) <= 1 or len(password) <= 1:
                        Draw().draw_text_center(const.WIDTH//2 + 20, const.HEIGHT//2 + 210, const.get_font(40), "yellow", "CONFIRM PASSWORD")
                    elif confirm == password:
                        self.user[username] = password
                        f.write(username + "," + password)
                        Draw().draw_text_center(const.WIDTH//2 + 10, const.HEIGHT//2 + 210, const.get_font(40), "green", "SIGNUP SUCCESSFUL")
                        self.check = 1   
                    else:
                        Draw().draw_text_center(const.WIDTH//2 + 20, const.HEIGHT//2 + 210, const.get_font(40), "yellow", "CONFIRM PASSWORD")
        except Exception:
            pass
        pygame.display.update()
        pygame.time.wait(2000)
        
class Log_in:
    def __init__(self):
        self.is_hidden = True
        self.load()
        self.parameters()
        self.check = 0
        self.user = Sign_Up().user
    
    def load(self):
        self.BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (180, 70)), pos = (const.WIDTH//2 - 100, 420), 
                                text_input = "BACK", font = const.get_font(40), base_color = "#FFFFF0", color = "#FF6347")
        self.SUBMIT_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\green.png"), size = (200, 70)), pos = (const.WIDTH//2 + 100, 420), 
                                text_input = "SUBMIT", font = const.get_font(38), base_color = "#FFFFF0", color = "#AFFFE0")
        self.CREATE_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\yellow.png"), size = (400, 70)), pos = (const.WIDTH//2 + 5, 505), 
                                text_input = "CREATE ACCOUNT", font = const.get_font(37), base_color = "#FFFFF0", color = "#FFFF00")
        self.HIDDEN_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\blue.png"), size = (100, 40)), pos = (const.WIDTH//2 + 255, 345), 
                                text_input = "SHOW", font = const.get_font(23), base_color = "#FFFFF0", color = "#AFEEEE")
    
    def parameters(self):
        user_text = ""
        pass_text = ""
        USERNAME_RECT = pygame.Rect(const.WIDTH//2 - 10, 270, 200 ,40)
        PASSWORD_RECT = pygame.Rect(const.WIDTH//2 - 10, 320, 200 ,40)
        active = [False, False]
        self.is_hidden = True
        font = pygame.font.Font("font\\Pixel Sans Serif.ttf", 16)

        self.username = InputHandler(user_text, active[0], font, const.color_active, const.color_passive, None, USERNAME_RECT)
        self.password = InputHandler(pass_text, active[1], font, const.color_active, const.color_passive, self.is_hidden, PASSWORD_RECT)
    
    def run(self):
        while True:
            self.events()
            self.display()
            pygame.display.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game().quit()

            for handler in [self.username, self.password]:
                handler.handler_box(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.BACK_BUTTON.checkWithSound(event.pos):
                        LoginScreen().run()
                    if self.SUBMIT_BUTTON.checkWithSound(event.pos):
                        self.submit_login(self.username.text, self.password.text)
                        if self.check == 1:
                            Name.name = str(self.username.text)
                            Loading(const.screen, const.BG).loading_screen()
                    if self.HIDDEN_BUTTON.checkWithSound(event.pos):
                        self.is_hidden = not self.is_hidden
                        if self.is_hidden:
                            self.HIDDEN_BUTTON.text_input = "SHOW" 
                        else:
                            self.HIDDEN_BUTTON.text_input = " HIDE"
                    if self.CREATE_BUTTON.checkWithSound(event.pos):
                        Sign_Up().run()
    
    def display(self):

        const.screen.blit(const.BG, (0, 0))

        Draw().draw_box(const.WIDTH//2 + 25, const.HEIGHT//2 - 10, "img\\menu\\fram.png", (700, 600))
        Draw().draw_text_center(const.WIDTH//2 + 15, 200, const.get_font(100), "#FFEFD5", "LOGIN")

        k = 0
        for handler in ["USERNAME", "PASSWORD"]:
            handler = const.get_font(25).render(handler, True, '#FFEFD5')
            const.screen.blit(handler, (const.WIDTH//2 - 180, 280 + k))
            k += 50

        for button in [self.BACK_BUTTON, self.SUBMIT_BUTTON, self.HIDDEN_BUTTON, self.CREATE_BUTTON]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(const.screen)


        for handler in [self.username, self.password]:
            handler.input_surface(self.is_hidden)
        pygame.display.update()
    
    def get_User(self):
        try:
            fileUser = "Users.txt"
            with open(fileUser, "r+") as f:
                    users = f.readlines()
                    for user in users:
                        fields = user.split(",")
                        self.user[fields[0]] = fields[1]
        except:
            Exception

    def submit_login(self, username, password):
        password = password + "\n"
        self.get_User()
        if len(username) == 0 or len(password) == 0:
            Draw().draw_text_center(const.WIDTH//2 + 20, const.HEIGHT//2 + 215, const.get_font(40), "red", "LOGIN INFO MISSING")
            self.check = 0
        elif username not in self.user:
            Draw().draw_text_center(const.WIDTH//2 + 10, const.HEIGHT//2 + 215, const.get_font(40), "red", "USERNAME NOT TAKEN")
            self.check = 0
        else:
            if self.user[username] == password:
                Draw().draw_text_center(const.WIDTH//2 + 10, const.HEIGHT//2 + 215, const.get_font(40), "green", "LOGIN SUCCESSFUL")
                self.check = 1
            else:
                Draw().draw_text_center(const.WIDTH//2 + 20, const.HEIGHT//2 + 215, const.get_font(40), "yellow", "PASSWORD INCORRECT")
                self.check = 0
        pygame.display.update()
        pygame.time.wait(2000)

def get_name():
    return Name.name
