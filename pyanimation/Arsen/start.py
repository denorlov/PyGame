import pyanimation
import pygame

pygame.init()

FPS = 60

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

girl = pyanimation.Animation("../images/spritesheet.png")
girl.create_animation(0, 0, 125, 125, "run", duration=80)
girl.run("run")
girl.x = screen.get_width() // 2
y_dir = 0

is_running = True
from_left_to_right = True
while is_running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            elif event.key == pygame.K_RIGHT:
                from_left_to_right = True
            elif event.key == pygame.K_LEFT:
                from_left_to_right = False
            elif event.key == pygame.K_UP:
                y_dir = -1
            elif event.key == pygame.K_DOWN:
                y_dir = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_dir = 0

    if from_left_to_right:
        girl.facing_right = False
        girl.x += 4
    else:
        girl.facing_right = True
        girl.x -= 4

    if y_dir > 0:
        girl.y += 4
    elif y_dir < 0:
        girl.y -= 4

    screen.fill((255, 255, 255))
    girl_surface = girl.update_surface()
    screen.blit(girl_surface, (girl.x, girl.y))
    pygame.display.flip()

pygame.quit()