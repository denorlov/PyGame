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

box_widht = 80

def draw_board(screen):
    screen.fill(BLACK_COLOR)

    pygame.draw.rect(
        screen,
        WHITE_COLOR,
        (X_START - 9, Y_START - 9 , box_widht * 8, box_widht * 8),
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
                (i * (box_widht - 2) + X_START, j * (box_widht - 2) + Y_START, box_widht - 4, box_widht - 4)
            )

def fade_in(screen):
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.fill((0, 0, 0))
    for alpha in range(299, 1, -1):
        fade_surface.set_alpha(alpha)
        draw_board(screen)
        screen.blit(fade_surface, (0,0))
        pygame.display.flip()

size = width, height = 1024, 768

def main():
    global box_widht

    pygame.init()
    screen = pygame.display.set_mode(size)

    fade_in(screen)

    event = pygame.event.wait()
    while event.type != pygame.QUIT:
        if event.type == pygame.MOUSEBUTTONUP:
            box_widht += 5
        elif event.type == pygame.KEYUP:
            box_widht -= 5

        draw_board(screen)

        pygame.display.flip()
        event = pygame.event.wait()

    pygame.quit()


main()