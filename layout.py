import pygame
from setting import *


class Layout():
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

        self.textScore = self.font.render(
            f"{self.monster.id-1}", True, "white")
        self.win.blit(self.textScore,
                      self.textScore.get_rect(topleft=(scale(1400), scale(50))))
        pygame.display.update()
