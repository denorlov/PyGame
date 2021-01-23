from random import randint

import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

FPS = 7

TILE = 50
W_TILES, H_TILES = 25, 15

SCREEN_SIZE = (WIDTH, HEIGHT) = (W_TILES * TILE, H_TILES * TILE)

# world state
snake = [(5,5), (5,6), (5,7)]
direction = (0, 1)

apples = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(10)]

def draw(screen):
    screen.fill(BLACK_COLOR)

    for x_cells, y_cells in snake:
        x_screen = (x_cells) * TILE
        y_screen = (y_cells) * TILE

        pygame.draw.rect(
            screen, GREEN_COLOR,
            (x_screen, y_screen, TILE, TILE)
        )

    for x_cells, y_cells in apples:
        x_screen = (x_cells) * TILE
        y_screen = (y_cells) * TILE

        pygame.draw.rect(
            screen, RED_COLOR,
            (x_screen, y_screen, TILE, TILE)
        )

    screen.blit(
        bunny_image,
        (100, 100, TILE, TILE)
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
pygame.display.set_caption("Змея")
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)
bunny_image = pygame.image.load("bunny.png")

clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = (0, -1)
            if event.key == pygame.K_DOWN:
                direction = (0, 1)
            if event.key == pygame.K_LEFT:
                direction = (-1, 0)
            if event.key == pygame.K_RIGHT:
                direction = (1, 0)


    # [(5, 5), (5, 6), (5, 7)]
    head = snake[0]
    head1 = (head[0] + direction[0], head[1] + direction[1])
    # head1 = (5+1, 5+0)
    snake = [head1] + snake[:-1]
    # [(6, 5), (5, 5), (5, 6)]

    draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()