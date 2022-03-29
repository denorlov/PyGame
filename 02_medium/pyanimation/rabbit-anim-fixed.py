import pyanimation
import pygame

pygame.init()

FPS = 60
TILE = 32

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

rabbit = pyanimation.Animation("images/rabbit.png")
rabbit.create_animation(0, 6, TILE, TILE, "down", duration=80, cols=3, rows=1)
rabbit.create_animation(0, 6 + TILE, TILE, TILE, "left", duration=80, cols=3, rows=1)
rabbit.create_animation(0, 6 + TILE * 2, TILE, TILE, "right", duration=80, cols=3, rows=1)
rabbit.create_animation(0, 6 + TILE * 3, TILE, TILE, "up", duration=80, cols=3, rows=1)

rabbit.x = screen.get_width() // 2
rabbit.y = screen.get_height() // 2

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
                rabbit.run("right")
                from_left_to_right = True
            elif event.key == pygame.K_LEFT:
                rabbit.run("left")
                from_left_to_right = False
            elif event.key == pygame.K_UP:
                rabbit.run("up")
            elif event.key == pygame.K_DOWN:
                rabbit.run("down")

    if rabbit.action_name == "left":
        rabbit.x -= 2
    elif rabbit.action_name == "right":
        rabbit.x += 2
    elif rabbit.action_name == "up":
        rabbit.y -= 2
    elif rabbit.action_name == "down":
        rabbit.y += 2

    screen.fill((255, 255, 255))
    girl_surface = rabbit.update_surface()
    screen.blit(girl_surface, (rabbit.x, rabbit.y))
    pygame.display.flip()

pygame.quit()