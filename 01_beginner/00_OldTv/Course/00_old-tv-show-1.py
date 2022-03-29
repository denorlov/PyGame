import pgzrun
import random

import pygame
from pgzero.rect import Rect

WIDTH = 1000
HEIGHT = 500

def update():
    pass

# отрисовка объектов
def draw():
    black_color = (0, 0, 0)
    screen.fill(black_color)
    x0 = WIDTH // 2
    y0 = HEIGHT // 2
    screen.draw.text("МИРУ МИР", (x0 - 150, y0), fontsize=60)
    r = Rect(100, 100, 200, 200)
    white_color = (255, 255, 255)
    screen.draw.filled_rect(r, white_color)

pgzrun.go()
