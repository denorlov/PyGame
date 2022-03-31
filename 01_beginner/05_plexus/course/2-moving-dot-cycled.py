from random import randint, uniform

import pgzrun
import pygame

from pygame.surface import Surface
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 600

VELOCITY = 0.8
POINTS = 100

points = [(randint(0, WIDTH), randint(0, HEIGHT)) for i in range(POINTS)]
VELOCITIES = [(uniform(-VELOCITY, VELOCITY), uniform(-VELOCITY, VELOCITY)) for i in range(POINTS)]

def update():
    for i in range(len(points)):
        x, y,  = points[i]
        vx, vy = VELOCITIES[i]

        x += vx
        y += vy

        if x < 0:
            x = WIDTH
        elif x > WIDTH:
            x = 0

        if y < 0:
            y = HEIGHT
        elif y > HEIGHT:
            y = 0

        points[i] = [x, y]

def draw():
    screen.fill((0, 0, 0))

    for point in points:
        x, y = point
        screen.draw.filled_circle((x, y), radius=2, color=(255, 255, 255))


pgzrun.go()