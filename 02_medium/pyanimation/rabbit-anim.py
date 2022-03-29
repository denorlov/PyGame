import pyanimation
import pygame

pygame.init()

FPS = 60
TILE = 32

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

girl = pyanimation.Animation("images/rabbit.png")
girl.create_animation(0, 6, TILE, TILE, "down", duration=80, cols=3, rows=1)
girl.create_animation(0, 6 + TILE, TILE, TILE, "left", duration=80, cols=3, rows=1)
girl.create_animation(0, 6 + TILE * 2, TILE, TILE, "right", duration=80, cols=3, rows=1)
girl.create_animation(0, 6 + TILE * 3, TILE, TILE, "up", duration=80, cols=3, rows=1)

girl.x = screen.get_width() // 2
girl.y = screen.get_height() // 2

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
                girl.facing_right = True
                girl.run("right")
                from_left_to_right = True
            elif event.key == pygame.K_LEFT:
                girl.facing_right = False
                girl.run("left")
                from_left_to_right = False
            elif event.key == pygame.K_UP:
                girl.run("up")
            elif event.key == pygame.K_DOWN:
                girl.run("down")

    if girl.action_name == "left":
        girl.x = girl.x + 2
    elif girl.action_name == "right":
        girl.x = girl.x - 2
    elif girl.action_name == "up":
        girl.y -= 2
    elif girl.action_name == "down":
        girl.y += 2

    screen.fill((255, 255, 255))
    girl_surface = girl.update_surface()
    screen.blit(girl_surface, (girl.x, girl.y))
    pygame.display.flip()

pygame.quit()