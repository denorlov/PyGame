import pygame

pygame.init()
pygame.display.set_mode((400, 300))

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
