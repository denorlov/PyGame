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
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

level1_map = [
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

spritesheet = Spritesheet(
    "assets/tileset3b.png",
    tile_width=24, tile_height=24,
    colorkey=pygame.Color(255, 0, 255)
)

code_to_tile = {
    220:spritesheet.image_at(tile_col=0, tile_row=11),
    222:spritesheet.image_at(tile_col=2, tile_row=11),
    223:spritesheet.image_at(tile_col=3, tile_row=11),
    229:spritesheet.image_at(tile_col=9, tile_row=11)
}

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 255))

    screen.blit(spritesheet.image_at(tile_col=8, tile_row=11), (0, 400))
    screen.blit(spritesheet.image_at(tile_col=9, tile_row=11), (100, 400))
    screen.blit(spritesheet.image_at(tile_col=10, tile_row=11), (200, 400))

    for c, row in enumerate(level1_map):
        for r, item_code in enumerate(row):
            if item_code != -1:
                rect = pygame.Rect(
                    r * spritesheet.tile_width,
                    c * spritesheet.tile_height,
                    spritesheet.tile_width,
                    spritesheet.tile_height
                )

                pygame.draw.rect(screen, GREEN_COLOR, rect, 2)

                if item_code in code_to_tile:
                    tile_img = code_to_tile[item_code]
                    screen.blit(tile_img, rect.topleft)

                draw_text(
                    text=f"{item_code}",
                    size=18,
                    color=GREEN_COLOR,
                    x=r*spritesheet.tile_width + 2,
                    y=c*spritesheet.tile_height + 2
                )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()