import pygame as pygame

from tiled.spritesheet import Spritesheet

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

ss = Spritesheet(
    "../assets/tileset3b.png",
    24,
    24,
    pygame.Color(255, 0, 255)
)

print([ss])

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 255))
    for i in range(0, 34):
        img = ss[9 + i % 6, 2]
        screen.blit(img, (i * 24, 0))
    for i in range(0, 34):
        ss.blit_tile(screen, 12 + i % 8, 8, i * 24, 576)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()