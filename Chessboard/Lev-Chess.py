import pygame as pygame

BLACK_COLOR = (0, 0, 0)
BACKGROUND = (150, 150, 255)


def draw(screen):
    screen.fill(BACKGROUND)
    scale = width // 8
    for r in range(2):
        for i in range(4):
            for j in range(4):
                a = j * scale * 2 + scale * r
                b = i * scale * 2 + scale * r
                pygame.draw.rect(screen, (0, 0, 60), (a, b, scale, scale))
                if i == 0 or r == 0 and i == 1:
                    pygame.draw.rect(screen, (200, 20, 20), (a + scale // 4, b + scale // 4, scale * 0.5, scale * 0.5))
                elif i == 3 or r == 1 and i == 2:
                    pygame.draw.rect(screen, (20, 200, 20), (a + scale // 4, b + scale // 4, scale * 0.5, scale * 0.5))


def cursor(mpos):
    a, b = mpos
    pygame.draw.rect(screen, (255, 255, 255), (a, b, 14, 14))


pygame.init()

width, height = 768, 768
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(0)

eventType = pygame.event.wait().type

while pygame.event.wait().type != pygame.QUIT:
    draw(screen)
    cursor(pygame.mouse.get_pos())
    pygame.display.flip()

pygame.quit()