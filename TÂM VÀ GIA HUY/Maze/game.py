import pygame, sys, json
import const
pygame.mixer.init()

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = const.screen
        self.clock = pygame.time.Clock()

    def quit(self):
        self.deleteGuest()
        pygame.quit()
        sys.exit()
    
    def deleteGuest(self):
        try:
            file = open("data.json")
            f = open("rank.json")
            data = json.load(file)
            rank = json.load(f)
            f.close()
            file.close()
            for i, j in data.items():
                if i == "GUEST":
                    data.pop(i)
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent = 4)
            for i, j in rank.items():
                if i == "GUEST":
                    rank.pop(i)
                    with open("rank.json", "w") as f:
                        json.dump(rank, f, indent = 4)
        except:
            pass




    


