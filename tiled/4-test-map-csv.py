import csv

import pygame as pygame

from tiled.spritesheet import Spritesheet
from tiled.tilemap import Tilemap

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

def draw_text(text, size, color, x, y):
    font_name = pygame.font.match_font('hack')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

pygame.init()
pygame.display.set_caption("Test")
#screen = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE, flags=pygame.FULLSCREEN)

clock = pygame.time.Clock()

level1_map = []
with open("assets/4.csv") as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        ints_row = [int(i) for i in row]
        level1_map.append(ints_row)

spritesheet = Spritesheet(
    "assets/tileset3b.png",
    tile_width=24, tile_height=24,
    colorkey=pygame.Color(255, 0, 255)
)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    #screen.fill((0, 0, 255))

    for c, row in enumerate(level1_map):
        for r, item_code in enumerate(row):
            if item_code != -1:
                rect = pygame.Rect(
                    r * spritesheet.tile_width,
                    c * spritesheet.tile_height,
                    spritesheet.tile_width,
                    spritesheet.tile_height
                )

                tile_col = item_code % 20
                tile_row = item_code // 20
                tile_img = spritesheet.image_at(tile_col=tile_col, tile_row=tile_row)
                screen.blit(tile_img, rect.topleft)

                # draw_text(
                #     text=f"{item_code}",
                #     size=18,
                #     color=GREEN_COLOR,
                #     x=r*spritesheet.tile_width + 2,
                #     y=c*spritesheet.tile_height + 2
                # )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()