import csv

import pygame

from consts import *

from spritesheet import Spritesheet

pygame.display.set_caption("Test")

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN_COLOR, self.rect)

    def update(self, events):
        global speed

        self.acc = pygame.Vector2(0, 0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.acc.x = 0.1
        elif keys[pygame.K_LEFT]:
            self.acc.x = -0.1

        # if keys[pygame.K_UP]:
        #     self.acc.y = -0.2
        # elif keys[pygame.K_DOWN]:
        #     self.acc.y = 0.2

        self.vel += self.acc
        self.rect.center = self.rect.center + self.vel + (self.acc / 2)

        if self.rect.right > start_x + map_width_px:
            self.rect.right = start_x + map_width_px

        #...


    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Player({self.x}, {self.y}, {self.dx}, {self.dy})"


def draw_text(text, x, y, size=18, color=WHITE_COLOR):
    font_name = pygame.font.match_font('hack')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

clock = pygame.time.Clock()

level1_map = []
with open("assets/5.csv") as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        ints_row = [int(i) for i in row]
        level1_map.append(ints_row)

spritesheet = Spritesheet(
    "assets/tileset3b.png",
    tile_width=24, tile_height=24,
    colorkey=pygame.Color(255, 0, 255)
)

background = pygame.Surface((screen.get_width(), screen.get_height()))
background.fill(color=BLACK_COLOR)

map_width_px = len(level1_map[0]) * 24
map_height_py = len(level1_map) * 24
start_x = (screen.get_width() - map_width_px) // 2
start_y = (screen.get_height() - map_height_py) // 2

player = Player(screen.get_width() // 2, screen.get_height() // 2, 24, 24)

is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    screen.blit(background, (0, 0))

    for c, row in enumerate(level1_map):
        for r, item_code in enumerate(row):
            if item_code != -1:
                rect = pygame.Rect(
                    start_x + r * spritesheet.tile_width,
                    start_x + c * spritesheet.tile_height,
                    spritesheet.tile_width,
                    spritesheet.tile_height
                )

                tile_col = item_code % 20
                tile_row = item_code // 20
                tile_img = spritesheet.image_at(
                    tile_col=tile_col, tile_row=tile_row
                )
                screen.blit(tile_img, rect.topleft)

    player.update(events)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()