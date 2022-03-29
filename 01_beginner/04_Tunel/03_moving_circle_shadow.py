import math

import pygame.mouse
from pgzrun import *

WIDTH = 800
HEIGHT = 800

X0 = WIDTH // 2
Y0 = HEIGHT // 2

def update():
    pass

circles = []
CIRCLES_COUNT = 20

def draw():
    screen.fill((0, 0, 0))

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    circles.append([mouse_x, mouse_y])

    i = 0
    for circle in circles:
        circle_x = circle[0]
        circle_y = circle[1]
        color_intensity = int(255 * i / CIRCLES_COUNT)
        screen.draw.circle((circle_x, circle_y), 100, (0, color_intensity, color_intensity))
        i = i + 1

    if len(circles) > CIRCLES_COUNT:
        del circles[0]

go()