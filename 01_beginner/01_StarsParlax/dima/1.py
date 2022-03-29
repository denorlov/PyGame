import random
import pgzrun

WIDTH, HEIGHT = 1600, 900

STARS_back = []
STARS_midl = []
STARS_forward = []

for i in range(900):
    STARS_back.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT)
        ]
    )

for l in range(900):
    STARS_midl.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT)
        ]
    )

for k in range(900):
    STARS_forward.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT)
        ]
    )


def update():
    pass


def draw():
    screen.fill((20, 0, 30))

    for j in range(len(STARS_back)):
        star_back = STARS_back[j]
        x = star_back[0]
        y = star_back[1]
        if x >= WIDTH:
            x = 0
        screen.draw.filled_circle((x, y), 1, (255, 255, 255))
        STARS_back[j][0] = x + 2

    for p in range(len(STARS_midl)):
        star_midl = STARS_midl[p]
        x_m = star_midl[0]
        y_m = star_midl[1]
        if x_m >= WIDTH:
            x_m = 0
        screen.draw.filled_circle((x_m, y_m), 2, (255, 255, 255))
        STARS_midl[p][0] = x_m + 4

    for f in range(len(STARS_forward)):
        star_forwatd = STARS_forward[f]
        x_f = star_forwatd[0]
        y_f = star_forwatd[1]
        if x_f >= WIDTH:
            x_f = 0
        screen.draw.filled_circle((x_f, y_f), 3, (255, 255, 255))
        STARS_forward[f][0] = x_f + 6


pgzrun.go()