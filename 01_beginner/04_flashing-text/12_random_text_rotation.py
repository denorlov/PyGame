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

colors = [(0, 100, 0), (100, 0, 0), (0, 0, 100), (100, 100, 0), (0, 100, 100), (100, 0, 100)]
ocolors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
texts = ["green зеленый grün", "красный red rot", "синий blue blau", "желтый yellow ", "голубой blue blau", "фиолетовый violet violett"]

time = 0
size = 260
rotation_direction = randint(-1, 1)
angle = 5 * rotation_direction

color_indx = randint(0, len(colors)) - 1
text_indx = randint(0, len(texts)) - 1

def update():
    global time, angle, size, color_indx, text_indx, rotation_direction

    time = time + 1

    if time > 140:
        time = 0
        size = 260
        rotation_direction = randint(-1, 1)
        angle = 5 * rotation_direction
        color_indx = randint(0, len(colors)-1)
        text_indx = randint(0, len(texts)-1)

    size = size - 2

    if size < 140:
        size = 140
        angle = 0

    if angle != 0:
        angle = angle + 6 * rotation_direction



def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"time:{time}, size:{size}, angle:{angle}, rotation:{rotation_direction}", (0,0))
    screen.draw.text(
        texts[text_indx],
        center=(X0, Y0),
        fontsize=size,
        color=colors[color_indx],
        owidth=0.4, ocolor=ocolors[color_indx],
        angle=angle,
        width=360
    )

pgzrun.go()