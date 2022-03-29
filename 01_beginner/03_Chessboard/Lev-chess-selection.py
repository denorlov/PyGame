import pygame as pygame

BLACK_COLOR = (0, 0, 0)
BACKGROUND = (150, 150, 255)


def draw(screen):
    screen.fill(BLACK_COLOR)
    scale = width // 8
    for r in range(2):
        for i in range(4):
            for j in range(4):
                a = j * scale * 2 + scale * r
                b = i * scale * 2 + scale * r
                c, d = pygame.mouse.get_pos()
                if a + scale > c >= a and b + scale > d >= b:
                    pygame.draw.rect(screen, (70, 70, 120), (a, b, scale, scale))
                else:
                    pygame.draw.rect(screen, (0, 0, 60), (a, b, scale, scale))
                if i == 0 or r == 0 and i == 1:
                    pygame.draw.rect(screen, (200, 20, 20), (a + scale // 4, b + scale // 4, scale * 0.5, scale * 0.5))
                elif i == 3 or r == 1 and i == 2:
                    pygame.draw.rect(screen, (20, 200, 20), (a + scale // 4, b + scale // 4, scale * 0.5, scale * 0.5))
    for r in range(2):
        for i in range(4):
            for j in range(4):
                a = j * scale * 2 + scale * r
                if r == 1:
                    b = i * scale * 2 + scale * 0
                else:
                    b = i * scale * 2 + scale * 1
                pygame.draw.rect(screen, (130, 130, 255), (a, b, scale, scale))
                c, d = pygame.mouse.get_pos()
                if a + scale > c >= a and b + scale > d >= b:
                    pygame.draw.rect(screen, (180, 180, 255), (a, b, scale, scale))
                else:
                    pygame.draw.rect(screen, (130, 130, 255), (a, b, scale, scale))


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