from copy import deepcopy

import pygame


class Tilemap:
    def __init__(self, spritesheet, level_map):
        """
        spritesheet is SpriteSheet with tile images
        level_map is 2d list with codes map
        """
        self.spritesheet = spritesheet
        self.level_map = level_map

        self.surface = pygame.Surface((self.get_width(), self.get_height()))
        self.surface.set_colorkey(spritesheet.sheet.get_colorkey())
        self.surface = self.surface.convert()

        for c, row in enumerate(self.level_map):
            for r, item_code in enumerate(row):
                if item_code != -1:
                    tile_img = self.spritesheet[item_code]
                    tile_img.set_colorkey(spritesheet.sheet.get_colorkey())
                    tile_img = tile_img.convert()
                    self.surface.blit(
                        tile_img,
                        (r * self.spritesheet.tile_width, c * self.spritesheet.tile_height)
                    )

    def get_map_rows(self):
        return len(self.level_map)

    def get_map_cols(self):
        return len(self.level_map[0])

    def get_height(self):
        return self.get_map_rows() * self.spritesheet.tile_height

    def get_width(self):
        return self.get_map_cols() * self.spritesheet.tile_width

    def get_tile_height(self):
        return self.spritesheet.tile_height

    def get_tile_width(self):
        return self.spritesheet.tile_width

    def __str__(self):
        return self.level_map

    def __repr__(self):
        return f"Tilemap({self.get_width}*{self.get_height}, {self.level_map}, {self.spritesheet})"

