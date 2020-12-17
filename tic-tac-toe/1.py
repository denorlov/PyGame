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

# world state
cells = [[0 for i in range(WIDTH // TILE)] for j in range(H_TILES)]

# control flags
turn = "x" # 'x' player or 'o' player
mouse_x, mouse_y = 0, 0

def update():
    pass

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
    text_surface = font.render(f"fps: {int(clock.get_fps())}, mouse: {mouse_x}, {mouse_y}, turn: {turn}", 1, WHITE_COLOR)
    screen.blit(text_surface, (5, 5))

    # cursor
    pygame.draw.rect(
        screen, GREEN_COLOR if turn == "x" else BLUE_COLOR,
        (
            mouse_x - (mouse_x % TILE) + 2,
            mouse_y - (mouse_y % TILE) + 2,
            TILE - 3,
            TILE - 3
        ),
        0
    )

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)
clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            cell_y = mouse_y // TILE
            cell_x = mouse_x // TILE
            print(cell_y, cell_x, cells[cell_y][cell_x])
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
    update()

    clock.tick(FPS)

pygame.quit()