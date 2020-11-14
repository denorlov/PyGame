import random

import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

running = True

FPS = 60

big_stars = []
medium_stars = []
small_stars = []
very_big_stars = []
p = 0


def init():
    pygame.init()

    for i in range(1000):
        small_stars.append(((random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)), random.randint(1, 14)))
    for i in range(250):
        medium_stars.append(
            ((random.randint(0, WIDTH - 1), random.randint(HEIGHT // 10, HEIGHT // 1.06 - 1)), random.randint(1, 14)))
    for i in range(100):
        big_stars.append(
            ((random.randint(0, WIDTH - 1), random.randint(HEIGHT // 7, HEIGHT // 1.14 - 1)), random.randint(1, 14)))
    for i in range(50):
        very_big_stars.append(
            ((random.randint(0, WIDTH - 1), random.randint(HEIGHT // 5, HEIGHT // 1.3 - 1)), random.randint(1, 14)))


def draw(screen):
    global p
    screen.fill((20, 0, 30))
    for i in small_stars:
        if i[1] == 1:
            color = (0, 0, 0)
        elif 5 >= i[1] >= 2:
            color = (240, 100, 0)
        elif 8 >= i[1] >= 6:
            color = (240, 240, 0)
        elif 11 >= i[1] >= 9:
            color = (240, 190, 0)
        else:
            color = (0, 240, 240)
        pygame.draw.circle(screen, color, ((i[0][0] + p) % WIDTH, i[0][1]), 1)
    for i in medium_stars:
        if i[1] == 1:
            color = (0, 0, 0)
        elif 5 >= i[1] >= 2:
            color = (240, 100, 0)
        elif 8 >= i[1] >= 6:
            color = (240, 240, 0)
        elif 11 >= i[1] >= 9:
            color = (240, 190, 0)
        else:
            color = (0, 240, 240)
        pygame.draw.circle(screen, color, ((i[0][0] + int(p * 1.3)) % WIDTH, i[0][1]), 2)
    for i in big_stars:
        if i[1] == 1:
            color = (0, 0, 0)
        elif 5 >= i[1] >= 2:
            color = (240, 100, 0)
        elif 8 >= i[1] >= 6:
            color = (240, 240, 0)
        elif 11 >= i[1] >= 9:
            color = (240, 190, 0)
        else:
            color = (0, 240, 240)
        pygame.draw.circle(screen, color, ((i[0][0] + p * 2) % WIDTH, i[0][1]), 4)
    for i in very_big_stars:
        if i[1] == 1:
            color = (0, 0, 0)
        elif 5 >= i[1] >= 2:
            color = (240, 100, 0)
        elif 8 >= i[1] >= 6:
            color = (240, 240, 0)
        elif 11 >= i[1] >= 9:
            color = (240, 190, 0)
        else:
            color = (0, 240, 240)
        pygame.draw.circle(screen, color, ((int(i[0][0] + p * 2.5)) % WIDTH, i[0][1]), 6)
    p += 1


init()

while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    draw(screen)

    # пауза на 1 / fps cek
    clock.tick(FPS)

    # обновление экрана
    pygame.display.flip()

pygame.quit()