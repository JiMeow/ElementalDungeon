import pygame
from setting import *


def loadPlayerimg():
    playerimg = []
    for i in range(1, 5):
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


class Player():
    playerimg = loadPlayerimg()
    elementimg = loadElementimg()
    starimg = pygame.transform.scale(
        pygame.image.load(f"photo/star.png"), (scale(30), scale(30)))

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
        self.atk = 0

    def draw(self, win):

        win.blit(Player.playerimg[self.id-1],
                 (scale(50), scale(800-100*self.id), scale(50), scale(34)))
        self.drawelement(win)
        if self.atksuccess != 0:
            self.drawatksuccess(win)
            self.atksuccess -= 1

    def drawname(self, win):
        """
        draw player name at stage by rect

        Args:
            win (pygame.display): pygame window
            stage (int): stage of game. Defaults to 0.
        """
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.name), True, "black")
        rect = text.get_rect()
        rect.center = (self.x, self.y)
        rect.x += self.width//2
        rect.y += self.height//2
        win.blit(text, rect)

    def drawelement(self, win):
        for index in range(len(self.elementSlot)):
            win.blit(Player.elementimg[self.elementSlot[index]],
                     (scale(40+25*index), scale(800-self.height-100*self.id), scale(20), scale(20)))

    def drawatksuccess(self, win):
        win.blit(Player.starimg, (scale(100), scale(
            800-100*self.id), scale(20), scale(20)))

    def invokeskill(self, skill):
        """
        control player move by keyboard then change speed of player
        if player on slab and press key 'down' or 's' then drop from slab 
        can not move is player not in frame of screen
        """
        if skill == pygame.K_r:
            if len(self.elementSlot) == 3:
                self.atkelement = list(self.elementSlot)
                self.elementSlot = []
                self.atk = 1

        if len(self.elementSlot) == 3:
            self.elementSlot.pop(0)
        if skill == pygame.K_q:
            self.elementSlot.append("water")
        if skill == pygame.K_w:
            self.elementSlot.append("fire")
        if skill == pygame.K_e:
            self.elementSlot.append("forest")

    def update(self, dt=1/60):
        """
        update player position by speed and delta time then 
        set player (x,y) position to collision information
        then check collision with all obstacle in map 
        and update information of player

        Args:
            dt (float, float): delta time check for lag. Defaults to 1/60.
            collision (Collision, Nonce): collision information for check collision. Defaults to None.
        """
        # print(f"{self.x}+{self.vel * 60}", end=":")
        self.x += self.vel * 60 * dt
        if self.x > width*2:
            self.x -= width - scale(48)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
