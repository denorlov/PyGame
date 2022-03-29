import random
import pgzrun

WIDTH, HEIGHT = 1920, 1080

STARS1 = []
STARS2 = []
STARS3 = []
for i in range(200):
    STARS1.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT)
        ]
    )
for i in range(100):
    STARS2.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT)
        ]
    )

for i in range(50):
    STARS3.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT)
        ]
    )


def update():
    pass


def draw():
    screen.fill((0, 0, 0))
    # ПЕРВЫЙ СЛОЙ
    for j in range(len(STARS1)):
        star = STARS1[j]

        x = star[0]
        y = star[1]

        screen.draw.filled_circle((x, y), 2, (130, 130, 130))

        STARS1[j][0] = x + 0.75
        if x >= 1920:
            x = 0
            STARS1[j][0] = x
    # ВТОРОЙ СЛОЙ
    for j in range(len(STARS2)):
        star = STARS2[j]

        x = star[0]
        y = star[1]

        screen.draw.filled_circle((x, y), 4, (200, 200, 200))
        STARS2[j][0] = x + 1
        if x >= 1920:
            x = 0
            STARS2[j][0] = x
    # ТРЕТИЙ СЛОЙ
    for j in range(len(STARS3)):
        star = STARS3[j]

        x = star[0]
        y = star[1]

        screen.draw.filled_circle((x, y), 6, (255, 255, 255))

        STARS3[j][0] = x + 1.5
        if x >= 1920:
            x = 0
            STARS3[j][0] = x


pgzrun.go()