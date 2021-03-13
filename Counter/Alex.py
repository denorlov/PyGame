import random
import sys

import time
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

sec = int(2)
num = int(10)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

font = pygame.font.SysFont("Sans", 500)
font2 = pygame.font.SysFont("Sans", 100)

text = font.render("Score: " + str(num), True, (0, 0, 0))
screen.blit(text, [300, 300])

is_running = True
while is_running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

            elif event.key == pygame.K_RIGHT:
                sec += 1

            elif event.key == pygame.K_LEFT:
                if sec > 1:
                    sec -= 1

    num = random.randint(0, 100)

    text = font.render(str(num), True, (0, 0, 0))
    text2 = font2.render('Скорость: ' + str(sec) + ' сек.', True, (0, 0, 0))

    screen.fill((255, 255, 255))
    screen.blit(text, [750, 400])
    screen.blit(text2, [1000, 900])
    pygame.display.flip()

    time.sleep(sec)

pygame.quit()