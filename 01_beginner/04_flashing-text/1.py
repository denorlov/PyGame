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
    screen.draw.text("Привет Мир!", (X0, Y0))

pgzrun.go()