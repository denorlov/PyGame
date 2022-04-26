#importing the stuff we need

import pygame as pg
from random import randint, uniform

#resolution

RESOLUTION = WIDTH, HEIGHT = 1000, 800

#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
velocity = 2

#creating window

FPS = 60
pg.init()
screen = pg.display.set_mode(RESOLUTION)
clock = pg.time.Clock()

#creating circles

class Circle:
    def __init__(self, amount):
        self.amount = amount
        self.circles = []
        self.velocity = [velocity, velocity]
        self.create_circles()

    def create_circles(self):
        for i in range(self.amount):
            self.x = randint(0, WIDTH)
            self.y = randint(0,HEIGHT)
            self.velocity_x = uniform(-self.velocity[0], self.velocity[0])
            self.velocity_y = uniform(-self.velocity[1], self.velocity[1])
            self.pos = (self.x, self.y, self.velocity_x, self.velocity_y)
            self.circles.append(self.pos)

    def update(self):
        self.circles_moved = []

        for i in self.circles:
            self.x = i[0]
            self.y = i[1]

            self.velocity_x = i[2]
            self.velocity_y = i[3]

            self.x += self.velocity_x
            self.y += self.velocity_y

            if self.x >= 0 or self.x == WIDTH:
                self.velocity_x *= -1
            if self.y <= 0 or self.y == HEIGHT:
                self.velocity_y *= -1

            self.position = (self.x, self.y, self.velocity_x, self.velocity_y)
            self.circles_moved.append(self.position)
            self.circles = self.circles_moved

    def connect_circles(self):
        self.lines = []
        for i1 in range(self.amount - 1):
            for i2 in range(i1 + 1, self.amount):
                self.lines.append([self.circles[i1][:2], self.circles[i2][:2]])
        return self.lines


circles = Circle(5)


#main loop

running = True
while running:
    clock.tick(FPS)

    #check if the user quited the programm

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #fill the screnn with black color

    screen.fill(BLACK)

    #draw lines

    for j in circles.connect_circles():
        pg.draw.line(screen, WHITE, start_pos = j[0], end_pos = j[1], width = 2)

    #draw circles

    for i1 in circles.circles:
        pg.draw.circle(screen, WHITE, center = i1[:2], radius = 5)

    circles.update()

    pg.display.update()