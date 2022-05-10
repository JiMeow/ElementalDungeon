import pygame
from setting import *


def loadimg():
    img = {}
    imgtemp = pygame.transform.scale(
        pygame.image.load(f"photo/fireelement.png"), (scale(30), scale(30)))
    img["fire"] = imgtemp
    imgtemp = pygame.transform.scale(
        pygame.image.load(f"photo/waterelement.png"), (scale(30), scale(30)))
    img["water"] = imgtemp
    imgtemp = pygame.transform.scale(
        pygame.image.load(f"photo/forestelement.png"), (scale(30), scale(30)))
    img["forest"] = imgtemp
    imgtemp = pygame.transform.scale(
        pygame.image.load(f"photo/bookskill.png"), (scale(250), scale(180)))
    img["book"] = imgtemp

    return img


class Layout():

    img = loadimg()

    def __init__(self, win, clock):
        self.win = win
        self.font = pygame.font.Font(None, 20)
        self.clock = clock

    def updatemap(self, map):
        self.map = map

    def updateplayer(self, player):
        self.player = player

    def updateallplayer(self, allplayer):
        self.allplayer = allplayer

    def updatestatus(self, status):
        self.status = status

    def updatemonster(self, monster):
        self.monster = monster

    def draw(self):
        self.map.draw()
        self.player.draw(self.win)
        for player in self.allplayer:
            if self.status[player.id-1] == 1 and player.id != self.player.id:
                player.draw(self.win)

        self.textFPS = self.font.render(
            f"{self.clock.get_fps():.2f}", True, "white")
        self.win.blit(self.textFPS, self.textFPS.get_rect(
            topleft=(scale(10), scale(50))))

        self.textScore = pygame.font.Font(None, 40).render(
            f"Stage: {self.monster.id-1}", True, "white")
        self.win.blit(self.textScore,
                      self.textScore.get_rect(topleft=(scale(1390), scale(50))))

        if self.monster.id <= 5:
            self.win.blit(
                Layout.img["book"], (width//2-scale(125), height-scale(240), scale(250), scale(180)))

            self.win.blit(
                Layout.img["fire"], (width//2-scale(80), height-scale(200), scale(30), scale(30)))
            self.textfire = pygame.font.Font(None, 30).render(
                f": q", True, "Black")
            self.win.blit(self.textfire,
                          self.textfire.get_rect(topleft=(width//2-scale(45), height-scale(195))))

            self.win.blit(
                Layout.img["forest"], (width//2-scale(80), height-scale(150), scale(30), scale(30)))
            self.textforest = pygame.font.Font(None, 30).render(
                f": w", True, "Black")
            self.win.blit(self.textforest,
                          self.textforest.get_rect(topleft=(width//2-scale(45), height-scale(145))))

            self.win.blit(
                Layout.img["water"], (width//2+scale(15), height-scale(200), scale(30), scale(30)))
            self.textwater = pygame.font.Font(None, 30).render(
                f": e", True, "Black")
            self.win.blit(self.textwater,
                          self.textwater.get_rect(topleft=(width//2+scale(50), height-scale(195))))
        pygame.display.update()
