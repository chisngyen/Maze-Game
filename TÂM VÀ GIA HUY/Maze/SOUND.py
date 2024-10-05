import pygame, const
pygame.mixer.init()

effect = pygame.mixer.Sound("sound\\click.mp3")

# music = pygame.mixer.Sound("sound\\Kevin MacLeod - Pixelland.mp3")
# music.set_volume(0.7)
pygame.mixer.music.load("sound\\Kevin MacLeod - Pixelland.mp3")
pygame.mixer.music.set_volume(0.7)

class SoundState:
    def __init__(self):
        self.is_play = True
        pygame.mixer.music.play(-1)
sound_state = SoundState()

class EffectState:
    def __init__(self):
        self.effect_active = True
effect_state = EffectState()

class ButtonSound:
    def __init__(self, image, pos, text_on, text_off):
        self.text_on = text_on
        self.text_off = text_off
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.rect = image.get_rect(center = (self.x, self.y))

    def display_effect(self, screen):
        text = self.text_on if effect_state.effect_active else self.text_off
        text = const.get_font(50).render(text, True, "white")
        text_rect = text.get_rect(center = (self.x, self.y))
        screen.blit(self.image, self.rect)
        screen.blit(text, text_rect)

    def display_sound(self, screen):
        text = self.text_on if sound_state.is_play else self.text_off
        text = const.get_font(50).render(text, True, "white")
        text_rect = text.get_rect(center = (self.x, self.y))
        screen.blit(self.image, self.rect)
        screen.blit(text, text_rect)

    def check(self, position):
        if self.rect.collidepoint(position):
            return True
        return False

    def checkForInput_effect(self, position):
        if self.check(position):
            effect_state.effect_active = not effect_state.effect_active
            if effect_state.effect_active:
                effect.play()
            else:
                effect.stop()
            return True
        return False
    
    def checkForInput_sound(self, position):
        if self.check(position):
            sound_state.is_play = not sound_state.is_play
            Effect().run()
            if sound_state.is_play:
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()
            return True
        return False
    
class Effect:
    def __init__(self):
        pass

    def run(self):
        if effect_state.effect_active:
            effect.play()
        else:
            effect.stop()