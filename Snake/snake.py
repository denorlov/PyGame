import pyanimation

from Snake.sprites.imgs import *
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

pygame.init()
pygame.display.set_caption("Змея")
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)

clock = pygame.time.Clock()

cycletime = 0
interval = .5  # how long one single images should be displayed in seconds
animation_phase_num = 0

# world state

# list of x, y
snake = [(1, 1), (1, 2), (1, 3)]

# dx, dy
direction = (0, 1)
is_in_pause = False


RABBIT_TILE = 32

class Rabbit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.animations = pyanimation.Animation("images/rabbit.png")
        self.animations.sprite_sheet.set_colorkey(pygame.color.Color("#78C380"))

        self.animations.create_animation(0, 6, RABBIT_TILE, RABBIT_TILE, "1", duration=80, cols=3, rows=1)
        self.animations.create_animation(0, 6 + RABBIT_TILE, RABBIT_TILE, RABBIT_TILE, "2", duration=80, cols=3, rows=1)
        self.animations.create_animation(0, 6 + RABBIT_TILE * 2, RABBIT_TILE, RABBIT_TILE, "3", duration=80, cols=3, rows=1)
        self.animations.create_animation(0, 6 + RABBIT_TILE * 3, RABBIT_TILE, RABBIT_TILE, "4", duration=80, cols=3, rows=1)

        self.animations.run(str(randint(1, 4)))

        self.animations.x = self.x * TILE
        self.animations.y = self.y * TILE

    def draw(self, screen):
        bunny_image = self.animations.update_surface()
        screen.blit(
            bunny_image,
            (
                self.animations.x + (TILE - RABBIT_TILE) // 2,
                self.animations.y + (TILE - RABBIT_TILE) // 2,
                RABBIT_TILE, RABBIT_TILE
            )
        )

# list of x, y
rabbits = [
    Rabbit(
        x=randint(0, W_TILES),
        y=randint(0, H_TILES)
    )
    for _ in range(15)
]

plants = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(5)]
crystals = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(5)]
rocks = [(randint(0, W_TILES), randint(0, H_TILES)) for _ in range(5)]

def update():
    global snake
    global apples

    if not is_in_pause:
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        eat = False
        for i in range(len(rabbits)):
            # eat apple
            if rabbits[i].x == head[0] and rabbits[i].y == head[1]:
                del rabbits[i]
                rabbits.append(
                    Rabbit(x=randint(0, W_TILES), y=randint(0, H_TILES))
                )
                eat = True
                break

        if eat:
            snake = [head] + snake[:]
        else:
            snake = [head] + snake[:-1]

def draw(screen):
    screen.fill(BLACK_COLOR)

    # screen.blit(snake_mid_bottom_right_img, (0, TILE, TILE, TILE))
    # screen.blit(snake_mid_bottom_left_img, (0, 2 * TILE, TILE, TILE))
    #
    # screen.blit(snake_mid_top_right_img, (0, 3 * TILE, TILE, TILE))
    # screen.blit(snake_mid_top_left_img, (0, 4 * TILE, TILE, TILE))

    for i in range(len(snake)):
        x,y = snake[i]

        if i == 0:
            # определяем направление головы
            snake_head_img = snake_head_down_img
            x1, y1 = snake[i + 1]

            if x == x1:
                if y > y1:
                    snake_head_img = snake_head_down_img
                else:
                    snake_head_img = snake_head_up_img
            else: # y == y1
                if x > x1:
                    snake_head_img = snake_head_right_img
                else:
                    snake_head_img = snake_head_left_img

            screen.blit(
                snake_head_img,
                ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1)
            )
        elif i == len(snake) - 1:
            # определяем направление хвоста
            xPrev, yPrev = snake[i - 1]

            if x == xPrev:
                if y > yPrev:
                    snake_tail_img = snake_tail_up_img
                else:
                    snake_tail_img = snake_tail_down_img
            else: # y == yPrev
                if x > xPrev:
                    snake_tail_img = snake_tail_left_img
                else:
                    snake_tail_img = snake_tail_right_img

            screen.blit(
                snake_tail_img,
                ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1)
            )

        else:
            xPrev, yPrev = snake[i - 1]
            xNext, yNext = snake[i + 1]

            if xNext == x and xPrev == x:
                snake_mid_img = snake_mid_vertical_img
            elif yPrev == y and yNext == y:
                snake_mid_img = snake_mid_horizontal_img
            else:
                if xPrev == x:
                    if yPrev > y:
                        if xNext > x:
                            snake_mid_img = snake_mid_bottom_right_img
                        else:
                            snake_mid_img = snake_mid_bottom_left_img
                    else:
                        if xNext > x:
                            snake_mid_img = snake_mid_top_right_img
                        else:
                            snake_mid_img = snake_mid_top_left_img
                else:
                    if xPrev > x:
                        if yNext > y:
                            snake_mid_img = snake_mid_bottom_right_img
                        else:
                            snake_mid_img = snake_mid_top_right_img
                    else:
                        if yNext > y:
                            snake_mid_img = snake_mid_bottom_left_img
                        else:
                            snake_mid_img = snake_mid_top_left_img

            screen.blit(
                snake_mid_img,
                ((x * TILE) + 1, (y * TILE) + 1, TILE - 1, TILE - 1)
            )

    for rabbit in rabbits:
        rabbit.draw(screen)

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

is_running = True
while is_running:
    milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0  # seconds passed since last frame (float)
    cycletime += seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = (-1, 0)
                is_in_pause = False
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)
                is_in_pause = False
            if event.key == pygame.K_UP:
                direction = (0, -1)
                is_in_pause = False
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)
                is_in_pause = False
            elif event.key == pygame.K_SPACE:
                is_in_pause = not is_in_pause

    update()

    if cycletime > interval:
        cycletime = 0

    draw(screen)
    pygame.display.flip()

pygame.quit()