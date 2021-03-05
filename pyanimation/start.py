import pygame
import sys
from pyanimation import Animation

pygame.init()

FPS = 60

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


is_running = True
while is_running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()