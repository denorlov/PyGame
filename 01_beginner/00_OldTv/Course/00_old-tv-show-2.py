import pgzrun
import random

import pygame
from pgzero.rect import Rect

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

# изменение свойств обьектов
def update():
    pass

# отрисовка объектов
def draw():
    screen.fill((0, 0, 0))
    screen.draw.text("КВАДРАТИКИ", (X0 - 150, Y0), fontsize=60)

    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = Rect(x, y, 20, 20)
    c = (255, 255, 255)
    screen.draw.filled_rect(r, c)

pgzrun.go()
