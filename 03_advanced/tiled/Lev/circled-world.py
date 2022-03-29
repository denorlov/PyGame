class Spritesheet(object):
    def __init__(self, filename, tile_width, tile_height, colorkey=None):
        self.filename = filename
        self.sheet = pygame.image.load(filename)
        self.colorkey = colorkey
        self.sheet = self.sheet.convert()

        self.tile_width = tile_width
        self.tile_height = tile_height

    def image_at(self, tile_col, tile_row):
        "Loads image from tile_col and tile_row tile"
        rect = pygame.Rect(
            tile_col * self.tile_width,
            tile_row * self.tile_height,
            self.tile_width,
            self.tile_height
        )
        image = pygame.Surface(rect.size)
        if self.colorkey != None:
            image.set_colorkey(self.colorkey)
        image.blit(self.sheet, (0, 0), rect)
        return image

    def blit_tile(self, surface, tile_col, tile_row, x, y):
        "Loads image from tile_col and tile_row tile"
        rect = pygame.Rect(
            tile_col * self.tile_width,
            tile_row * self.tile_height,
            self.tile_width,
            self.tile_height
        )
        if self.colorkey != None:
            self.sheet.set_colorkey(self.colorkey)
        surface.blit(self.sheet, (x, y), rect)

    def __getitem__(self, tile_col, tile_row):
        return self.image_at(tile_col, tile_row)

    def __str__(self):
        return f"{self.tile_width} * {self.tile_height}"

    def __repr__(self):
        return f"Spritesheet({self.tile_width} * {self.tile_height}, {self.filename})"


class Hero:
    def __init__(self, x, y, width, height):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        self.width = width
        self.height = height

    def draw(self, surface_to_draw):
        pygame.draw.rect(surface_to_draw, (255, 120, 40), (self.position.x, self.position.y, self.width, self.height))

    def update(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            a = 0.5
        else:
            a = 0.1
        if keys[pygame.K_LEFT]:
            print('left')
            self.velocity.x -= a
        if keys[pygame.K_RIGHT]:
            print('right')
            self.velocity.x += a
        if keys[pygame.K_UP]:
            print('left')
            self.velocity.y -= a
        if keys[pygame.K_DOWN]:
            print('right')
            self.velocity.y += a
        self.position = self.position + self.velocity
        if self.position.x >= 766:
            self.position.x = -23
        if self.position.y >= 360:
            self.position.y = -23
        if self.position.x <= -24:
            self.position.x = 768
        if self.position.y <= -24:
            self.position.y = 360



import pygame as pygame
import csv

SCREEN_SIZE = WIDTH, HEIGHT = 720, 360

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

gr = []
f = open("sheet.csv", mode='r')
for i in f:
    dwa = i.split()
    for j in dwa:
        gr.append(j.split(','))

ss = Spritesheet(
    "tileset3b.png",
    24,
    24,
    pygame.Color(255, 0, 255)
)

code_to_tile = {
    220: ss.image_at(tile_col=0, tile_row=11),
    222: ss.image_at(tile_col=2, tile_row=11),
    223: ss.image_at(tile_col=3, tile_row=11),
    229: ss.image_at(tile_col=9, tile_row=11)
}

hero = Hero(100, 100, 24, 24)

is_running = True
while is_running:
    events =pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((30, 40, 30))
    for i, g in enumerate(gr):
        for j, z in enumerate(g):
            ss.blit_tile(screen, int(z) % 20, int(z) // 20, j * 24, i * 24)

    hero.update(events)
    hero.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
