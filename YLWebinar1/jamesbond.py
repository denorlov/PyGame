import pygame

size = width, height = 1501, 301
screen = pygame.display.set_mode(size)

running = True
x_pos = 0


def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)


while running:
    events = pygame.event.get()
    for event in events:
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    draw(screen)
    x_pos += 1

    # обновление экрана
    pygame.display.flip()

pygame.quit()