import math

import pygame.mouse
from pgzrun import *

WIDTH = 800
HEIGHT = 800

X0 = WIDTH // 2
Y0 = HEIGHT // 2

COUNT_CIRCLES = 3   # Всего фигур
STEP_RADIUS = 30    # Шаг увеличения размера

# список содержащий окружности, каждый элемент этого списка это также
# список чисел представляющим координаты центра и радиус:
# [X, Y, RADIUS]
сircles = []

for i in range(1, COUNT_CIRCLES + 1):
    сircles.append([X0, Y0, 100 + i * STEP_RADIUS])

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    for i in range(len(сircles)):
        circle = сircles[i]

        x = circle[0]
        y = circle[1]
        r = circle[2]
        rgb_color = (255, 255, 255)

        screen.draw.circle((x, y), r, rgb_color)
        screen.draw.text(f"{i}", (x + r, y))

        circle[2] = circle[2] + STEP_RADIUS
        if circle[2] > WIDTH:
            circle[2] = 100

go()