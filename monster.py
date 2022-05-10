import random
import pygame
from setting import *
import time


class Monster():
    element = ["fire", "forest", "water"]
    monsterimg = pygame.transform.scale(
        pygame.image.load("photo/monster.png"), (scale(158), scale(108)))
    elementimg = {}
    img = pygame.transform.scale(
        pygame.image.load(f"photo/fireelement.png"), (scale(20), scale(20)))
    elementimg["fire"] = img
    img = pygame.transform.scale(
        pygame.image.load(f"photo/waterelement.png"), (scale(20), scale(20)))
    elementimg["water"] = img
    img = pygame.transform.scale(
        pygame.image.load(f"photo/forestelement.png"), (scale(20), scale(20)))
    elementimg["forest"] = img

    def __init__(self, times, serverstarttime, id):
        self.atk = random.randint(1, 10)
        self.hp = random.randint(1, 10)
        self.id = id
        self.speed = random.randint(2, 3)
        self.time = times
        self.nowtime = times-serverstarttime
        self.nowdifficulty = int(self.nowtime//30) + 1
        self.weakskill = [
            [Monster.element[random.randint(0, 2)] for i in range(3)]for i in range(self.nowdifficulty)]
        self.x = width*1.5
        self.y = height//2-20
        self.tempx = self.x
        self.tempy = self.y

    def update(self, deltatime):
        self.tempx = scale(self.x - self.speed *
                           (time.time()-deltatime-self.time) * 60)
        self.tempy = scale(self.y)

    def draw(self, win):
        win.blit(Monster.monsterimg, (self.tempx, self.tempy))
        self.drawweak(win)

    def drawweak(self, win):
        for row in range(len(self.weakskill)):
            for index in range(len(self.weakskill[row])):
                win.blit(Monster.elementimg[self.weakskill[row][index]],
                         (self.tempx + scale(40+25*index), self.tempy-scale(40*row+40), scale(20), scale(20)))
