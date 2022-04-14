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
    сircles.append([WIDTH // 2, HEIGHT // 2, 100, 50])

def draw_circle(circle):
    angle = 0                   # Угол перемещения по эллипсу, для отрисовки очередной точки.
    step = math.pi * 2 / 100    # Шаг, с которым рисуются точки эллипса.

    circle_x = circle[0]
    circle_y = circle[1]
    circle_r = circle[2]
    circle_color = circle[3]

    while angle < math.pi * 2:
        x = round(circle_x + math.sin(angle) * circle_r)
        y = round(circle_y + math.cos(angle) * circle_r // 1.5)

        if 0 < x < WIDTH and 0 < y < HEIGHT:
            screen.draw.filled_circle((x, y), 2, (0, circle_color, circle_color))

        angle += step

def update():
    pass

rotation_angle = 0

def draw():
    global rotation_angle

    screen.fill((0, 0, 0))

    for i in range(len(сircles) - 2, -1, -1):
        circle = сircles[i]

        circle[2] += STEP_RADIUS
        circle[3] += STEP_COLOR
        сircles[i + 1] = circle

        draw_circle(circle)

    # Вычисление координат X, Y для новой окружности
    rotation_angle += 0.05
    x = X0 + math.sin(rotation_angle) * 50.0
    y = Y0 + math.cos(rotation_angle) * 50.0

    # Добавляем новую окружность в начало списка
    сircles[0] = [x, y, 100, 50]

go()