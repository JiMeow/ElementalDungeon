from src.setting import *
import pygame


class Tile():

    def __init__(self, id) -> None:
        self.type = id
        self.img = photo[id]
        self.img.set_colorkey((0, 0, 0))
        self.rect = self.img.get_rect()

    def draw(self, win, player):
        pygame.Surface.blit(win, self.img, (self.rect.x+scale(50)-player.x,
                            self.rect.y, self.rect.width, self.rect.height))


def cut_picture(path):
    surface = pygame.image.load(f"src/{path}")
    tile_num_x = surface.get_size()[0] // 16
    tile_num_y = surface.get_size()[1] // 16
    cut_tiles = []
    for row in range(tile_num_x):
        for col in range(tile_num_y):
            x = row * 16
            y = col * 16
            new_surface = pygame.Surface((16, 16))
            new_surface.blit(surface, (0, 0), pygame.Rect(
                y, x, 16, 16))
            new_surface = pygame.transform.scale(
                new_surface, (scale(48), scale(48)))
            cut_tiles.append(new_surface)

    return cut_tiles


photo = cut_picture(
    "map/0x72_DungeonTilesetII_v1.3.1/0x72_DungeonTilesetII_v1.3.png")
