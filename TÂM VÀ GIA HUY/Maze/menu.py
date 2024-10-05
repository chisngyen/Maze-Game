import pygame
import const, SOUND, Maze, login, json
from button import Button
from game import Game
from cursor import *
from draw_const import Draw
import create_save
pygame.init()

def question():
        size_BUTTON_W = 80
        size_BUTTON_H = 50

        YES_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\green.png"), size = (size_BUTTON_W, size_BUTTON_H)), pos = (const.WIDTH//2 - 70, 520), 
                                text_input = "YES", font=const.get_font(30), base_color = "#FFFFF0", color = "#AFFFE0")
        NO_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (size_BUTTON_W, size_BUTTON_H)), pos = (const.WIDTH//2+ 70, 520), 
                                text_input = "NO", font=const.get_font(30), base_color = "#FFFFF0", color = "#FF6347")
        while True:
    
            for button in [YES_BUTTON, NO_BUTTON]:
                button.changeColor(pygame.mouse.get_pos())
                button.update(const.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if YES_BUTTON.checkWithSound(event.pos):
                        return True
                    if NO_BUTTON.checkWithSound(event.pos): 
                        return False
            pygame.display.update()

def display_message(text, time, size):
    const.screen.blit(const.BG, (0, 0))
    Draw().draw_text_center(const.WIDTH//2, const.HEIGHT//2, const.get_font(size), "#FFEFD5", text)
    pygame.display.update()
    pygame.time.wait(time * 1000)

class MENU:
    def credits():
        while True:
            const.screen.blit(const.BG, (0, 0))

            Draw().draw_box(const.WIDTH//2, const.HEIGHT//2, "img\\menu\\credits.png", (700, 700))

            Draw().draw_text_center(const.WIDTH//2, 110, const.get_font(70), "yellow", "CREDITS")
            Draw().draw_text_center(const.WIDTH//2, 170, const.get_font(35), "#FFFF99", "MAZE GAME PROJECT")
            Draw().draw_text_center(const.WIDTH//2, 220, const.get_font(35), "#FFFF99", "GROUP 11 - 23TNT1 - HCMUS")

            Draw().draw_text_center(const.WIDTH//2, 270, const.get_font(30), "#00FF99", "===================Members===================")
            Draw().draw_text_center(const.WIDTH//2, 310, const.get_font(20), "white", "Nguyen Trong Hoa - 23122029")
            Draw().draw_text_center(const.WIDTH//2, 350, const.get_font(20), "white", "Phan Huynh Chau Thinh - 23122019")
            Draw().draw_text_center(const.WIDTH//2, 390, const.get_font(20), "white", "Tran Chi Nguyen - 23122044")
            Draw().draw_text_center(const.WIDTH//2, 430, const.get_font(20), "white", "Kpuih Thuing - 23122054")
            Draw().draw_text_center(const.WIDTH//2, 470, const.get_font(20), "white", "Nguyen Viet Hung - 23122032")

            Draw().draw_text_center(const.WIDTH//2, 520, const.get_font(30), "#00FF99", "=======================GVHD======================")
            Draw().draw_text_center(const.WIDTH//2, 560, const.get_font(20), "white", "Nguyen Tien Huy")
            Draw().draw_text_center(const.WIDTH//2, 600, const.get_font(20), "white", "Le Thanh Tung")
            Draw().draw_text_center(const.WIDTH//2, 640, const.get_font(20), "white", "Nguyen Tran Duy Minh")

            BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (140, 70)), pos = (60, 200), text_input = "BACK", font = const.get_font(40), base_color = "#FFFFF0", color = "#FF6347")

            BACK_BUTTON.changeColor(pygame.mouse.get_pos())
            BACK_BUTTON.update(const.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkWithSound(pygame.mouse.get_pos()):
                        MENU.main_menu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        MENU.main_menu()

            pygame.display.update()

    def help():
        while True:
            const.screen.blit(const.BG, (0, 0))

            Draw().draw_box(const.WIDTH//2, const.HEIGHT//2, "img\\menu\\credits.png", (700, 700))

            Draw().draw_text_center(const.WIDTH//2, 110, const.get_font(70), "yellow", "HELP")

            Draw().draw_text_center(const.WIDTH//2, 155, const.get_font(14), "white", "Player need to use Mouse to click the buttons/ Arrows to move. ")
            Draw().draw_text_center(const.WIDTH//2, 170, const.get_font(14), "white", "There are two modes: Player and Bot.")
            Draw().draw_text_center(const.WIDTH//2, 185, const.get_font(14), "white", "Player can use H to have a hint.")
            Draw().draw_text_center(const.WIDTH//2, 200, const.get_font(14), "white", "Bot has two algorithms, player can stop an algorithm to get another.")
            Draw().draw_text_center(const.WIDTH//2, 215, const.get_font(14), "white", "There are three levels: Easy(20 cells), Medium(40 cells), Hard(100 cells).")

            Draw().draw_box(280, 270, "img/keyboard/left.png", (30,30))
            Draw().draw_text_center(380, 270, const.get_font(17), "#00FF99", "===MOVE LEFT===")
            Draw().draw_text(x= 320, y = 310, size = 12, color = "white", text = "      O))")
            Draw().draw_text(x = 320, y=325, size = 12, color = "white", text="    O))")
            Draw().draw_text(x = 320, y=340, size = 12, color = "white", text="  O))")
            Draw().draw_text(x = 320, y=355, size = 12, color = "white", text="O)O)))))O)))))")
            Draw().draw_text(x = 320, y=370, size = 12, color = "white", text="  O))")
            Draw().draw_text(x = 320, y=385, size = 12, color = "white", text="   O))")
            Draw().draw_text(x = 320, y=400, size = 12, color = "white", text="     O))")

            Draw().draw_box(280, 440, "img/keyboard/right.png", (30,30))
            Draw().draw_text_center(380, 440, const.get_font(17), "#00FF99", "===MOVE RIGHT===")
            Draw().draw_text(x = 320, y = 480, size = 12, color = "white", text="   O))")
            Draw().draw_text(x=320, y=495, size = 12, color = "white", text="     O))")
            Draw().draw_text(x=320, y=510, size = 12, color = "white", text="        O))")
            Draw().draw_text(x=320, y=525, size = 12, color = "white", text="O))))O))))O))")
            Draw().draw_text(x=320, y=540, size = 12, color = "white", text="       O))")
            Draw().draw_text(x=320, y=555, size = 12, color = "white", text="     O))")
            Draw().draw_text(x=320, y=570, size = 12, color = "white", text="   O))")

            Draw().draw_box(const.WIDTH//2, 425, "img/playgame.png", (120,90))

            Draw().draw_box(650, 270, "img/keyboard/up.png", (30,30))
            Draw().draw_text_center(750, 270, const.get_font(17), "#00FF99", "===MOVE UP===")
            Draw().draw_text(x=690, y=310, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=325, size = 12, color = "white", text="  O)) O))")
            Draw().draw_text(x=690, y=340, size = 12, color = "white", text="O))     O))")
            Draw().draw_text(x=690, y=355, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=370, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=385, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=400, size = 12, color = "white", text="    O))")

            Draw().draw_box(650, 440, "img/keyboard/down.png", (30,30))
            Draw().draw_text_center(750, 440, const.get_font(17), "#00FF99", "===MOVE DOWN===")
            Draw().draw_text(x=690, y=480, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=495, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=510, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=525, size = 12, color = "white", text="    O))")
            Draw().draw_text(x=690, y=540, size = 12, color = "white", text="O))     O))")
            Draw().draw_text(x=690, y=555, size = 12, color = "white", text="  O)) O))")
            Draw().draw_text(x=690, y=570, size = 12, color = "white", text="    O))")
            
            Draw().draw_text_center(const.WIDTH//2, 250, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 265, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 280, const.get_font(15), "white", "!?")

            Draw().draw_text_center(const.WIDTH//2, 310, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 325, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 340, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 355, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 370, const.get_font(15), "white", "!?")

            Draw().draw_text_center(const.WIDTH//2, 490, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 505, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 520, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 535, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 550, const.get_font(15), "white", "!?")

            Draw().draw_text_center(const.WIDTH//2, 580, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 595, const.get_font(15), "white", "!?")
            Draw().draw_text_center(const.WIDTH//2, 610, const.get_font(15), "white", "!?")

            BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (140, 70)), pos = (60, 200), text_input = "BACK", font = const.get_font(40), base_color = "#FFFFF0", color = "#FF6347")

            BACK_BUTTON.changeColor(pygame.mouse.get_pos())
            BACK_BUTTON.update(const.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkWithSound(event.pos):
                        MENU.main_menu()
            pygame.display.update()

    def main_menu():
        size_font = 45
        size_BUTTON_W = 180

        PLAY_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\green.png"), size = (size_BUTTON_W + 90,  size_font + 30)), pos = (const.WIDTH//2, 300), text_input = "PLAY", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#AFFFE0")
        OPTIONS_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\orange.png"), size = (size_BUTTON_W + 90, size_font + 30)), pos = (const.WIDTH//2, 380), text_input = "OPTIONS", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#FAA460")
        CREDITS_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\yellow.png"), size = (size_BUTTON_W + 90, size_font + 30)), pos = (const.WIDTH//2, 460), text_input = "CREDITS", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#FFFF00")
        HELP_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\violet.png"), size = (size_BUTTON_W + 90, size_font + 30)), pos = (const.WIDTH//2, 540), text_input = "HELP", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#EE82EE")
        QUIT_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\blue_white.png"), size = (size_BUTTON_W + 90, size_font + 30)), pos = (const.WIDTH//2, 620), text_input = "QUIT", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#AFEEEE")
        BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (170, size_font + 30)), pos = (130, 200), text_input = "LOGIN", font = const.get_font(25), base_color = "#FFFFF0", color = "#FF6347")


        cursor_left = Cursor_LEFT('img/keyboard/nut.png', PLAY_BUTTON.pos, size = (60, 30))
        cursor_right = Cursor_RIGHT('img/keyboard/nut2.png', PLAY_BUTTON.pos, size =(60, 30))

        cursor_left.set_buttons([PLAY_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, HELP_BUTTON, QUIT_BUTTON], 48, 15)
        cursor_right.set_buttons([PLAY_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, HELP_BUTTON, QUIT_BUTTON], 38, 15)
        
        name = login.get_name()

        while True:
            const.screen.blit(const.BG, (0, 0))
            const.screen.blit(pygame.image.load("img/assets/t.png"), (670, 170))
            const.screen.blit(pygame.transform.scale(pygame.image.load("img/assets/jr.png").convert_alpha(), size = (530, 300)), (-50, 370))

            const.screen.blit(pygame.transform.scale(pygame.image.load("img/menu/login.png"), size = (250, 250)), (5, 10))

            Draw().draw_text_center(130, 130, const.get_font(30), "#008080", name)
            Draw().draw_text_center(const.WIDTH//2 + 20, 120, const.get_font(90), "#FFEFD5", "MAIN MENU" )

            for button in [BACK_BUTTON, PLAY_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, HELP_BUTTON, QUIT_BUTTON]:
                button.changeColor(pygame.mouse.get_pos())
                button.update(const.screen)
            
            cursor_left.update_current_position([PLAY_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, HELP_BUTTON, QUIT_BUTTON], pygame.mouse.get_pos())
            cursor_right.update_current_position([PLAY_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, HELP_BUTTON, QUIT_BUTTON], pygame.mouse.get_pos())

            cursor_left.draw(const.screen)  
            cursor_right.draw(const.screen)  

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                cursor_left.move_up()
                cursor_right.move_up()
                pygame.time.wait(150)  
            if keys[pygame.K_DOWN]:
                cursor_left.move_down()
                cursor_right.move_down()
                pygame.time.wait(150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if BACK_BUTTON.checkWithSound(event.pos):
                                Game().deleteGuest()
                                login.LoginScreen().run()
                            if PLAY_BUTTON.checkWithSound(event.pos):
                                const.screen.fill("black")
                                Maze.Play_game(account = name)
                            if OPTIONS_BUTTON.checkWithSound(event.pos):
                                OPTIONS.menu_options()
                            if CREDITS_BUTTON.checkWithSound(event.pos):
                                MENU.credits()
                            if HELP_BUTTON.checkWithSound(event.pos):
                                MENU.help()
                            if QUIT_BUTTON.checkWithSound(event.pos):
                                display_message("GAME OVER", 3, 100)
                                Game().quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Game().deleteGuest()
                        login.LoginScreen().run()
                    if event.key == pygame.K_RETURN:
                        if cursor_left.current_position == 0 or cursor_right.current_position == 0:
                            const.screen.fill("black")
                            Maze.Play_game()
                        elif cursor_left.current_position == 1 or cursor_right.current_position == 1:
                            MENU.sound_effect()
                        elif cursor_left.current_position == 2 or cursor_right.current_position == 2:
                            MENU.credits()
                        elif cursor_left.current_position == 3 or cursor_right.current_position == 3:
                            MENU.help()
                        elif cursor_left.current_position == 4 or cursor_right.current_position == 4:
                            display_message("GAME OVER", 3, 100)
                            Game().quit()
            pygame.display.update()


class OPTIONS:
    def music():
        SOUND_BUTTON = SOUND.ButtonSound(image = pygame.transform.scale(pygame.image.load("img\\menu\\turn.png").convert_alpha(), size = (180, 80)), pos = (const.WIDTH//2 + 160, 290), text_on = "ON", text_off = "OFF")
            
        EFFECT_BUTTON = SOUND.ButtonSound(image = pygame.transform.scale(pygame.image.load("img\\menu\\turn.png").convert_alpha(), size = (180, 80)), pos = (const.WIDTH//2 + 160, 460), text_on = "ON", text_off = "OFF")

        BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png").convert_alpha(), size = (160, 45 + 25)), pos = (const.WIDTH//2, 630), text_input = "BACK", font = const.get_font(45), base_color = "#FFFFF0", color = "#FF6347")

        cursor_left = Cursor_LEFT("img/keyboard/nut.png", SOUND_BUTTON.pos, size = (60, 30))
        cursor_right = Cursor_RIGHT("img/keyboard/nut2.png", SOUND_BUTTON.pos, size = (60, 30))

        cursor_left.set_buttons([SOUND_BUTTON, EFFECT_BUTTON], width = 55, height = 20)
        cursor_right.set_buttons([SOUND_BUTTON, EFFECT_BUTTON], width = 45, height = 20)

        while True:
            const.screen.blit(const.BG, (0, 0))

            Draw().draw_box(const.WIDTH//2, const.HEIGHT//2, "img\\menu\\options.png", (700, 600))
            Draw().draw_text_center(const.WIDTH//2, 150, const.get_font(65), "white", "SOUND")
            
            Draw().draw_text_center(380, 290, const.get_font(50), "white", "MUSIC")
            Draw().draw_text_center(380, 460, const.get_font(50), "white", "EFFECT")

            BACK_BUTTON.changeColor(pygame.mouse.get_pos())
            BACK_BUTTON.update(const.screen)
            
            EFFECT_BUTTON.display_effect(const.screen)
            SOUND_BUTTON.display_sound(const.screen)

            cursor_left.update_current_position([SOUND_BUTTON, EFFECT_BUTTON], pygame.mouse.get_pos())
            cursor_right.update_current_position([SOUND_BUTTON, EFFECT_BUTTON], pygame.mouse.get_pos())

            cursor_left.draw(const.screen) 
            cursor_right.draw(const.screen)  

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                cursor_left.move_up()
                cursor_right.move_up()
                pygame.time.wait(150)  
            if keys[pygame.K_DOWN]:
                cursor_left.move_down()
                cursor_right.move_down()
                pygame.time.wait(150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if SOUND_BUTTON.checkForInput_sound(event.pos):
                            pass
                        if EFFECT_BUTTON.checkForInput_effect(event.pos):
                            pass
                        if BACK_BUTTON.checkWithSound(event.pos):
                            OPTIONS.menu_options()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        OPTIONS.menu_options()
                    if event.key == pygame.K_RETURN:
                        if cursor_left.current_position == 0:
                            k = SOUND_BUTTON.checkForInput_sound((const.WIDTH//2 + 160, 290))
                        elif cursor_left.current_position == 1:
                            k = EFFECT_BUTTON.checkForInput_effect((const.WIDTH//2 + 160, 460))
            pygame.display.update()

    def leaderBoard():
        try:
            with open('rank.json', "r") as f:
                data = json.load(f)

            levels = {
                'easy': [],
                'medium': [],
                'hard': []
            }
            for player, info in data.items():
                levels_info = zip(info['level'], info['time'])
                for level, time in levels_info:
                    levels.get(level.strip(), []).append((player, time))


            for level, players in levels.items():
                levels[level] = sorted(players, key = lambda x: x[1])
        except:
            pass

        selected_level = None  # Không hiển thị bảng xếp hạng mặc định

        # Tạo các nút chế độ với vị trí điều chỉnh
        EASY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("img\\menu\\green.png"), size=(140, 70)), pos=(350, 250), text_input="EASY", font=const.get_font(40), base_color="#FFFFF0", color="#00FF00")
        MEDIUM_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("img\\menu\\yellow.png"), size=(210, 70)), pos=(540, 250), text_input="MEDIUM", font=const.get_font(40), base_color="#FFFFF0", color="#FFFF00")
        HARD_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size=(140, 70)), pos=(730, 250), text_input="HARD", font=const.get_font(40), base_color="#FFFFF0", color="#FF0000")
        BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size=(140, 70)), pos=(60, 200), text_input="BACK", font=const.get_font(40), base_color="#FFFFF0", color="#FF6347")

        # Vòng lặp chính
        while True:
            # Xử lý sự kiện
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY_BUTTON.checkWithSound(event.pos):
                        selected_level = 'easy'
                    elif MEDIUM_BUTTON.checkWithSound(event.pos):
                        selected_level = 'medium'
                    elif HARD_BUTTON.checkWithSound(event.pos):
                        selected_level = 'hard'
                    elif BACK_BUTTON.checkWithSound(event.pos):
                        OPTIONS.menu_options()

            # Xóa màn hình
            const.screen.fill('white')
            const.screen.blit(const.BG, (0, 0))
            Draw().draw_box(const.WIDTH//2, const.HEIGHT//2, "img\\menu\\credits.png", (700, 700))

            # Vẽ tiêu đề LEADERBOARD
            Draw().draw_text_center(const.WIDTH//2, 140, const.get_font(70), "yellow", "LEADERBOARD")

            # Vẽ các nút
            EASY_BUTTON.changeColor(pygame.mouse.get_pos())
            EASY_BUTTON.update(const.screen)
            MEDIUM_BUTTON.changeColor(pygame.mouse.get_pos())
            MEDIUM_BUTTON.update(const.screen)
            HARD_BUTTON.changeColor(pygame.mouse.get_pos())
            HARD_BUTTON.update(const.screen)
            BACK_BUTTON.changeColor(pygame.mouse.get_pos())
            BACK_BUTTON.update(const.screen)

            if selected_level:
                # Tính toán vị trí để căn giữa màn hình
                total_height = 200  # Thay đổi vị trí bắt đầu để tránh các nút
                if selected_level == "easy":
                    text = f"===================== {selected_level} ======================"
                elif selected_level == "medium":
                    text = f"=================== {selected_level} ==================="
                else:
                    text = f"===================== {selected_level} ======================"
                total_height += 130
                Draw().draw_text_center(const.WIDTH//2, total_height, const.get_font(30), "#FFFF99", text)
                total_height += 50

                # Định dạng font và màu cho các cột "Rank", "Player Name", "Time"
                font_color = "#00FF99"  # Màu cho chữ
                font_size = 25  # Kích thước font
                column_titles = ["Rank", "Player Name", "Time"]
                column_offsets = [300, 540, 780]
                for i, title in enumerate(column_titles):
                    # Vẽ tiêu đề của từng cột với font và màu sắc như đã mô tả
                    Draw().draw_text_center(column_offsets[i], total_height, const.get_font(font_size), font_color, title)

                total_height += font_size + 10
                try:
                    for rank, (player, time) in enumerate(levels[selected_level][:5], 1):
                        # Vẽ nội dung của từng ô với font và màu sắc như đã mô tả
                        Draw().draw_text_center(column_offsets[0], total_height, const.get_font(20), "white", str(rank))
                        total_height += 10
                        Draw().draw_text_center(column_offsets[1], total_height, const.get_font(20), "white", player)
                        total_height += 10
                        Draw().draw_text_center(column_offsets[2], total_height, const.get_font(20), "white", str(time))
                        
                        total_height += 25
                except:
                    pass

                total_height += 20

            pygame.display.flip()
    
    def loadGAME():
        BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (140, 70)), pos = (60, 200), text_input = "BACK", font = const.get_font(40), base_color = "#FFFFF0", color = "#FF6347")

        NAME = Button(image = pygame.transform.scale(pygame.image.load("img/menu/green2.png"), size = (200, 80)), pos = (340, 200), text_input = "NAME", font = const.get_font(35), base_color = "WHITE", color="white")
        MODE = Button(image = pygame.transform.scale(pygame.image.load("img/menu/green2.png"), size = (180, 80)), pos = (570, 200), text_input = "MODE", font = const.get_font(35), base_color = "WHITE", color="white")
        LEVEL = Button(image = pygame.transform.scale(pygame.image.load("img/menu/green2.png"), size = (180, 80)), pos = (760, 200), text_input = "LEVEL", font = const.get_font(35), base_color = "WHITE", color="white")
        ten = login.get_name()
        try:
            file_load = []
            mode_load = []
            level_load = []
            with open("data.json", "r") as f:
                data = json.load(f)
                for i, j in data[ten].items():
                    file_load.append(i)
                    mode_load.append(j["mode"])
                    level_load.append(j["level"])
        except:
            pass

        while True:
            const.screen.fill('white')
            const.screen.blit(const.BG, (0, 0))
            Draw().draw_box(const.WIDTH//2, const.HEIGHT//2, "img\\menu\\credits.png", (700, 700))
            Draw().draw_text_center(const.WIDTH//2, 110, const.get_font(70), "yellow", "LOAD")
            
            BACK_BUTTON.update(const.screen)
            BACK_BUTTON.changeColor(pygame.mouse.get_pos())
            NAME.update(const.screen)
            MODE.update(const.screen)
            LEVEL.update(const.screen)
            k = 300
            for mode, level in zip(mode_load, level_load):
                Draw().draw_box(570, k, "img/menu/blue.png", size = (140, 60))
                Draw().draw_text_center(570, k, const.get_font(25), "white", text = mode)
                Draw().draw_box(760, k, "img/menu/blue.png", size = (140, 60))
                Draw().draw_text_center(760, k, const.get_font(25), "white", text = level)
                k += 75

            p = 300
            buttons = []
            for file in file_load:
                buttons.append(Button(pygame.transform.scale(pygame.image.load("img/menu/blue.png"), size = (200, 60)), (340, p), text_input = file, font = const.get_font(27), base_color = "white", color = "white"))
                p += 75

            for button in buttons:
                button.update(const.screen)
                button.changeColor(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkWithSound(event.pos):
                        OPTIONS.menu_options()
                    for button in buttons:
                        if button.checkWithSound(event.pos):
                            Maze.Play_game(account = ten, NameLoad = button.text_input)
            pygame.display.update()

    def menu_options():
        size_font = 50
        size_BUTTON_W = 280
        
        LEADERRBOARD_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\blue_deep.png"), size = (size_BUTTON_W, size_font + 50)), pos = (const.WIDTH//2, 350), 
                                text_input="RANKING", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#B0C4DE")
        SOUND_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\blue.png"), size = (size_BUTTON_W, size_font + 50)), pos = (const.WIDTH//2, 470), 
                                text_input="SOUND", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#AFEEEE")
        LOAD_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\yellow.png"), size = (size_BUTTON_W, size_font + 50)), pos = (const.WIDTH//2, 590), 
                                text_input="LOAD", font = const.get_font(size_font), base_color = "#FFFFF0", color = "#FFFF00")
        BACK_BUTTON = Button(image = pygame.transform.scale(pygame.image.load("img\\menu\\red.png"), size = (140, 70)), pos = (60, 200), 
                                text_input="BACK", font = const.get_font(size_font - 10), base_color = "#FFFFF0", color = "#FF6347")
        
        cursor_left = Cursor_LEFT('img/keyboard/nut.png' , LEADERRBOARD_BUTTON.pos, size = (70, 40))
        cursor_right = Cursor_RIGHT('img/keyboard/nut2.png' , LEADERRBOARD_BUTTON.pos, size = (70, 40))

        cursor_left.set_buttons([LEADERRBOARD_BUTTON, SOUND_BUTTON, LOAD_BUTTON], width = 60, height = 25)
        cursor_right.set_buttons([LEADERRBOARD_BUTTON, SOUND_BUTTON, LOAD_BUTTON], width = 45, height = 25)

        while True:
            const.screen.blit(const.BG, (0, 0))
           
            Draw().draw_text_center(const.WIDTH//2, 165, const.get_font(100), "#FFEFD5", "OPTIONS")

            for button in [BACK_BUTTON, SOUND_BUTTON, LOAD_BUTTON, LEADERRBOARD_BUTTON]:
                button.changeColor(pygame.mouse.get_pos())
                button.update(const.screen)

            cursor_left.update_current_position([LEADERRBOARD_BUTTON, SOUND_BUTTON, LOAD_BUTTON], pygame.mouse.get_pos())
            cursor_right.update_current_position([LEADERRBOARD_BUTTON, SOUND_BUTTON, LOAD_BUTTON], pygame.mouse.get_pos())

            cursor_left.draw(const.screen)  
            cursor_right.draw(const.screen)  

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                cursor_left.move_up()
                cursor_right.move_up()
                pygame.time.wait(150)  
            if keys[pygame.K_DOWN]:
                cursor_left.move_down()
                cursor_right.move_down()
                pygame.time.wait(150)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if BACK_BUTTON.checkWithSound(event.pos):
                            MENU.main_menu()
                        if SOUND_BUTTON.checkWithSound(event.pos):
                            OPTIONS.music()
                        if LOAD_BUTTON.checkWithSound(event.pos):
                            OPTIONS.loadGAME()
                        if LEADERRBOARD_BUTTON.checkWithSound(event.pos):
                            OPTIONS.leaderBoard()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        MENU.main_menu()
                    if event.key == pygame.K_RETURN:
                        if cursor_left.current_position == 0 or cursor_right.current_position == 0:
                            OPTIONS.music()
                        elif cursor_left.current_position == 1 or cursor_right.current_position == 1:
                            OPTIONS.loadGAME()
                        elif cursor_left.current_position == 2 or cursor_right.current_position == 2:
                            OPTIONS.leaderBoard()
            pygame.display.update()