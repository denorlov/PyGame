import pgzrun
import math
import random

WIDTH = 1000
HEIGHT = 600

X0, Y0 = WIDTH // 2, HEIGHT // 2

COLORS = ['BLUE', 'GREEN', 'RED', 'VIOLET', 'CYAN', 'YELLOW', 'BLACK', 'ORANGE', 'GRAY']

ramdom_color = random.randint(0, len(COLORS) - 1)

def update():
    pass
time = 0

def draw():
    global time
    time += 1
    size = 150 * math.sin(time/10)

    ramdom_color = random.randint(0, len(COLORS) - 1) # <- для проверки цветов

    screen.fill((0, 0, 0))
    screen.draw.text(f"{ramdom_color}", (0, 0))

    if ramdom_color == 0:
        color = 'blue'
    if ramdom_color == 1:
        color = 'green'
    if ramdom_color == 2:
        color = 'red'
    if ramdom_color == 3:
        color = 'violet'
    if ramdom_color == 4:
        color = 'cyan'
    if ramdom_color == 5:
        color = 'yellow'
    if ramdom_color == 6:
        color = 'black'
    if ramdom_color == 7:
        color = 'orange'
    if ramdom_color == 8:
        color = 'gray'





    screen.draw.text(
        'Wake up!',
        owidth=1.5,
        ocolor=(255, 255, 0),
        color=color,

        center=(X0, Y0),
        # shadow=(1, 1),
        # scolor=(255, 255, 255),
        angle=time,
        fontsize=size,
    )
    print(size)

pgzrun.go()