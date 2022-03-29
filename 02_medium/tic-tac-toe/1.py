import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

FPS = 30

TILE = 30
W_TILES, H_TILES = 20, 20

SCREEN_SIZE = WIDTH, HEIGHT = W_TILES * TILE, H_TILES * TILE

CELLS_IN_ROW_TO_WIN = 5

# world state
cells = [[0 for i in range(WIDTH // TILE)] for j in range(H_TILES)]

# control flags
turn = "x" # 'x' player or 'o' player
mouse_x, mouse_y = 0, 0
winner = "" # 'x' player or 'o' player


def check_winner():
    for x in range(0, W_TILES - CELLS_IN_ROW_TO_WIN):
        for y in range(0, H_TILES - CELLS_IN_ROW_TO_WIN):
            has_x, has_o, has_empty  = False, False, False

            for i in range(0, CELLS_IN_ROW_TO_WIN):
                if cells[y][x + i] == "x":
                    has_x = True
                elif cells[y][x + i] == "o":
                    has_o = True
                else:
                    has_empty = True

            if not has_empty:
                if has_x and not has_o:
                    return "x"
                elif has_o and has_x:
                    return "o"

            has_x, has_o, has_empty = False, False, False

            for i in range(0, CELLS_IN_ROW_TO_WIN):
                if cells[y + i][x] == "x":
                    has_x = True
                elif cells[y + i][x] == "o":
                    has_o = True
                else:
                    has_empty = True

            if not has_empty:
                if has_x and not has_o:
                    return "x"
                elif has_o and has_x:
                    return "o"

            has_x, has_o, has_empty = False, False, False

            for i in range(0, CELLS_IN_ROW_TO_WIN):
                if cells[y + i][x + i] == "x":
                    has_x = True
                elif cells[y + i][x + i] == "o":
                    has_o = True
                else:
                    has_empty = True

            if not has_empty:
                if has_x and not has_o:
                    return "x"
                elif has_o and has_x:
                    return "o"

    return None


def draw(screen):
    screen.fill(BLACK_COLOR)

    # cells
    for x in range(0, W_TILES):
        for y in range(0, H_TILES):
            if cells[y][x] == "x":
                # draw x
                pygame.draw.line(
                    screen, GREEN_COLOR,
                    ((x * TILE) + 5, (y * TILE) + 5),
                    ((x * TILE) + TILE - 5, (y * TILE) + TILE - 5),
                    3
                )

                pygame.draw.line(
                    screen, GREEN_COLOR,
                    ((x * TILE) + 5, (y * TILE) + TILE - 5),
                    ((x * TILE) + TILE - 5, (y * TILE) + 5),
                    3
                )
            elif cells[y][x] == "o":
                # draw o
                pygame.draw.circle(
                    screen, BLUE_COLOR,
                    ((x * TILE) + TILE // 2, (y * TILE) + TILE // 2),
                    TILE // 2 - 5,
                    3
                )

    # vertical lines
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (x, 0), (x, HEIGHT))

    # horizontal lines
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (0, y), (WIDTH, y))

    # debug text
    text_surface = font.render(f"fps: {int(clock.get_fps())}, mouse: {mouse_x}, {mouse_y}, turn: {turn}, winner: {winner}", 1, WHITE_COLOR)
    screen.blit(text_surface, (5, 5))

    if winner == "x" or winner == "o":
        pygame.display.set_caption(f"Победил {winner}!")

        text_surface = big_font.render(f"Победил {winner}!", 1, RED_COLOR)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2))
    else:
        # cursor
        pygame.draw.rect(
            screen, GREEN_COLOR if turn == "x" else BLUE_COLOR,
            (
                mouse_x - (mouse_x % TILE) + 2,
                mouse_y - (mouse_y % TILE) + 2,
                TILE - 4,
                TILE - 4
            ),
            2
        )

pygame.init()
pygame.display.set_caption("Крестики-нолики")
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)
big_font = Font(None, 64)
clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if not (winner == "x" or winner == "o"):
                cell_y = mouse_y // TILE
                cell_x = mouse_x // TILE

                if cells[cell_y][cell_x] == 0:
                    if turn == "x":
                        cells[cell_y][cell_x] = "x"
                        turn = "o"
                    else:
                        cells[cell_y][cell_x] = "o"
                        turn = "x"
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

    draw(screen)
    pygame.display.flip()
    winner = check_winner()
    clock.tick(FPS)

pygame.quit()