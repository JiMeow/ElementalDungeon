from setting import scale


class checkDamage():
    def __init__(self, map):
        self.player = map.player
        self.map = map
        self.monster = map.monster

    def update(self, map):
        self.player = map.player
        self.map = map
        self.monster = map.monster
        self.monsterAttackPlayer()
        self.playerAttackMonster()
        
    def playerAttackMonster(self):
        pass

    def monsterAttackPlayer(self):
        if scale(50) > self.monster.tempx+scale(150):
            self.player.atk = 1
            