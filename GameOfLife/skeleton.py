import time

import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

FPS = 30

def update():
    pass

def draw(screen):
    screen.fill(BLACK_COLOR)

    #...

    # debug text
    text_surface = font.render(f"fps: {int(clock.get_fps())}, mouse: {mouse_x}, {mouse_y}", 1, WHITE_COLOR)
    screen.blit(text_surface, (5, 5))


pygame.init()
screen = pygame.display.set_mode((1200, 800))
font = Font(None, 24)
clock = pygame.time.Clock()
mouse_x, mouse_y = 0, 0

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

    draw(screen)
    pygame.display.flip()
    update()

    clock.tick(FPS)

pygame.quit()