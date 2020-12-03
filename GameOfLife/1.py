import time
from copy import deepcopy
from random import randint

import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')

FPS = 30

TILE = 10
W_TILES, H_TILES = 200, 150

SCREEN_SIZE = WIDTH, HEIGHT = W_TILES * TILE, H_TILES * TILE

# world state
#cells = [[randint(0, 1) for i in range(WIDTH // TILE)] for j in range(H_TILES)]
#cells = [[0 if i % 5 else 1 for i in range(WIDTH // TILE)] for j in range(H_TILES)]
cells = [[1 if i == WIDTH / TILE // 2 else 0 for i in range(WIDTH // TILE)] for j in range(H_TILES)]
next_cells = [[0 for _ in range(WIDTH // TILE)] for _ in range(H_TILES)]

# control flags
next_turn = False
dont_wait_key_to_draw = False

def check_cell(cells, x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if cells[j][i]:
                count += 1

    # if alive
    if cells[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    # is dead
    else:
        if count == 3:
            return 1
        return 0


def update():
    global cells, next_turn

    if next_turn or dont_wait_key_to_draw:
        for x in range(1, W_TILES - 1):
            for y in range(1, H_TILES - 1):
                next_cells[y][x] = check_cell(cells, x, y)

        cells = deepcopy(next_cells)

        next_turn = False


def draw(screen):
    screen.fill(BLACK_COLOR)

    # cells
    for x in range(0, W_TILES):
        for y in range(0, H_TILES):
            if cells[y][x]:
                pygame.draw.rect(
                    screen, GREEN_COLOR,
                    ((x * TILE) + 2, (y * TILE) + 2, TILE - 2, TILE - 2),
                    0
                )

    # vertical lines
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (x, 0), (x, HEIGHT))

    # horizontal lines
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (0, y), (WIDTH, y))

    # debug text
    text_surface = font.render(f"fps: {int(clock.get_fps())}", 1, WHITE_COLOR)
    screen.blit(text_surface, (5, 5))



pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)
clock = pygame.time.Clock()

event = pygame.event.wait()
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            next_turn = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dont_wait_key_to_draw = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                dont_wait_key_to_draw = False


    draw(screen)
    pygame.display.flip()
    update()

    clock.tick(FPS)

pygame.quit()