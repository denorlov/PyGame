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

bunnies = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(10)]
plants = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(10)]
ice = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(10)]
rock = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(10)]

def draw(screen):
    screen.fill(BLACK_COLOR)

    # screen.blit(snake_tail_up, (64, 0))
    # screen.blit(snake_tail_down, (64*2, 0))
    # screen.blit(snake_tail_right, (64*3, 0))
    # screen.blit(snake_tail_left, (64*4, 0))

    for n, cell in enumerate(snake):
        x_cells, y_cells = cell
        x_screen = (x_cells) * TILE
        y_screen = (y_cells) * TILE

        if n == 0:
            x_cells_next, y_cells_next = snake[1]
            if y_cells == y_cells_next:
                if x_cells > x_cells_next:
                    snake_head_img = snake_head_right
                else:
                    snake_head_img = snake_head_left
            else: # x == x_next
                if y_cells > y_cells_next:
                    snake_head_img = snake_head_down
                else:
                    snake_head_img = snake_head_up

            screen.blit(snake_head_img, (x_screen, y_screen, TILE, TILE))

        elif n == len(snake) - 1:
            x_cells_prev, y_cells_prev = snake[-2]

            if y_cells == y_cells_prev:
                if x_cells > x_cells_prev:
                    snake_tail_img = snake_tail_right
                else:
                    snake_tail_img = snake_tail_left
            else: # x == x_next
                if y_cells > y_cells_prev:
                    snake_tail_img = snake_tail_down
                else:
                    snake_tail_img = snake_tail_up

            screen.blit(snake_tail_img, (x_screen, y_screen, TILE, TILE))

        else:
            pygame.draw.rect(
                screen, GREEN_COLOR,
                (x_screen, y_screen, TILE, TILE)
            )

    for x_cells, y_cells in bunnies:
        x_screen = (x_cells) * TILE
        y_screen = (y_cells) * TILE

        screen.blit(bunny_image, (x_screen, y_screen, TILE, TILE))

    for x_cells, y_cells in plants:
        x_screen = (x_cells) * TILE
        y_screen = (y_cells) * TILE

        screen.blit(plant_image, (x_screen, y_screen, TILE, TILE))

    for x_cells, y_cells in ice:
        screen.blit(ice_image, (x_cells * TILE, y_cells * TILE, TILE, TILE))

    for x_cells, y_cells in rock:
        screen.blit(rock_image, (x_cells * TILE, y_cells * TILE, TILE, TILE))


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
plant_image = pygame.image.load("plant.png")
ice_image = pygame.image.load("crystal.png")
rock_image = pygame.image.load("rock.png")

snake_grapichs = pygame.image.load("snake-graphics.png")

snake_head_up = snake_grapichs.subsurface((64 * 3, 0, 64, 64))
snake_head_up = pygame.transform.scale(snake_head_up, (TILE, TILE))

snake_head_down = snake_grapichs.subsurface((64 * 4, 64, 64, 64))
snake_head_down = pygame.transform.scale(snake_head_down, (TILE, TILE))

snake_head_right = snake_grapichs.subsurface((64 * 4, 0, 64, 64))
snake_head_right = pygame.transform.scale(snake_head_right, (TILE, TILE))

snake_head_left = snake_grapichs.subsurface((64 * 3, 64, 64, 64))
snake_head_left = pygame.transform.scale(snake_head_left, (TILE, TILE))


snake_tail_up = snake_grapichs.subsurface((64 * 4, 64 * 3, 64, 64))
snake_tail_up = pygame.transform.scale(snake_tail_up, (TILE, TILE))

snake_tail_down = snake_grapichs.subsurface((64 * 3, 64 * 2, 64, 64))
snake_tail_down = pygame.transform.scale(snake_tail_down, (TILE, TILE))

snake_tail_right = snake_grapichs.subsurface((64 * 3, 64 * 3, 64, 64))
snake_tail_right = pygame.transform.scale(snake_tail_right, (TILE, TILE))

snake_tail_left = snake_grapichs.subsurface((64 * 4, 64 * 2, 64, 64))
snake_tail_left = pygame.transform.scale(snake_tail_left, (TILE, TILE))

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