from random import random

import pygame as pygame

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)


def draw(screen):
    screen.fill(BLACK_COLOR)

    font = pygame.font.Font(None, 100)
    text = font.render('Ну как там с деньгами?', 1, WHITE_COLOR)

    text_x = (width // 2) - (text.get_width() // 2)
    text_y = (height // 2) - (text.get_height() // 2)
    screen.blit(text, (text_x, text_y))


def pix(screen):
    for i in range(1000):

        x_coord = random() * width
        y_coord = random() * height
        r, g, b = random() * 255, random() * 255, random() * 255
        pygame.draw.rect(screen, (r, g, b),  (x_coord, y_coord, 4, 4))


pygame.init()


width, height = 1024, 768
screen = pygame.display.set_mode((width, height))
draw(screen)

eventType = pygame.event.wait().type
draw(screen)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    draw(screen)
    pix(screen)
    pygame.display.flip()
pygame.quit()