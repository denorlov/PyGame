import pgzrun
from random import randint


WIDTH = 1000
HEIGHT = 600

points = [(randint(0, WIDTH), randint(0, HEIGHT)) for i in range(100)]

def update():
    pass

def draw():
    screen.fill((0,0,0))

    for point in points:
        x, y = point
        screen.draw.filled_circle((x,y), radius=2, color=(255, 255, 255))
        screen.draw.text(f"{x},{y}", (x,y))

pgzrun.go()