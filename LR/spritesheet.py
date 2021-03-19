import pygame

class SpriteSheet(object):
    def __init__(self, filename, tile_width, tile_height, colorkey = None):
        self.sheet = pygame.image.load(filename)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = self.sheet.get_at((0,0))
            self.sheet.set_colorkey(colorkey, pygame.RLEACCEL)
        self.sheet.convert()

        self.tile_widht = tile_width
        self.tile_height = tile_height

    def __getitem__(self, item):
        return self.image_at(item)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            tile_x, tile_y = index
            return self.image_at(tile_x, tile_y)
        else:
            rows = self.sheet.get_height() // self.tile_height
            cols = self.sheet.get_width() // self.tile_widht
            tile_x = index % cols
            tile_y = index // cols
            return self.image_at(tile_x, tile_y)

    def image_at(self, tile_x, tile_y):
        "Loads image from tile_x_y_pair position"
        rect = pygame.Rect(
            tile_x * self.tile_widht,
            tile_y * self.tile_height,
            self.tile_widht,
            self.tile_height
        )
        image = pygame.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        return image