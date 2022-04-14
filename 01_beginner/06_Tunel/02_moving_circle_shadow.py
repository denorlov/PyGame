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

def draw():
    screen.fill((0, 0, 0))

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    circles.append([mouse_x, mouse_y])

    i = 0
    for circle in circles:
        circle_x = circle[0]
        circle_y = circle[1]
        screen.draw.circle((circle_x, circle_y), 100, (0, 255, 255))
        screen.draw.text(f"{i}", (circle_x + 100, circle_y))
        i += 1

go()