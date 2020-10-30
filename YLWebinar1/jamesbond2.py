import pygame

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
x_pos = 0
v = 60  # пикселей в секунду

def draw():
    global x_pos
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
    t = clock.tick()  # в миллисекундах
    x_pos += v * t / 1000  # v * t в секундах


while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    draw()

    # обновление экрана
    pygame.display.flip()

pygame.quit()