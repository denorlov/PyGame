import pygame
from pyanimation import Animation

pygame.init()

screen = pygame.display.set_mode((640, 480))

filled_surface = pygame.Surface(screen.get_size())
filled_surface = filled_surface.convert()
filled_surface.fill(pygame.Color("#D9B990"))

clock = pygame.time.Clock()

among_us = Animation("images/among_us_sprite_sheet.jpg")
among_us.create_animation(10, 15, 125, 125, "run", duration=75, cols=1, rows=5)
among_us.run("run")
among_us.x = 0

is_running = True
while is_running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    among_us.x += 4

    screen.blit(filled_surface, (0, 0))
    screen.blit(among_us.update_surface(), (among_us.x, among_us.y))

    pygame.display.flip()

pygame.quit()