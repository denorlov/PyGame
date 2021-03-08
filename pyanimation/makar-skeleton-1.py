import pygame
import pyanimation
from pyanimation import Animation

pygame.init()

FPS = 60
High = 300
Width_S = 170
Width_H = 230
Step = 10

screen = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()

sans = Animation("images/sprite.png")
sans.create_animation(0 + 20, 310 + 20, Width_S + Step, High, "right", duration=200, cols=4, rows=1)
sans.create_animation(10 + 20, 630 + 20, Width_S + Step, High, "left", duration=200, cols=4, rows=1)
sans.create_animation(0 + 20, 0 + 20, Width_H + Step, High, "down", duration=200, cols=4, rows=1)
sans.create_animation(1020 + 20, 0 + 20, Width_H + Step, High + 30, "up", duration=200, cols=4, rows=1)
sans.x = screen.get_width() // 2
sans.y = screen.get_height() // 2
sans.run("right")
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
                sans.run("right")
            elif event.key == pygame.K_LEFT:
                sans.run("left")
            elif event.key == pygame.K_UP:
                sans.run("up")
            elif event.key == pygame.K_DOWN:
                sans.run("down")

    if sans.action_name == "left":
        sans.x -= 2
    elif sans.action_name == "right":
        sans.x += 2
    elif sans.action_name == "up":
        sans.y -= 2
    elif sans.action_name == "down":
        sans.y += 2

    screen.fill((255, 255, 255))
    sans_surface = sans.update_surface()
    screen.blit(sans_surface, (sans.x, sans.y))
    pygame.display.flip()

pygame.quit()
