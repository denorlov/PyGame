import pygame
from pyanimation import Animation

pygame.init()

FPS = 60
from_left_to_right = True

screen = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()

sans = Animation("images/sprite_update.png")

# sprite->170*300
# 980, 660

sans.create_animation(980 - 10, 660, 170 + 20, 300, "run", duration=200, cols=4, rows=1)
sans.run("run")


is_running = True
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

    if from_left_to_right:
        sans.facing_right = False
        sans.x = sans.x + 4
    else:
        sans.facing_right = True
        sans.x = sans.x - 4

    screen.fill((255, 255, 255))
    sans_surface = sans.update_surface()
    screen.blit(sans_surface, (sans.x, sans.y))
    pygame.display.flip()
    sans.x += 1

pygame.quit()