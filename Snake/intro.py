from random import randint

import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

FPS = 7

pygame.init()



pygame.display.set_caption("Картинка")

image = pygame.image.load("Images/python_intro_img.jpg")


screen_size = (width, height) = (image.get_width(), image.get_height())
screen = pygame.display.set_mode(screen_size)

font = Font(None, 24)

clock = pygame.time.Clock()


start_x = 0
start_y = -image.get_height()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill(BLACK_COLOR)

    screen.blit(image, (start_x + randint(-5, 5), start_y + randint(-5, 5)))
    start_y += 5
    if start_y > image.get_height():
        start_y = -image.get_height()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()