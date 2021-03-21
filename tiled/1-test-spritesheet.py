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

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

spritesheet = Spritesheet(
    "assets/tileset3b.png",
    tile_width=24,
    tile_height=24,
    colorkey=pygame.Color(255, 0, 255)
)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 255))

    screen.blit(spritesheet.image_at(tile_col=8, tile_row=11), (0, 0))
    screen.blit(spritesheet.image_at(tile_col=9, tile_row=11), (100, 0))
    screen.blit(spritesheet.image_at(tile_col=10, tile_row=11), (200, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()