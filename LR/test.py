import pygame as pygame

from LR.spritesheet import SpriteSheet
from LR.tilemap import TileMap

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
#screen = pygame.display.set_mode(SCREEN_SIZE, flags=pygame.FULLSCREEN)
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

map = [
[340,344,344,344,342,342,344,344,-1,342,342,342,340,340,135,343,343,343,343,262],
[261,158,-1,156,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,135,-1,-1,-1,-1,262],
[225,225,225,225,225,152,112,112,112,112,112,112,112,112,135,156,-1,-1,-1,262],
[261,-1,-1,-1,-1,152,-1,-1,207,207,235,-1,-1,225,225,225,235,225,225,225],
[261,-1,-1,-1,-1,152,-1,-1,207,207,235,-1,-1,-1,-1,-1,235,-1,-1,262],
[261,-1,-1,-1,-1,152,-1,-1,207,207,235,-1,-1,-1,-1,-1,235,-1,-1,262],
[158,-1,-1,-1,-1,152,-1,-1,226,208,226,226,226,226,226,226,235,-1,-1,262],
[226,226,235,226,226,226,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,235,-1,-1,262],
[261,-1,235,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,235,-1,-1,262],
[261,-1,235,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,235,-1,-1,262],
[223,222,222,223,223,222,223,152,222,222,222,222,222,222,222,222,235,-1,-1,262],
[261,-1,-1,-1,-1,156,-1,152,-1,-1,-1,-1,-1,-1,156,-1,235,-1,-1,262],
[261,-1,-1,152,220,220,220,220,220,-1,-1,-1,-1,-1,220,220,220,220,220,152],
[261,-1,-1,152,-1,-1,-1,-1,-1,-1,-1,156,-1,-1,-1,-1,-1,-1,-1,152],
[220,220,220,220,220,220,220,220,220,220,220,220,220,220,220,220,220,220,220,220]
]

spritesheet = SpriteSheet("tileset3b.png", 24, 24, pygame.Color(255, 0, 255))
tilemap = TileMap(spritesheet, map)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    x = (screen.get_width() - tilemap.get_width()) // 2
    y = (screen.get_height() - tilemap.get_height()) // 2

    screen.blit(tilemap.surface, (x, y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()