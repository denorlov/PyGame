import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

pygame.init()
pygame.display.set_caption("Заставка")
screen = pygame.display.set_mode(SCREEN_SIZE)

intro_image = pygame.image.load("python_intro_img.jpg")
start_x = -intro_image.get_width()
speed = 25 # pixels per sec

clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    time_delta_ms = clock.get_time()
    dx = time_delta_ms * speed // 100
    start_x = start_x + dx

    if start_x > 0:
        start_x = 0

    screen.blit(intro_image, (start_x, 0))
    pygame.display.flip()
    clock.tick(120)

pygame.quit()