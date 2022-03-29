import random

import pgzrun

WIDTH, HEIGHT = 1080, 720

X0 = WIDTH // 2
Y0 = HEIGHT // 2

STARS = []

for i in range(10000):
    STARS.append(
        (
            # x, y
            random.randint(0 - WIDTH + 1, WIDTH - 1),
            random.randint(0 - HEIGHT - 1, HEIGHT + 1),
            # light
            random.randint(1, 255)
         )
    )

print(STARS)

def update():
    pass

def draw():
    screen.fill((20, 0, 30))
    for star in STARS:
        star_light = star[2]
        if star_light != 0:
            rgb = (star_light, star_light, star_light)
            x = X0 + star[1]
            y = Y0 + star[0]
            screen.draw.filled_circle(pos=(x, y), radius=2, color=rgb)

pgzrun.go()
