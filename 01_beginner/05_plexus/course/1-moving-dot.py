from random import randint, uniform
import pgzrun

WIDTH = 1000
HEIGHT = 600

VELOCITY = 0.8
POINTS_CNT = 100

points = [
    (randint(0, WIDTH), randint(0, HEIGHT))
    for i in range(POINTS_CNT)
]
VELOCITIES = [
    (uniform(-VELOCITY, VELOCITY), uniform(-VELOCITY, VELOCITY))
    for i in range(POINTS_CNT)
]

def update():
    for i in range(len(points)):
        x, y  = points[i]
        dx, dy = VELOCITIES[i]
        x = x + dx
        y = y + dy
        points[i] = [x, y]

def draw():
    screen.fill((0, 0, 0))

    for point in points:
        x, y = point
        screen.draw.filled_circle((x, y), radius=2, color=(255, 255, 255))


pgzrun.go()