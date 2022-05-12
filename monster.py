import random
import pygame
from setting import *
import time


class Monster():

    skillist = []
    for i in range(1, 11):
        imgleft = pygame.transform.scale(
            pygame.image.load(f"photo/skill_{i}.jpg"), (scale(40), scale(40)))
        skillist.append(imgleft)

    monsterimg = []
    monsterimg.append(pygame.transform.scale(
        pygame.image.load("photo/monster1.png"), (scale(158), scale(108))))
    monsterimg.append(pygame.transform.scale(
        pygame.image.load("photo/monster2.png"), (scale(158), scale(130))))

    element = ["fire", "forest", "water"]
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
        self.imgindex = random.randint(0, 1)
        self.speed = random.randint(2, 3)
        self.time = times
        self.nowtime = times-serverstarttime
        self.nowdifficulty = int(self.nowtime//30) + 1
        self.weakskill = [
            [Monster.element[random.randint(0, 2)] for i in range(3)]for i in range(self.nowdifficulty)]
        self.x = 1536*1.5
        self.y = 968//2-20
        self.tempx = self.x
        self.tempy = self.y

    def update(self, deltatime):
        self.tempx = scale(self.x - self.speed *
                           (time.time()-deltatime-self.time) * 60)
        self.tempy = scale(self.y)

    def draw(self, win):
        win.blit(Monster.monsterimg[self.imgindex], (self.tempx, self.tempy))
        self.drawweak(win)

    def drawweak(self, win):
        for row in range(len(self.weakskill)):
            w1, w2, w3 = sorted(self.weakskill[row])
            if w1 == "fire" and w2 == "fire" and w3 == "fire":
                win.blit(Monster.skillist[0],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w1 == "fire" and w2 == "fire" and w3 == "forest":
                win.blit(Monster.skillist[1],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w1 == "fire" and w2 == "fire" and w3 == "water":
                win.blit(Monster.skillist[2],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w1 == "forest" and w2 == "forest" and w3 == "forest":
                win.blit(Monster.skillist[3],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w3 == "forest" and w2 == "forest" and w1 == "fire":
                win.blit(Monster.skillist[4],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w1 == "forest" and w2 == "forest" and w3 == "water":
                win.blit(Monster.skillist[5],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w1 == "water" and w2 == "water" and w3 == "water":
                win.blit(Monster.skillist[6],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w3 == "water" and w2 == "water" and w1 == "fire":
                win.blit(Monster.skillist[7],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w3 == "water" and w2 == "water" and w1 == "forest":
                win.blit(Monster.skillist[8],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))
            if w1 == "fire" and w2 == "forest" and w3 == "water":
                win.blit(Monster.skillist[9],
                         (self.tempx + scale(40*(row % 3)), self.tempy-scale(40*(row//3)+50), scale(20), scale(20)))

            # for index in range(len(self.weakskill[row])):
                # win.blit(Monster.elementimg[self.weakskill[row][index]],
                #          (self.tempx + scale(40+25*index), self.tempy-scale(40*row+40), scale(20), scale(20)))
