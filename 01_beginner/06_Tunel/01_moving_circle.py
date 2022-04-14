import math

import pygame.mouse
from pgzrun import *

WIDTH = 800
HEIGHT = 800

X0 = WIDTH // 2
Y0 = HEIGHT // 2

def update():
    pass


def draw():
    screen.fill((0, 0, 0))

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    screen.draw.circle((mouse_x, mouse_y), 100, (0, 255, 255))
    screen.draw.text(f"{mouse_x}, {mouse_y}", (mouse_x, mouse_y))

go()