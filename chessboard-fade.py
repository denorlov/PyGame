import pygame as pygame

Y_START = 80
X_START = 100

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = pygame.Color('white')
DARK_GREEN = pygame.Color('#008000')
GREEN = pygame.Color(50, 150, 50)

COLOR = DARK_GREEN

COLOR2 = pygame.Color(0, 0, 0, 0)
COLOR2.hsla = (COLOR.hsla[0], COLOR.hsla[1], COLOR.hsla[2] - 20, COLOR.hsla[3])

BOX_WIDHT = 80

def draw(screen):
    screen.fill(BLACK_COLOR)

    pygame.draw.rect(
        screen,
        WHITE_COLOR,
        (X_START - 9, Y_START - 9 , BOX_WIDHT * 8, BOX_WIDHT * 8),
        2
    )

    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                color = COLOR2
            else:
                color = COLOR

            pygame.draw.rect(
                screen,
                color,
                (i * (BOX_WIDHT - 2) + X_START, j * (BOX_WIDHT - 2) + Y_START, BOX_WIDHT - 4, BOX_WIDHT - 4)
            )

def fade(screen):
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.fill((0, 255, 0))
    for alpha in range(0, 300):
        fade_surface.set_alpha(alpha)
        draw(screen)
        screen.blit(fade_surface, (0,0))
        pygame.display.flip()


pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

event = pygame.event.wait()
while event.type != pygame.QUIT:
    if event.type == pygame.MOUSEBUTTONUP:
        fade(screen)
    elif event.type == pygame.KEYUP:
        BOX_WIDHT -= 5

    draw(screen)

    pygame.display.flip()
    event = pygame.event.wait()

pygame.quit()