import pgzrun
import random
w, h = 1000, 600
a = []
for i in range(1000):
    a.append([random.randint(0, w), random.randint(0, h)])
b = []
for i in range(1000):
    b.append([random.randint(0, w), random.randint(0, h)])
c = []
for i in range(1000):
    c.append([random.randint(0, w), random.randint(0, h)])
def update():
    pass
def draw():
    screen.fill((random.randint(20, 20), random.randint(0, 0), random.randint(30, 30)))
    for i in range(len(a)):
        star = a[i]
        x = star[0]
        y = star[1]
        screen.draw.filled_circle((x, y), 1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        a[i][0] = x + 6
        if a[i][0] > w:
            a[i][0] = a[i][0] - w
    for i in range(len(b)):
        star = b[i]
        o = star[0]
        p = star[1]
        screen.draw.filled_circle((o, p), 2, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        b[i][0] = o + 4
        if b[i][0] > w:
            b[i][0] = b[i][0] - w
    for i in range(len(c)):
        star = c[i]
        g = star[0]
        f = star[1]
        screen.draw.filled_circle((g, f), 4, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        c[i][0] = g + 2
        if c[i][0] > w:
            c[i][0] = c[i][0] - w
pgzrun.go()