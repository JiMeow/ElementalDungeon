from src.setting import *


class checkDamage():
    def __init__(self, map):
        self.player = map.player
        self.map = map
        # self.monster = map.monster

    def update(self, map):
        self.player = map.player
        self.map = map
        self.monster = map.monster
        self.monsterAttackPlayer()

    def monsterAttackPlayer(self):
        if scale(50) > self.monster.tempx+scale(150):
            self.player.atk = 9999
            