import math
from random import randint, uniform

import pgzrun
import pygame

from pygame.surface import Surface
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 600

X0 = WIDTH // 2
Y0 = HEIGHT // 2

def update():
    pass

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(
        "Привет Мир!",
        center=(X0, Y0),
        color=(0, 255, 0),
        fontsize=128,
        shadow=(.5, .5),
        scolor=(0, 100, 0)
    )

pgzrun.go()