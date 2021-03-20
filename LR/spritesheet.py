import pygame

class Spritesheet(object):
    def __init__(self, filename, tile_width, tile_height, colorkey = None):
        self.filename = filename
        self.sheet = pygame.image.load(filename)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = self.sheet.get_at((0,0))
            self.sheet.set_colorkey(colorkey, pygame.RLEACCEL)
        self.sheet.convert()

        self.tile_width = tile_width
        self.tile_height = tile_height

    def __getitem__(self, item):
        return self.image_at(item)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            tile_col, tile_row = index
            return self.image_at(tile_col, tile_row)
        else:
            cols = self.sheet.get_width() // self.tile_width
            tile_col = index % cols
            tile_row = index // cols
            return self.image_at(tile_col, tile_row)

    def image_at(self, tile_col, tile_row):
        "Loads image from tile_x_y_pair position"
        rect = pygame.Rect(
            tile_col * self.tile_width,
            tile_row * self.tile_height,
            self.tile_width,
            self.tile_height
        )
        image = pygame.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey(self.sheet.get_colorkey())
        image = image.convert()
        return image

    def __str__(self):
        return f"{self.tile_width} * {self.tile_height}"

    def __repr__(self):
        return f"Spritesheet({self.tile_width} * {self.tile_height}, {self.filename})"
