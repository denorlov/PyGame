import pygame

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

bright_decrease = 30


def draw(screen):
    screen.fill(WHITE_COLOR)

    box_width = 90

    clr = pygame.Color('#000080')

    alternate_color = pygame.Color(0, 0, 0, 0)
    alternate_color.hsva = (clr.hsva[0], clr.hsva[1], clr.hsva[2] - bright_decrease, clr.hsva[3])

    for i in range(8):
        for j in range(8):
            rect = ((i * box_width) + 2, (j * box_width) + 2, box_width - 4, box_width - 4)
            if (i + j) % 2:
                pygame.draw.rect(screen, clr, rect)
            else:
                pygame.draw.rect(screen, alternate_color, rect)


def fade_out(screen):
    surface = pygame.Surface((screen.get_width(), screen.get_height()))
    surface.fill((0, 0, 255))

    for alpha in range(0, 300):
        surface.set_alpha(alpha)
        draw(screen)
        screen.blit(surface, (0, 0))
        pygame.display.flip()


pygame.init()

size = width, height = 1024, 768
screen = pygame.display.set_mode((width, height))

event = pygame.event.wait()
while event.type != pygame.QUIT:
    if event.type == pygame.MOUSEBUTTONUP:
        bright_decrease += 5
    elif event.type == pygame.KEYUP:
        fade_out(screen)

    draw(screen)
    pygame.display.flip()
    event = pygame.event.wait()

pygame.quit()
