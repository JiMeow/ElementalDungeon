from setting import *
from tile import Tile
from bookskill import BookSkill


class Map():
    def __init__(self, tilelist, win, player, bookskill):
        self.player = player
        self.win = win
        self.tile = tilelist
        self.bookskill = bookskill
        for layer in range(2):
            for row in range(len(tilelist[layer])):
                for col in range(len(tilelist[layer][0])):
                    if tilelist[layer][row][col] != -1:
                        tile = Tile(tilelist[layer][row][col])
                        tile.rect.y = row*scale(48)
                        tile.rect.x = col*scale(48)
                        self.tile[layer][row][col] = tile

    def draw(self):
        for layer in range(2):
            for row in range(len(self.tile[layer])):
                for col in range(len(self.tile[layer][0])):
                    if self.tile[layer][row][col] != -1:
                        self.tile[layer][row][col].draw(self.win, self.player)
        self.monster.draw(self.win)
        self.bookskill.draw()

    def update(self, player, monster):
        self.player = player
        self.monster = monster


def readmap():
    result = []
    for i in range(2):
        ans = []
        with open(f"map/map_{i+1}.csv", "r") as f:
            r = f.read().strip().split('\n')
            for i in range(len(r)):
                r[i] = r[i].strip().split(',')
                for j in range(len(r[i])):
                    r[i][j] = int(r[i][j])
                ans.append(r[i])
        result.append(ans)
    return result
