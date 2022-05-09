import pygame


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

    def draw(self):
        self.map.draw()
        self.player.draw(self.win)
        for player in self.allplayer:
            if self.status[player.id-1] == 1 and player.id != self.player.id:
                player.draw(self.win)

        self.text = self.font.render(
            f"{self.clock.get_fps():.2f}", True, "white")
        self.textrect = self.text.get_rect(topleft=(10, 50))
        self.win.blit(self.text, self.textrect)
        pygame.display.update()
