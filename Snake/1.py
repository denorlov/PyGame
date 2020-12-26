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

SCREEN_SIZE = WIDTH, HEIGHT = W_TILES * TILE, H_TILES * TILE

CELLS_IN_ROW_TO_WIN = 5

# world state

# list of x, y
snake = [(1, 1), (1, 2), (1, 3)]

# dx, dy
direction = (0, 1)

# list of x, y
rabbits = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(5)]
plants = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(5)]
crystals = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(5)]
rocks = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(5)]

def update():
    global snake
    global apples

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    eat = False
    for i in range(len(rabbits)):
        # eat apple
        if rabbits[i][0] == head[0] and rabbits[i][1] == head[1]:
            del rabbits[i]
            rabbits.append((randint(0, W_TILES),randint(0, H_TILES)))
            eat = True
            break

    if eat:
        snake = [head] + snake[:]
    else:
        snake = [head] + snake[:-1]

def draw(screen):
    screen.fill(BLACK_COLOR)

    for i in range(len(snake)):
        x,y = snake[i]

        pygame.draw.rect(
            screen, GREEN_COLOR,
            ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1),
            0
        )

    for i in range(len(rabbits)):
        x, y = rabbits[i]
        screen.blit(bunny_image, ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1))

    for i in range(len(plants)):
        x, y = plants[i]
        screen.blit(plant_img, ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1))

    for i in range(len(crystals)):
        x, y = crystals[i]
        screen.blit(crystal_img, ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1))

    for i in range(len(rocks)):
        x, y = rocks[i]
        screen.blit(rock_img, ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1))


    # vertical lines
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (x, 0), (x, HEIGHT))

    # horizontal lines
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (0, y), (WIDTH, y))

    # debug text
    text_surface = font.render(f"fps: {int(clock.get_fps())}, score: {len(snake)}", 1, WHITE_COLOR)
    screen.blit(text_surface, (5, 5))


pygame.init()
pygame.display.set_caption("Змея")
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)

bunny_image = pygame.image.load("bunny.png")
plant_img = pygame.image.load("plant.png")
crystal_img = pygame.image.load("crystal.png")
rock_img = pygame.image.load("rock.png")

clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)
            if event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)

    update()
    draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()