import pygame
from pygame.time import Clock

size = width, height = 1501, 301
screen = pygame.display.set_mode(size)

running = True
x_pos = 250

V = 30
FPS = 30

clock = pygame.time.Clock()

x_y_mouse = (0, 0)


def draw(screen):
    #screen.fill((0, 0, 0))

    # красный летяший шар
    pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
    # курсор мыши
    pygame.draw.circle(screen, (255, 255, 255), x_y_mouse, 20)


while running:
    events = pygame.event.get()
    for event in events:
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x_y_mouse = event.pos

    # отрисовка и изменение свойств объектов
    draw(screen)

    # обновление экрана
    pygame.display.flip()

    x_pos += V / FPS
    clock.tick(FPS)

pygame.quit()