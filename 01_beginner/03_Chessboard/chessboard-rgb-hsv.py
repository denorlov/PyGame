# 1. Цвета в pygame и pygame zero,
# 2. HSV и HSL представление цвета: https://en.wikipedia.org/wiki/HSL_and_HSV

import pgzrun
import pygame
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 800

X0 = WIDTH // 2
Y0 = HEIGHT // 2

BLACK = (0, 0, 0)
WHITE = pygame.color.Color('white')
DARK_GREEN = pygame.color.Color('#008000')
GREEN = pygame.Color(50, 150, 50)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

# цвета которые будут использоваться для отрисовки доски
color1 = BLUE
color2 = pygame.Color(0, 0, 0, 0)
color2.hsla = (color1.hsla[0], color1.hsla[1], color1.hsla[2] - 30, color1.hsla[3])

SIDE = 100


def update():
    pass

def draw():
    screen.fill(BLACK)

    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                color = color2
            else:
                color = color1

            screen.draw.filled_rect(Rect(i * SIDE + 2, j * SIDE + 2, SIDE - 4, SIDE - 4), color)
            #screen.draw.text(f"i,j={i},{j}", (i * SIDE, j * SIDE))

pgzrun.go()