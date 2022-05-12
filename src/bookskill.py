from src.setting import *
import pygame


class BookSkill():

    skillist = []
    for i in range(1, 11):
        imgleft = pygame.transform.scale(
            pygame.image.load(f"src/photo/skill_{i}.jpg"), (scale(40), scale(40)))
        skillist.append(imgleft)

    bookskillimg = pygame.transform.scale(
        pygame.image.load("src/photo/bookskill2.png"), (scale(400), scale(300)))

    elementimg = {}
    img = pygame.transform.scale(
        pygame.image.load(f"src/photo/fireelement.png"), (scale(25), scale(25)))
    elementimg["fire"] = img
    img = pygame.transform.scale(
        pygame.image.load(f"src/photo/waterelement.png"), (scale(25), scale(25)))
    elementimg["water"] = img
    img = pygame.transform.scale(
        pygame.image.load(f"src/photo/forestelement.png"), (scale(25), scale(25)))
    elementimg["forest"] = img

    skillnum = [['fire', 'fire', 'fire'],
                ['fire', 'fire', 'forest'],
                ['fire', 'fire', 'water'],
                ['forest', 'forest', 'forest'],
                ['forest', 'forest', 'fire'],
                ['forest', 'forest', 'water'],
                ['water', 'water', 'water'],
                ['water', 'water', 'fire'],
                ['water', 'water', 'forest'],
                ['fire', 'forest', 'water']]

    def __init__(self, win, rect, imagepath="src/photo/spellbook.png"):
        self.win = win
        self.rect = pygame.Rect(rect)
        self.isdraw = 0
        self.image = pygame.transform.scale(
            pygame.image.load(imagepath), (self.rect.width, self.rect.height))

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.isdraw += 1

    def draw(self):
        self.win.blit(self.image, self.rect)
        if self.isdraw % 2 == 1:
            self.showspellbook()

    def showspellbook(self):
        self.win.blit(BookSkill.bookskillimg, (scale(300), scale(20)))

        for i in range(10):
            if i < 5:
                self.win.blit(BookSkill.skillist[i],
                              (scale(345), scale(45)+scale(41)*i))
                for j in range(3):
                    index = BookSkill.skillnum[i][j]
                    self.win.blit(BookSkill.elementimg[index],
                                  (scale(390)+scale(30)*j, scale(55)+scale(41)*i))
            else:
                self.win.blit(BookSkill.skillist[i],
                              (scale(512), scale(45)+scale(41)*(i-5)))
                for j in range(3):
                    index = BookSkill.skillnum[i][j]
                    self.win.blit(BookSkill.elementimg[index],
                                  (scale(557)+scale(30)*j, scale(55)+scale(41)*(i-5)))

# screen = pygame.display.set_mode((800, 600))
# bs = BookSkill(rect=(100, 100, 100, 100))

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         bs.get_event(event)
#     bs.draw(screen)
#     pygame.display.update()
