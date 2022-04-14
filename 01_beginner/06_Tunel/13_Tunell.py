import math

import pygame.mouse
from pgzrun import *

WIDTH = 800
HEIGHT = 800

X0 = WIDTH // 2
Y0 = HEIGHT // 2

COUNT_CIRCLES = 5   # Всего фигур
STEP_RADIUS = 10    # Шаг увеличения размера

# список содержащий окружности, каждый элемент этого списка это также
# список чисел представляющим координаты центра и радиус:
# [X, Y, RADIUS]
circles = []

for i in range(1, COUNT_CIRCLES + 1):
    circles.append([X0, Y0, 100])

def update():
    pass

def draw():
    # # Вычисление координат X, Y для новой окружности
    # mouse_x = pygame.mouse.get_pos()[0]
    # mouse_y = pygame.mouse.get_pos()[1]
    #
    # # Добавляем новую окружность в начало списка
    # circles[0] = [mouse_x, mouse_y, 100]

    screen.fill((0, 0, 0))

    for i in range(len(circles) - 2, -1, -1):
        circle = circles[i]

        x = circle[0]
        y = circle[1]
        r = circle[2]
        rgb_color = (255, 255, 255)

        screen.draw.circle((x, y), r, rgb_color)
        screen.draw.text(f"{i}", (x + r, y))

        circle[2] = circle[2] + STEP_RADIUS
        circles[i+1] = circle

go()