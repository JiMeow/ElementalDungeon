import pygame
import time
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
        pygame.image.load(f"photo/invoke.png"), (scale(30), scale(30)))
    img["invoke"] = imgtemp
    imgtemp = pygame.transform.scale(
        pygame.image.load(f"photo/bookskill.png"), (scale(250), scale(180)))
    img["book"] = imgtemp

    return img


class Layout():
    img = loadimg()
    colorlist = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrod', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey',
                 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslateblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'violetred', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']

    def __init__(self, win, clock):
        self.win = win
        self.font = pygame.font.Font(None, int(scale(20)))
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

    def updatescoreboard(self, scoreboard):
        self.scoreboard = scoreboard

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

        self.textScore = pygame.font.Font(None, int(scale(40))).render(
            f"Stage: {self.monster.id-1}", True, "white")
        self.win.blit(self.textScore,
                      self.textScore.get_rect(topleft=(scale(1395), scale(50))))

        if self.monster.id <= 5:
            self.win.blit(
                Layout.img["book"], (width//2-scale(125), height-scale(240), scale(250), scale(180)))

            self.win.blit(
                Layout.img["fire"], (width//2-scale(80), height-scale(200), scale(30), scale(30)))
            self.textfire = pygame.font.Font(None, int(scale(30))).render(
                f": q", True, "Black")
            self.win.blit(self.textfire,
                          self.textfire.get_rect(topleft=(width//2-scale(45), height-scale(195))))

            self.win.blit(
                Layout.img["forest"], (width//2-scale(80), height-scale(150), scale(30), scale(30)))
            self.textforest = pygame.font.Font(None, int(scale(30))).render(
                f": w", True, "Black")
            self.win.blit(self.textforest,
                          self.textforest.get_rect(topleft=(width//2-scale(45), height-scale(145))))

            self.win.blit(
                Layout.img["water"], (width//2+scale(15), height-scale(200), scale(30), scale(30)))
            self.textwater = pygame.font.Font(None, int(scale(30))).render(
                f": e", True, "Black")
            self.win.blit(self.textwater,
                          self.textwater.get_rect(topleft=(width//2+scale(50), height-scale(195))))

            self.win.blit(
                Layout.img["invoke"], (width//2+scale(15), height-scale(150), scale(30), scale(30)))
            self.textinvoke = pygame.font.Font(None, int(scale(30))).render(
                f": r", True, "Black")
            self.win.blit(self.textinvoke,
                          self.textinvoke.get_rect(topleft=(width//2+scale(50), height-scale(145))))

        self.textscoreboard = pygame.font.Font(None, int(scale(30))).render(
            f"scoreboard", True, "White")
        self.win.blit(self.textscoreboard,
                      self.textscoreboard.get_rect(topleft=(scale(1395), scale(100))))
        index = 0
        # print(self.scoreboard)
        for name, data in sorted(self.scoreboard.items(), key=lambda x: x[1], reverse=True):
            score, id = data
            if self.status[id-1] == 1:
                if index == 0:
                    self.textscoreboard = pygame.font.Font(None, int(scale(25))).render(
                        f"{name}{' '*(7-len(name))} : {' '*(3-len(str(score)))} {score}", True, Layout.colorlist[int(time.time()*2) % len(Layout.colorlist)])
                else:
                    self.textscoreboard = pygame.font.Font(None, int(scale(25))).render(
                        f"{name}{' '*(7-len(name))} : {' '*(3-len(str(score)))} {score}", True, "White")
                self.win.blit(self.textscoreboard,
                              self.textscoreboard.get_rect(topleft=(scale(1400), scale(140+35*index))))
                index += 1
        pygame.display.update()
