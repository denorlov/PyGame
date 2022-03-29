import random

import pgzrun

WIDTH, HEIGHT = 1080, 720

X0 = WIDTH // 2
Y0 = HEIGHT // 2

STARS = []
MEDIUM_STARS = []
BIG_STARS = []

STARS = [
    (
        # x, y
        random.randint(0 - WIDTH + 1, WIDTH - 1),
        random.randint(0 - HEIGHT - 1, HEIGHT + 1),
        # light
        random.randint(125, 200)
     )
    for i in range(800)
]

MEDIUM_STARS = [
    (
        # x, y
        random.randint(0 - WIDTH + 1, WIDTH - 1),
        random.randint(0 - HEIGHT - 1, HEIGHT + 1),
        # light
        random.randint(200, 220)
     )
    for i in range(300)
]

BIG_STARS = [
    (
        # x, y
        random.randint(0 - WIDTH + 1, WIDTH - 1),
        random.randint(0 - HEIGHT - 1, HEIGHT + 1),
        # light
        random.randint(220, 255)
     )
    for i in range(200)
]


ticks = 0

def update():
    global ticks
    ticks += 1

def draw():
    screen.fill((20, 0, 30))

    for star in STARS:
        star_light = star[2]
        if star_light != 0:
            rgb = (star_light, star_light, star_light)
            x = X0 + star[1] + ticks * 2
            y = Y0 + star[0]
            screen.draw.filled_circle(pos=(x % WIDTH, y), radius=2, color=rgb)

    for star in MEDIUM_STARS:
        star_light = star[2]
        if star_light != 0:
            rgb = (star_light, star_light, star_light)
            x = X0 + star[1] + ticks * 1.5
            y = Y0 + star[0]
            screen.draw.filled_circle(pos=(x % WIDTH, y), radius=4, color=rgb)

    for star in BIG_STARS:
        star_light = star[2]
        if star_light != 0:
            rgb = (star_light, star_light, star_light)
            x = X0 + star[1] + ticks
            y = Y0 + star[0]
            screen.draw.filled_circle(pos=(x % WIDTH, y), radius=8, color=rgb)

pgzrun.go()
