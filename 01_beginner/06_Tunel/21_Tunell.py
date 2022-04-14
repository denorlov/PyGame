import math

import pygame.mouse
from pgzrun import *

WIDTH = 800
HEIGHT = 800

X0 = WIDTH // 2
Y0 = HEIGHT // 2

COUNT_CIRCLES = 100                      # Всего фигур
STEP_RADIUS = 10                         # Шаг увеличения размера
STEP_COLOR = (255-50) / COUNT_CIRCLES    # Шаг увеличения яркости

# список содержащий эллипсы, каждый элемент этого списка это также
# список чисел представляющим координаты центра, радиус и оттенок:
# [X, Y, RADIUS, COLOR]
сircles = []

for i in range(0, COUNT_CIRCLES):
    сircles.append([X0, Y0, 100, 50])

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    for i in range(len(сircles) - 2, -1, -1):
        circle = сircles[i]

        circle[2] = circle[2] + STEP_RADIUS
        circle[3] = circle[3] + STEP_COLOR

        сircles[i + 1] = circle

        circle_x = circle[0]
        circle_y = circle[1]
        circle_r = circle[2]
        circle_color = circle[3]
        screen.draw.circle((circle_x, circle_y), circle_r, (0, circle_color, circle_color))

    # Вычисление координат X, Y для новой окружности
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    # Добавляем новую окружность в начало списка
    сircles[0] = [mouse_x, mouse_y, 100, 50]

go()