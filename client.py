import pygame
import json
from threading import *
from utils import *
from ui import UI
from setting import *
from map import Map, readmap
from network import Network
from player import Player
from layout import Layout
from checkDamage import checkDamage
from bookskill import BookSkill
import time


class Game():
    def __init__(self, username, password):
        self.network = Network()
        self.player, self.servertime = self.network.getInitData()
        self.player.name = username

        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("ElementalDungeon")
        pygame.init()
        self.deltatime = time.time()-self.servertime
        self.clock = pygame.time.Clock()

        self.run = True
        self.frame = 0

        self.allp, self.status, self.monster = getDataFromServer(
            self.network, self.player)
        self.tempallp = list(self.allp)
        self.tempstatus = dict(self.status)
        self.tempmonster = list(self.monster)
        self.tempplayerreturn = {"playeratksuccess": 0,
                                 "timeinvokedelay": 0,
                                 "scoreboard": {}, }
        self.scoreboard = {}
        self.bookskill = BookSkill(
            self.win, (scale(50), scale(50), scale(75), scale(75)))

        self.map = Map(readmap(), self.win, self.player, self.bookskill)
        self.layout = Layout(self.win, self.clock)

        self.thread = Thread(target=getDataFromServer, args=(
            self.network, self.player, self.tempallp, self.tempstatus, self.tempmonster))

        self.checkDamage = checkDamage(self.map)
        self.beforetime = time.time()

    def play(self):
        while self.run:
            self.clock.tick(60)
            dt = time.time() - self.beforetime
            self.beforetime = time.time()

            if not self.thread.is_alive():
                setdatafromserver(self.allp, self.status, self.monster, self.player, self.scoreboard,
                                  self.tempallp, self.tempstatus, self.tempmonster, self.tempplayerreturn)
                self.tempplayerreturn = {}
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.tempallp, self.tempstatus, self.tempmonster, self.tempplayerreturn))
                self.thread.start()
                self.player.atk = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    self.network.disconnect()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_w or event.key == pygame.K_e or\
                            event.key == pygame.K_r or event.key == pygame.K_j or event.key == pygame.K_k or\
                            event.key == pygame.K_l or event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or\
                            event.key == pygame.K_KP_1 or event.key == pygame.K_KP_2 or event.key == pygame.K_KP_3:
                        self.player.invokeskill(event.key)
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                        pygame.quit()
                        self.network.disconnect()
                        break
                self.bookskill.get_event(event)

            if not self.run:
                break

            self.monster[0].update(self.deltatime)
            if self.monster[0].tempx > width:
                self.player.update(dt)

            self.map.update(self.player, self.monster[0])
            self.checkDamage.update(self.map)

            if not self.thread.is_alive():
                setdatafromserver(self.allp, self.status, self.monster, self.player, self.scoreboard,
                                  self.tempallp, self.tempstatus, self.tempmonster, self.tempplayerreturn)
                self.tempplayerreturn = {}
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.tempallp, self.tempstatus, self.tempmonster, self.tempplayerreturn))
                self.thread.start()
                self.player.atk = 0
            redrawWindow(self.layout, self.map,  self.player,
                         self.allp, self.status, self.monster[0], self.scoreboard)
            self.frame += 1


datafromUI = []
ui = UI(datafromUI)
while True:
    ui.show()
    if len(datafromUI) != 2:
        break
    username, password = datafromUI
    game = Game(username, password)
    game.play()

print("BYE")
