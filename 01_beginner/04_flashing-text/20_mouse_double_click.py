import math
from random import randint, uniform

import pgzrun
import pygame

from pygame.surface import Surface
from pygame.math import Vector2
import os

TITLE = "Старый престарый телевизор"

WIDTH = 1000
HEIGHT = 600

X0 = WIDTH // 2
Y0 = HEIGHT // 2

colors = [(0, 100, 0), (100, 0, 0), (0, 0, 100), (100, 100, 0), (0, 100, 100), (100, 0, 100)]
ocolors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
texts = ["green зеленый grün", "красный red rot", "синий blue blau", "желтый yellow ", "циановый cyan cyan", "фиолетовый violet violett"]

round_time_limit = 200
time = 0
size = 260
rotation_direction = randint(-1, 1)
angle = 5 * rotation_direction

color_indx = randint(0, len(colors)) - 1
text_indx = randint(0, len(texts)) - 1

clicked_button = None
prev_button = None

score = 0

def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

def update():
    global time, angle, size, color_indx, text_indx
    global rotation_direction, clicked_button, prev_button, score

    time = time + 1

    # конец раунда по времени
    if time > round_time_limit:
        time = 0
        size = 260
        rotation_direction = randint(-1, 1)
        angle = 5 * rotation_direction
        color_indx = randint(0, len(colors)-1)
        if randint(0, 1):
            text_indx = randint(0, len(texts)-1)
        else:
            text_indx = color_indx

        if prev_button == None or prev_button != clicked_button:
            score -= 5

        clicked_button = None
        prev_button = None

    # меням размер и расположение надписи со временем
    size = size - 2

    if size < 140:
        size = 140
        angle = 0

    if angle != 0:
        angle = angle + 6 * rotation_direction

def on_mouse_down(pos, button):
    global score, clicked_button, prev_button, round_time_limit

    print(f"btn: {clicked_button}, prev btn: {prev_button}")
    print(f"txt_idx={text_indx}, color_idx={color_indx}")

    if mouse.LEFT == button or mouse.RIGHT == button:
        prev_button = clicked_button
        clicked_button = button

        if prev_button == clicked_button:
            if mouse.LEFT == clicked_button:
                print("Left button clicked!")

                if color_indx == text_indx:
                    print("They matches, score increase")
                    score += 5
                    round_time_limit -= 2
                else:
                    print("They don't, score decrease")
                    score -= 5

            elif mouse.RIGHT == clicked_button:
                print("Right button clicked!")

                if color_indx == text_indx:
                    print("They matches, score decrease")
                    score -= 5
                else:
                    print("They don't, score increase")
                    score += 5
                    round_time_limit -= 2


def draw():
    screen.fill((0, 0, 0))

    if score < 25:
        alpha = 1
        if score > 5:
            alpha = 0.5
        elif score > 15:
            alpha = 0.6
        elif score > 20:
            alpha = 0.8

        screen.draw.text(f"левая кнопка мыши, если цвета совпадают\nправая кнопка мыши, если не совпадают", fontsize=30, midtop=(WIDTH//2, 5), alpha=alpha)

    screen.draw.text("✌", (5, HEIGHT - 69), fontname="notoemoji-661a", fontsize=50)
    screen.draw.text(f"{score}", (67, HEIGHT - 65), fontsize=100)

    time_rest = (round_time_limit - time) // 5

    clock_sym = "⏳"
    if time_rest < 30:
        clock_sym = "⌛"

    if time_rest > 20:
        screen.draw.text(clock_sym, (WIDTH - 180, HEIGHT - 67), fontname="notoemoji-661a", fontsize=50)
    elif (time_rest // 6) % 2:
        screen.draw.text(clock_sym, (WIDTH - 180, HEIGHT - 67), fontname="notoemoji-661a", fontsize=50)

    screen.draw.text(f"{time_rest:{2}}", (WIDTH - 110, HEIGHT - 65), fontsize=100)

    screen.draw.text(
        texts[text_indx],
        center=(X0, Y0),
        fontsize=size,
        color=colors[color_indx],
        owidth=0.4, ocolor=ocolors[color_indx],
        angle=angle,
        width=360
    )

    mouse_pos = pygame.mouse.get_pos()

    if clicked_button == prev_button:
        if (clicked_button == mouse.LEFT and text_indx != color_indx) or\
                (clicked_button == mouse.RIGHT and text_indx == color_indx):
            print(f"btn: {clicked_button}, txt_idx={text_indx}, color_idx={color_indx}")
            screen.draw.text("x", center=mouse_pos, fontsize=420, fontname="mysoul-regular", color="red", owidth=0.2, ocolor=(200, 0, 0))
        elif (clicked_button == mouse.LEFT and text_indx == color_indx) or\
                (clicked_button == mouse.RIGHT and text_indx != color_indx):
            print(f"btn: {clicked_button}, txt_idx={text_indx}, color_idx={color_indx}")
            screen.draw.text("√", center=mouse_pos, fontsize=420, color="green", owidth=0.2, ocolor=(0, 200, 0))
    elif clicked_button:
        print(f"btn: {clicked_button}, txt_idx={text_indx}, color_idx={color_indx}")
        if clicked_button == mouse.LEFT:
            screen.draw.text("совпадают? второй клик!", midtop=(WIDTH//2, HEIGHT-45), fontsize=30, color="green")
        else:
            screen.draw.text("разные? второй клик!", midtop=(WIDTH//2, HEIGHT-45), fontsize=30, color="red")




pygame.mouse.set_visible(False)
pgzrun.go()