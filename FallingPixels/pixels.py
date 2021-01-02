import random
import sys

import pygame

SCR_RECT = pygame.Rect(0, 0, 1270, 480)
FPS = 60
MAX_REGENERATE_TIME = FPS // 1.5

GRAVITY = 1
CUBE_RECT = pygame.Rect(0, 0, 8, 8)


class Scene:
    class Cube:
        def __init__(self, color, x, floor):
            self.floor = floor * CUBE_RECT.h
            self.speed = 0
            self.is_in_motion = False
            self.prevImpactSpeed = 0
            self.rect = pygame.Rect((x * CUBE_RECT.w, -CUBE_RECT.h), CUBE_RECT.size)
            self.color = color

        def do(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)

            if self.is_in_motion:
                self.rect.y += self.speed
                self.speed += GRAVITY

                if self.rect.bottom >= self.floor:
                    self.rect.bottom = self.floor

                    if self.prevImpactSpeed == 0:
                        self.prevImpactSpeed = self.speed

                    self.prevImpactSpeed /= 3
                    self.speed = -self.prevImpactSpeed

        def reached_floor(self):
            return self.rect.bottom >= self.floor and self.prevImpactSpeed <= 0.1


    class Column:
        def __init__(self):
            self.cubes = []
            self.timer = random.randint(MAX_REGENERATE_TIME // 2, MAX_REGENERATE_TIME)

        def draw(self, screen):
            if not self.cubes:
                return

            if self.timer == 0:
                # initiate move of next cube
                for idx, cube in enumerate(self.cubes):
                    if cube.is_in_motion == False:
                        self.cubes[idx].is_in_motion = True
                        break

                self.timer = random.randint(MAX_REGENERATE_TIME // 2, MAX_REGENERATE_TIME)
            else:
                self.timer -= 1

            for idx, cube in enumerate(self.cubes):
                cube.do(screen)

                if cube.reached_floor():
                    scene.statics.append(cube)
                    del self.cubes[idx]

    def __init__(self, screen, imageSurface):
        self.statics = []

        rect = imageSurface.get_rect()

        pa = pygame.PixelArray(imageSurface)
        self.columns = []
        for x in range(rect.w):
            self.columns.append(self.Column())
            for y in range(rect.h):
                if pa[x][y] != 0:
                    cube = self.Cube(screen.unmap_rgb(pa[x][y]), x, y)
                    self.columns[x].cubes.append(cube)
            self.columns[x].cubes.reverse()
        pa.close()


    def do(self, screen):
        for static in self.statics:
            pygame.draw.rect(screen, static.color, static.rect)

        for column in self.columns:
            column.draw(screen)

pygame.init()
screen = pygame.display.set_mode(SCR_RECT.size)
scene = Scene(screen, pygame.image.load("2021.png").convert())

pygame.mixer.music.load('bells.mp3')
pygame.mixer.music.play(loops=2)

runnning = True
while runnning:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            runnning = False

    screen.fill((0, 0, 0))
    scene.do(screen)
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()