from random import random

import pygame as pygame

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

def draw(screen):
    screen.fill(BLACK_COLOR)

    font = pygame.font.Font(None, 50)
    text = font.render("Hello buddy!", 1, WHITE_COLOR)

    text_w = text.get_width()
    text_h = text.get_height()

    text_x = (width // 2) - (text_w // 2)
    text_y = (height // 2) - (text_h // 2)

    pygame.draw.rect(screen, (100, 100, 100), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 10)

    screen.blit(text, (text_x, text_y))

    for i in range(10000):
        x_coord = random() * width
        y_coord = random() * height
        # r, g, b = random() * 255, random() * 255, random() * 255
        pygame.draw.rect(screen, (222, 255, 255), (x_coord, y_coord, 1, 1))


pygame.init()

width, height = 1024, 720
screen = pygame.display.set_mode((width, height))

eventType = pygame.event.wait().type
draw(screen)
pygame.display.flip()

while eventType != pygame.QUIT:
#    if eventType == pygame.KEYUP:
    draw(screen)
    pygame.display.flip()
    eventType = pygame.event.wait().type

pygame.quit()





