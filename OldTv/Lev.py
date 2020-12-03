import pygame as pygame

from random import random

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)


def draw(screen):
    screen.fill((255, 180, 25))

    for i in range(1000):
        x_coord = random() * width
        y_coord = random() * height
        r, g, b = random() * 255, random() * 255, random() * 255
        scale = random() * 10
        pygame.draw.rect(screen, (r, g, b), (x_coord, y_coord, scale, scale))

    font = pygame.font.Font(None, 50)
    text = font.render("Apelsin Studio", 1, WHITE_COLOR)

    text_w = text.get_width()
    text_h = text.get_height()

    text_x = width // 2 - text_w // 2
    text_y = height // 2 - text_h // 2

    pygame.draw.rect(screen, BLACK_COLOR, (text_x - 10, text_y - 10, text_w + 20, text_h + 20))

    screen.blit(text, (text_x, text_y))


pygame.init()

width, height = 1024, 720
screen = pygame.display.set_mode((width, height))

eventType = pygame.event.wait().type

while eventType != pygame.QUIT:
    #if eventType == pygame.MOUSEBUTTONDOWN:
    draw(screen)
    pygame.display.flip()
    eventType = pygame.event.wait().type

pygame.quit()