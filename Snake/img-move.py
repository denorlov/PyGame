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

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

start_x = 0
speed = 15 # pixels per sec
last_time_ms = 0

def draw(screen):
    global last_time_ms, start_x

    time_delta_ms = clock.get_time()
    dx = time_delta_ms * speed // 100
    start_x = start_x + dx

    screen.fill(BLACK_COLOR)

    screen.blit(bunny_image, (100 + start_x, 100))
    screen.blit(plant_img, (200 + start_x, 200))
    screen.blit(crystal_img, (300 + start_x, 300))
    screen.blit(rock_img, (400 + start_x, 400))


pygame.init()
pygame.display.set_caption("Картинка")
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)

bunny_image = pygame.image.load("bunny.png")
plant_img = pygame.image.load("plant.png")
crystal_img = pygame.image.load("crystal.png")
rock_img = pygame.image.load("rock.png")

clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()