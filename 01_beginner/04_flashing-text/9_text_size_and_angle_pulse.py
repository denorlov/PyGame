import math
from random import randint, uniform

import pgzrun
import pygame

from pygame.surface import Surface
from pygame.math import Vector2

TITLE = "Draw text examples"

WIDTH = 1000
HEIGHT = 600

X0 = WIDTH // 2
Y0 = HEIGHT // 2

time = 0
angle = 5
size = 260

def update():
    global time, angle, size

    time = time + 1

    if time > 160:
        time = 0
        size = 260
        angle = 5

    size = size - 2

    if size < 140:
        size = 140
        angle = 0

    if angle > 0:
        angle += 6



def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"time:{time}, size:{size}, angle:{angle}", (0,0))
    screen.draw.text(
        "green зеленый grün",
        center=(X0, Y0),
        fontsize=size,
        color=(0, 255, 0),
        owidth=0.4, ocolor=(0,200,0),
        angle=angle,
        width=360
    )

pgzrun.go()