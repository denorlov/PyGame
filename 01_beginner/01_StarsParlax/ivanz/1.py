import pgzrun
import random

WIDTH = 1000
HEIGHT = 500

little_stars = []
medium_stars = []
big_stars = []
large_stars = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

for i in range(3000):
    little_stars.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            random.randint(0, 220),
            random.randint(0, 220),
            random.randint(0, 220)
        ]
    )

for i in range(1000):
    medium_stars.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            random.randint(0, 220),
            random.randint(0, 220),
            random.randint(0, 220)
        ]
    )

for i in range(500):
    big_stars.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            random.randint(0, 220),
            random.randint(0, 220),
            random.randint(0, 220)
        ]
    )

for i in range(250):
    large_stars.append(
        [
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            random.randint(0, 220),
            random.randint(0, 220),
            random.randint(0, 220)
        ]
    )


def update():
    pass


def draw():
    screen.fill(BLACK)

    for i in range(len(little_stars)):
        star = little_stars[i]

        x = star[0]
        y = star[1]
        r = star[2]
        g = star[3]
        b = star[4]

        screen.draw.filled_circle((x, y), 1, (r, g, b))

        if x + 1 <= WIDTH:
            little_stars[i][0] = x + 1
        else:
            little_stars[i][0] = 0

    for i in range(len(medium_stars)):
        star = medium_stars[i]

        x = star[0]
        y = star[1]
        r = star[2]
        g = star[3]
        b = star[4]

        screen.draw.filled_circle((x, y), 2, (r, g, b))

        if x + 2 <= WIDTH:
            medium_stars[i][0] = x + 2
        else:
            medium_stars[i][0] = 0

    for i in range(len(big_stars)):
        star = big_stars[i]

        x = star[0]
        y = star[1]
        r = star[2]
        g = star[3]
        b = star[4]

        screen.draw.filled_circle((x, y), 3, (r, g, b))

        if x + 3 <= WIDTH:
            big_stars[i][0] = x + 3
        else:
            big_stars[i][0] = 0

    for i in range(len(large_stars)):
        star = large_stars[i]

        x = star[0]
        y = star[1]
        r = star[2]
        g = star[3]
        b = star[4]

        screen.draw.filled_circle((x, y), 4, (r, g, b))

        if x + 4 <= WIDTH:
            large_stars[i][0] = x + 4
        else:
            large_stars[i][0] = 0


pgzrun.go()