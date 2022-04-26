from this import d
from pgzrun import *
from random import *
from math import *

TITLE = "Old TV"

WIDTH = 1600
HEIGHT = 900

CX = WIDTH // 2
CY = HEIGHT // 2


DEBUG = False # Debug mode


COLORS = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]

COLORS_NAMES = ["BLACK", "WHITE", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PURPLE"]

global color_right, color_left, flag_player, flag_real, index_color, index_name, select, score

score = 0

select = False

flag_real = True
flag_player = True

index_color = False
index_name = False

color_right = COLORS[2]
color_left = COLORS[2]

score = -5

def a():
    a = 1

def on_key_down(key):
    global color_right, color_left

    if (key == keys.LEFT):
        color_left = COLORS[3]
        color_right = COLORS[2]
    elif (key == keys.RIGHT):
        color_left = COLORS[2]
        color_right = COLORS[3]

def on_key_up(key):
    global color_right, color_left, flag_player, select, score

    if (key == keys.LEFT):
        flag_player = False
        select = False
        music.play_once("misfires hitsound.wav")
    elif (key == keys.RIGHT):
        flag_player = True
        select = False
        music.play_once("misfires hitsound.wav")
    else:
        select = True
    
    color_right = COLORS[2]
    color_left = COLORS[2]
    

def update():
    pass

def draw():
    global color_right, color_left, flag_player, flag_real, index_color, index_name, select, score

    screen.clear()
    screen.fill(COLORS[1])

    if not (select):
        index_color = randint(0, 7)

        concurrence = randint(0, 1)

        if (concurrence == 0):
            index_color = randint(0, 7)
            index_name = index_color
        else:
            while True:
                index_color = randint(0, 7)
                index_name = randint(0, 7)
                if (index_color != index_name):
                    break
        

        if (flag_real == flag_player):
            score += 5
        else:
            score -= 5

        select = True

    if (index_color == index_name):
        flag_real = True
    else:
        flag_real = False

    if (DEBUG):
        screen.draw.text("flag_player=" + str(flag_player), (0, 0), owidth=0.5, ocolor=COLORS[0], color=COLORS[1])
        screen.draw.text("flag_real="   + str(flag_real),   (0, 20), owidth=0.5, ocolor=COLORS[0], color=COLORS[1])
        screen.draw.text("index_color=" + str(index_color),   (0, 40), owidth=0.5, ocolor=COLORS[0], color=COLORS[1])
        screen.draw.text("index_name="  + str(index_name),   (0, 60), owidth=0.5, ocolor=COLORS[0], color=COLORS[1])
        screen.draw.text("select="      + str(select),      (0, 80), owidth=0.5, ocolor=COLORS[0], color=COLORS[1])

    screen.draw.text(COLORS_NAMES[index_name], centerx=CX, centery=CY, owidth=0.5, ocolor=COLORS[0], color=COLORS[index_color], fontsize=100)

    screen.draw.filled_circle((CX + 150, CY + 150), 30, color_right)
    screen.draw.text(">", centerx=CX + 150, centery=CY + 150, owidth=1, ocolor=COLORS[0], color=COLORS[1], fontsize=50)
    screen.draw.text("RIGHT arrow\n(if the name MATCHES the color)", centerx=CX + 150, centery=CY + 200, owidth=0.5, ocolor=COLORS[0], color=COLORS[1])

    screen.draw.filled_circle((CX - 150, CY + 150), 30, color_left)
    screen.draw.text("<", centerx=CX - 150, centery=CY + 150, owidth=1, ocolor=COLORS[0], color=COLORS[1], fontsize=50)
    screen.draw.text("LEFT arrow\n(if the name NOT MATCHES the color)", centerx=CX - 150, centery=CY + 200, owidth=0.5, ocolor=COLORS[0], color=COLORS[1])

    screen.draw.text("Score: " + str(score), centerx=CX, centery=CY + 150, owidth=1, ocolor=COLORS[0], color=COLORS[1])

go()