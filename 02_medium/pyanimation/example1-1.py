import pygame
from pyanimation import Animation

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

girl = Animation("images/spritesheet.png")
girl.create_animation(0, 0, 125, 125, "run", duration=30)
girl.run("run")

is_running = True
look_left = True
while is_running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

            if event.key == pygame.K_LEFT:
                girl.facing_right = True
            elif event.key == pygame.K_RIGHT:
                girl.facing_right = False

    if girl.facing_right:
        girl.x -= 2
    else:
        girl.x += 2

    screen.fill((255, 255, 255))
    screen.blit(girl.update_surface(), (girl.x, girl.y))
    pygame.display.flip()

pygame.quit()