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

t = 0

def draw():
    global t
    t = t + 1

    screen.fill((0, 0, 0))
    screen.draw.text(f"time: {t}, fontsize={int(128 * math.sin(t / 20))}", (0, 0))

    offset = 100 * math.sin(t / 10)
    screen.draw.text(
        "Привет Мир!",
        center=(X0-offset, Y0+offset),
        owidth=1.5, ocolor=(0,0,255),
        color="green",
        fontsize=128 * math.sin(t / 20),
        shadow=(1, 1),
        scolor=(60, 60, 60)
    )
    #screen.draw.text("Миру мир!", (X0, Y0), fontsize=abs(60*math.cos(t/200))+18)
    # offset = 100 * abs(60 * math.cos(t / 20) + math.cos(t / 2)) // t
    # screen.draw.text(
    #     "Red Красный Rojo Rot",
    #     center=(X0, Y0 + offset),
    #     # angle=180 * math.cos(t / 10),
    #     width=360,
    #     fontsize=148,
    #     # color="#AAFF00",
    #     # gcolor="#66AA00"
    #     color="red",
    #     scolor="#202020",
    #     # owidth=1.5,
    #     # ocolor="#66AA00",
    #     # alpha=0.8
    # )

pgzrun.go()