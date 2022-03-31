from random import randint, uniform

import pgzrun
import pygame

from pygame.surface import Surface
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 600

FPS = 60

VELOCITY = 0.8
MAX_DISTANCE = HEIGHT // 5

is_in_full_screen = False

def on_key_down(key):
    global is_in_full_screen

    if key == keys.F:
        is_in_full_screen = not is_in_full_screen
        if is_in_full_screen:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

class Particle:
    def __init__(self, pos, velocity, acc=pygame.Vector2(0, 0)):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        # self.lifetime = 255

    def is_alive(self):
        return True

    def update(self):
        if self.is_alive():
            # self.lifetime -= 1
            self.velocity += self.acc
            self.pos += self.velocity

            if self.pos.x < 0:
                self.pos.x = WIDTH
            if self.pos.x > WIDTH:
                self.pos.x = 0

            if self.pos.y < 0:
                self.pos.y = HEIGHT

            if self.pos.y > HEIGHT:
                self.pos.y = 0

            self.acc = pygame.math.Vector2(0, 0)

    def draw(self, surface:Surface):
        if self.is_alive():
            color = pygame.Color(0, 0, 0, 0)
            color.hsva = (self.hue, 100, 100, self.lifetime)
            pygame.draw.circle(surface, center=self.pos, radius=2, color=color)
            # screen.draw.text(f"life:{self.lifetime}", self.pos)
            # screen.draw.text(f"vel:{self.velocity}", self.pos + Vector2(0, 10))


def map_color(distance, max_distance):
    x = int((max_distance - distance) * 255 / max_distance)
    return 0, x, x


particles = [
    Particle(
        pos=Vector2(randint(0, WIDTH), randint(0, HEIGHT)),
        velocity=Vector2(uniform(-VELOCITY, VELOCITY), uniform(-VELOCITY, VELOCITY))
    ) for _ in range(100)
]

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0,0,0))

    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p0 = particles[i]
            p1 = particles[j]

            distance = (p0.pos - p1.pos).length()
            if distance < MAX_DISTANCE:
                screen.draw.line(p0.pos, p1.pos, color=map_color(distance, MAX_DISTANCE))

    # Draw circles
    for p in particles:
        screen.draw.filled_circle(p.pos, radius=2, color=map_color(1, MAX_DISTANCE))

pgzrun.go()