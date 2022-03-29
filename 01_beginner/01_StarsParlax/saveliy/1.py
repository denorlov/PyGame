import random
import pgzrun

WIDTH, HEIGHT = 1080, 720

STARS = []
STARS1 = []
STARS2 = []

for i in range(1000):
   STARS.append(
       [
           random.randint(0, WIDTH), # x
           random.randint(0, HEIGHT) # y
       ]
   )
for i1 in range(500):
   STARS1.append(
       [
           random.randint(0, WIDTH), # x
           random.randint(0, HEIGHT) # y
       ]
   )
for i2 in range(250):
   STARS2.append(
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

       if x == WIDTH:
           x = 0
       screen.draw.filled_circle((x, y), 2, (255, 255, 255))
       STARS[j][0] = x + 1

   for j1 in range(len(STARS1)):
       star1 = STARS1[j1]

       x = star1[0]
       y = star1[1]

       if x == WIDTH:
           x = 0
       screen.draw.filled_circle((x, y), 3, (255, 255, 255))
       STARS1[j1][0] = x + 0.75
   for j2 in range(len(STARS2)):
       star2 = STARS1[j2]

       x = star2[0]
       y = star2[1]

       if x == WIDTH:
           x = 0
       screen.draw.filled_circle((x, y), 4, (255, 255, 255))
       STARS1[j2][0] = x + 0.5
   # for j3 in range(1000):
   #     screen.blit('C:\Users\kuznetsov.s\PycharmProjects\untitled\images\amogus1.png', 100, 100)
pgzrun.go()