import pygame
from setting import *


def loadPlayerimg():
    playerimg = []
    for i in range(1, 15):
        imgleft = pygame.transform.scale(
            pygame.image.load(f"photo/player{i}.png"), (scale(50), scale(34)))
        playerimg.append(pygame.transform.flip(imgleft, True, False))
    return playerimg


def loadElementimg():
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
    return elementimg


def loadStarimg():
    return pygame.transform.scale(
        pygame.image.load(f"photo/star.png"), (scale(30), scale(30)))


class Player():
    playerimg = loadPlayerimg()
    elementimg = loadElementimg()
    starimg = loadStarimg()

    def __init__(self, id, x, y, width, height, color, name):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = scale(1.5)
        self.elementSlot = []
        self.atksuccess = 0
        self.timeinvokedelay = 0
        self.atk = 0

    def draw(self, win):
        if self.id > 6:
            win.blit(Player.playerimg[self.id-1],
                     (scale(250), scale(800-100*(self.id-6)), scale(50), scale(34)))
        else:
            win.blit(Player.playerimg[self.id-1],
                     (scale(50), scale(800-100*self.id), scale(50), scale(34)))

        self.drawelement(win)
        self.drawname(win)
        if self.atksuccess != 0:
            self.drawatksuccess(win)
            self.atksuccess -= 1
        if self.timeinvokedelay != 0:
            self.timeinvokedelay -= 1

    def drawname(self, win):
        font = pygame.font.Font(None, int(scale(20)))
        text = font.render(str(self.name), True, "black")
        if self.id > 6:
            rect = text.get_rect(
                center=(scale(277), scale(845-100*(self.id-6))))
            win.blit(text, rect)
        else:
            rect = text.get_rect(
                center=(scale(77), scale(845-100*self.id)))
            win.blit(text, rect)

    def drawelement(self, win):
        for index in range(len(self.elementSlot)):
            if self.id > 6:
                win.blit(Player.elementimg[self.elementSlot[index]],
                         (scale(240+25*index), scale(800-100*(self.id-6)-self.height), scale(20), scale(20)))
            else:
                win.blit(Player.elementimg[self.elementSlot[index]],
                         (scale(40+25*index), scale(800-100*self.id-self.height), scale(20), scale(20)))

    def drawatksuccess(self, win):
        if self.id > 6:
            win.blit(Player.starimg, (scale(310), scale(
                800-100*(self.id-6)), scale(20), scale(20)))
        else:
            win.blit(Player.starimg, (scale(110), scale(
                800-100*self.id), scale(20), scale(20)))

    def invokeskill(self, skill):
        if skill == pygame.K_r or skill == pygame.K_SPACE or skill == pygame.K_KP_ENTER:
            if self.timeinvokedelay != 0:
                return
            if len(self.elementSlot) == 3:
                self.atkelement = list(self.elementSlot)
                self.elementSlot = []
                self.atk = 1

        if len(self.elementSlot) == 3:
            self.elementSlot.pop(0)
        if skill == pygame.K_q or skill == pygame.K_j or skill == pygame.K_KP_1:
            self.elementSlot.append("fire")
        if skill == pygame.K_w or skill == pygame.K_k or skill == pygame.K_KP_2:
            self.elementSlot.append("forest")
        if skill == pygame.K_e or skill == pygame.K_l or skill == pygame.K_KP_3:
            self.elementSlot.append("water")

    def update(self, dt=1/60):
        self.x += self.vel * 60 * dt
        if self.x > width*2:
            self.x -= width - scale(48)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
