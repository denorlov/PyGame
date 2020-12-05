from copy import deepcopy
from random import randint

import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

FPS = 30

TILE = 10
WIDTH, HEIGHT = 150, 50

cells_next = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

#cells = [[randint(0, 1) for _ in range(WIDTH)] for _ in range(HEIGHT)]
cells = [[0 if x % 33 else 1 for x in range(WIDTH)] for y in range(HEIGHT)]
#cells = [[1 for i in range(WIDTH)] for j in range(HEIGHT)]

next_turn = False
play_mode = False

def calc_cell_state(cells, x, y):
    count = 0
    # x = 1, y = 1
    for i in range(x - 1, x + 2): # 0, 1, 2
        for j in range(y - 1, y + 2): # 0, 1, 2
            if cells[j][i]:
                count += 1

    # if alive
    if cells[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    # if dead
    else:
        if count == 3:
            return 1
        return 0

def update():
    global cells_next, cells, next_turn

    if next_turn or play_mode:
        for x in range(1, WIDTH - 1):
            for y in range(1, HEIGHT - 1):
                cells_next[y][x] = calc_cell_state(cells, x, y)

        cells = deepcopy(cells_next)

        next_turn = False

def draw(screen):
    screen.fill(BLACK_COLOR)

    #cells
    for x_cell in range(WIDTH):
        for y_cell in range(HEIGHT):
            if cells[y_cell][x_cell]:
                pygame.draw.rect(
                    screen, GREEN_COLOR,
                    ((x_cell * TILE) + 1, (y_cell * TILE) + 1, TILE - 2, TILE - 2)
                )

    #draw vertical lines
    for x in range(0, WIDTH * TILE, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (x, 0), (x, HEIGHT * TILE))

    #horizontal lines
    for y in range(0, HEIGHT * TILE, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (0, y), (WIDTH * TILE, y))

    # debug text
    text_surface = font.render(f"next_turn: {next_turn}, mouse: {mouse_x}, {mouse_y}", 1, WHITE_COLOR)
    screen.blit(text_surface, (5, 5))


pygame.init()
screen = pygame.display.set_mode((WIDTH * TILE, HEIGHT * TILE))
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
        elif event.type == pygame.MOUSEBUTTONUP:
            next_turn = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_mode = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                play_mode = False


    draw(screen)
    pygame.display.flip()
    update()

    clock.tick(FPS)

pygame.quit()