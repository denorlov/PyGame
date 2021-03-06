import pyanimation
import pygame

pygame.init()

FPS = 60

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

girl = pyanimation.Animation("images/spritesheet.png")
girl.create_animation(0, 0, 125, 125, "run", duration=60)
girl.run("run")
girl.x = screen.get_width() // 2

is_running = True
from_left_to_right = True
jump = False
jump_height = 0
while is_running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            elif event.key == pygame.K_RIGHT:
                girl.facing_right = False
            elif event.key == pygame.K_LEFT:
                girl.facing_right = True
            elif event.key == pygame.K_UP:
                jump = True

    if girl.facing_right:
        girl.x -= 4
    else:
        girl.x += 4

    if jump:
        if jump_height < 50:
            jump_height += 4
        else:
            jump = False
            jump_height -= 6
    elif jump_height > 0:
        jump_height -= 6

    screen.fill((255, 255, 255))
    girl_surface = girl.update_surface()
    screen.blit(girl_surface, (girl.x, girl.y - jump_height))
    pygame.display.flip()

pygame.quit()