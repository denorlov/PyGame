import pygame as pygame

from tiled.spritesheet import Spritesheet

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

sprite_sheet = Spritesheet(
    '../assets/tileset3b.png',
    24, 24,
    colorkey=(255, 0, 255)
)
# col,row = 2,3
# col, row = 5,5
# col, row = 7,5

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 0))
    sprite_sheet.blit_tile(screen, 2, 3, 0, 0)
    sprite_sheet.blit_tile(screen, 5, 5, 100, 100)
    sprite_sheet.blit_tile(screen, 7, 5, 50, 50)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()