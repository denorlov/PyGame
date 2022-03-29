import random

import pgzrun

WIDTH, HEIGHT = 1080, 720

STARS = []

for i in range(10000):
    STARS.append(
        [
            random.randint(0, WIDTH), # x
            random.randint(0, HEIGHT) # y
        ]
    )

def update():
    pass

def draw():
    screen.fill((20, 0, 30))

    for j in range(len(STARS)):
        star = STARS[j]

        x = star[0]
        y = star[1]

        screen.draw.filled_circle((x, y), 2, (255, 255, 255))

        # после отрисовки точки увеличиваем x координату точки на единицу
        STARS[j][0] = x + 1

pgzrun.go()
