import pygame as pygame

from LR.spritesheet import Spritesheet
from LR.tilemap import Tilemap

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

level_map = [
[-1,-1,-1,-1,-1,152,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,152,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,233,233,-1,-1,152,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[188,188,188,235,245,245,245,76,202,202,202,202,95,95,95,95,132,-1,-1,-1],
[-1,-1,-1,235,-1,-1,-1,76,-1,-1,-1,-1,-1,-1,-1,-1,132,-1,-1,-1],
[-1,-1,-1,235,-1,-1,-1,76,-1,-1,-1,-1,-1,-1,-1,-1,132,-1,-1,-1],
[-1,-1,-1,235,-1,-1,-1,76,-1,-1,-1,-1,-1,-1,-1,-1,132,-1,-1,-1],
[173,173,173,173,173,-1,209,76,-1,-1,-1,-1,-1,-1,-1,-1,132,-1,-1,-1],
[-1,-1,229,-1,-1,-1,209,204,204,204,229,-1,-1,-1,-1,-1,132,-1,-1,-1],
[222,222,222,222,222,222,222,222,222,222,222,222,222,222,222,222,222,222,222,222]
]

spritesheet = Spritesheet(
    "assets/tileset3b.png",
    tile_width=24, tile_height=24,
    colorkey=pygame.Color(255, 0, 255)
)
tilemap = Tilemap(spritesheet, level_map=level_map)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 255, 0))

    screen.blit(tilemap.surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()