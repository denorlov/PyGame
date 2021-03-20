from copy import deepcopy

import pygame


class Tilemap:
    def __init__(self, spritesheet, level_map):
        """
        spritesheet is SpriteSheet with tile images
        map is 2d list with tile codes map
        """
        self.spritesheet = spritesheet
        self.level_map = level_map

        self.surface = pygame.Surface((self.get_width(), self.get_height()))
        self.surface.set_colorkey(spritesheet.sheet.get_colorkey())
        self.surface = self.surface.convert()

        for y, row in enumerate(self.level_map):
            for x, item_code in enumerate(row):
                if item_code != -1:
                    tile_img = self.spritesheet[item_code]
                    tile_img.set_colorkey(spritesheet.sheet.get_colorkey())
                    tile_img = tile_img.convert()
                    self.surface.blit(
                        tile_img,
                        (x * self.spritesheet.tile_width, y * self.spritesheet.tile_height)
                    )

    def get_height(self):
        return len(self.level_map) * self.spritesheet.tile_height

    def get_width(self):
        return len(self.level_map[0]) * self.spritesheet.tile_width
