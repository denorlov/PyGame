import random

import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720

worldsize = 1080
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

running = True

FPS = 60

stars = []
p = 0


def init():
    pygame.init()
    for i in range(10000):
        stars.append((random.randint(0 - worldsize, worldsize), random.randint(0 - worldsize, worldsize), random.randint(1, worldsize)))

    print(stars)


def draw(screen):
    global p
    screen.fill((20, 0, 30))
    for i in stars:
        color = (i[2] % 255, i[2] % 255, i[2] % 255)
        if i[2] != 0:
            pygame.draw.circle(screen, color, 100 / i[2] * i[1] + WIDTH // 2, 100 / i[2] * i[0] + HEIGHT // 2, 1)
    # for i in range(len(stars)):
    #     print(stars[i][0])
    #     stars[i][0] += 1
    #     if stars[i][2] == worldsize:
    #         stars[i][2] = 0


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