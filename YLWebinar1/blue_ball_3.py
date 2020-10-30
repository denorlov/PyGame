import pygame

size = width, height = 301, 301
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

MYEVENTTYPE = 30
pygame.time.set_timer(MYEVENTTYPE, 1000)

count = 0
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYEVENTTYPE:
            count += 1
            print("Сработал таймер", count)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
