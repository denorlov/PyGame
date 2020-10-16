import pygame as pygame
from random import random

def draw(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Hi buddy!", 1, (100, 100, 100))

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2

    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10, text.get_width() + 20, text.get_height() + 20))

    screen.blit(text, (text_x, text_y))

    screen.fill((0, 255, 0), (10, 10, 300, 300))

    for i in range(10000):
        coords = (random() * width, random() * height, 3, 3)
        screen.fill((255, 255, 255), coords)

pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)


while pygame.event.wait().type != pygame.QUIT:
    draw(screen)
    pygame.display.flip()

pygame.quit()