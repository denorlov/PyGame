from pgzrun import *
from math import *

TITLE = "Sun System"

WIDTH = 1600 // 2
HEIGHT = 900 // 2

CX = WIDTH // 2
CY = HEIGHT // 2

BLACK = 0, 0, 0
GREY = 100, 100, 100
WHITE = 255, 255, 255

SUN = 240, 140, 30

MERCURY = 100, 100, 100
VENUS = 200, 170, 150
EARTH = 150, 255, 150
MARS = 150, 50, 50
JUPITER = 100, 25, 0
SATURN = 200, 170, 150
URANUS = 150, 150, 230
NEPTUNE = 120, 70, 240
PLUTO = 150, 50, 50

SPEED = 1

K = 0.98630136986

R = 57.2957795131

FPS = 30

SHOWDAYS = True
SHOWSPEED = True

SHOWPLANETNAMES = True
SHOWPLANETSTRAJECTORIES = True

global current_day_mercury
global current_day_venus
global current_day_earth
global current_day_mars
global current_day_jupiter
global current_day_saturn
global current_day_uranus
global current_day_neptune
global current_day_pluto

current_day_mercury = 0
current_day_venus = 0
current_day_earth = 0
current_day_mars = 0
current_day_jupiter = 0
current_day_saturn = 0
current_day_uranus = 0
current_day_neptune = 0
current_day_pluto = 0

def update():
    pass

def draw_planet(day, distance, radius, name, color):
    angle = (day * K) / R
    x = sin(angle) * distance
    y = cos(angle) * distance

    screen.draw.filled_circle((CX - x, CY - y), radius, color)
    if (SHOWPLANETNAMES):
        screen.draw.text(name, (CX - x, CY - y + radius + 5), fontsize=15, owidth=1, ocolor=BLACK, color=WHITE)

def draw():

    global current_day_mercury
    global current_day_venus
    global current_day_earth
    global current_day_mars
    global current_day_jupiter
    global current_day_saturn
    global current_day_uranus
    global current_day_neptune
    global current_day_pluto

    current_day_mercury += FPS * SPEED / 8.797
    current_day_venus   += FPS * SPEED / 22.47
    current_day_earth   += FPS * SPEED / 35.6       # INGAME DAYS ON EARTH IN 1 REAL SECOND
    current_day_mars    += FPS * SPEED / 68.62
    current_day_jupiter += FPS * SPEED / 432.89
    current_day_saturn  += FPS * SPEED / 1075.29
    current_day_uranus  += FPS * SPEED / 3066.365
    current_day_neptune += FPS * SPEED / 6014.835
    current_day_pluto   += FPS * SPEED / 9073.535

    screen.fill(BLACK)

    screen.draw.filled_circle((CX, CY), 50, SUN)
    screen.draw.text("Sun", (CX - 12, CY), fontsize=20, owidth=1, ocolor=BLACK, color=WHITE)

    x = 75

    if (SHOWPLANETSTRAJECTORIES):
        for i in range(9):
            screen.draw.circle((CX, CY), x, GREY)
            x += 25

    draw_planet(current_day_mercury, 75, 2, "Mercury", MERCURY)
    draw_planet(current_day_venus,   100, 2, "Venus",   VENUS)
    draw_planet(current_day_earth,   125, 2, "Earth",   EARTH)
    draw_planet(current_day_mars,    150, 2, "Mars",    MARS)
    draw_planet(current_day_jupiter, 175, 2, "Jupiter", JUPITER)
    draw_planet(current_day_saturn,  200, 2, "Saturn",  SATURN)
    draw_planet(current_day_uranus,  225, 2, "Uranus",  URANUS)
    draw_planet(current_day_neptune, 250, 2, "Neptune", NEPTUNE)
    draw_planet(current_day_pluto,   275, 2, "Pluto",   PLUTO)

    if (SHOWDAYS):
        screen.draw.text("Day=" + str(trunc(current_day_earth)) + " (Earth time)", (0, 0), fontsize=20, owidth=1, ocolor=BLACK, color=WHITE)
    if (SHOWSPEED):
        screen.draw.text("Speed=" + str(SPEED) + "x", (0, 15), fontsize=20, owidth=1, ocolor=BLACK, color=WHITE)

go()