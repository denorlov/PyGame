from copy import deepcopy

import pygame


class TileMap:
    def __init__(self, spritesheet, map):
        """
        spritesheet is SpriteSheet with tile images
        map is 2d list with tile codes map
        """
        self.spritesheet = spritesheet
        self.map = deepcopy(map)

        self.surface = pygame.Surface((self.get_width(), self.get_height()))
        self.draw(self.surface)

    def draw(self, surface):
        for y, row in enumerate(self.map):
            for x, item_code in enumerate(row):
                if item_code != -1:
                    tile_img = self.spritesheet[item_code]
                    surface.blit(tile_img, (x * self.spritesheet.tile_widht, y * self.spritesheet.tile_height))

    def get_height(self):
        return len(self.map) * self.spritesheet.tile_height

    def get_width(self):
        return len(self.map[0]) * self.spritesheet.tile_widht
