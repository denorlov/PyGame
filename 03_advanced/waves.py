import numpy
import pygame
W, H = SIZE = 800, 800
DAMPING = 0.99
pygame.init()
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
current = numpy.zeros(SIZE, numpy.float32)
previous = numpy.zeros_like(current)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if any(pygame.mouse.get_pressed()):
        mx, my = mouse_pos = pygame.mouse.get_pos()
        previous[my-1:my+2, mx-1:mx+2] = 255*2
    current[1:-1, 1:-1] = ((previous[:-2, :-2] + previous[2:,:-2] + previous[:-2,2:] + previous[2:, 2:]) / 2 - current[1:-1, 1:-1]) * DAMPING
    array = current
    array = numpy.clip(array + 0.5, 0, 255)  # Инверсия и ограничение. Можно отключить :)
    array = numpy.repeat(array.reshape(*SIZE, 1).astype('uint8'), 3, axis=2)
    image = pygame.image.frombuffer(array.flatten(), SIZE, 'RGB')
    previous, current = current, previous
    window.blit(image, (0, 0))
    pygame.display.flip()


