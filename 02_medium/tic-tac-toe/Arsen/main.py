from random import randint

import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

FPS = 50

TILE = 30
W_TILES, H_TILES = 19, 19

SCREEN_SIZE = WIDTH, HEIGHT = W_TILES * TILE, H_TILES * TILE

# world state
CROSS = 1
ZERO = -1
EMPTY = 0
#cells = [[randint(-1, 1) for i in range(WIDTH // TILE)] for j in range(H_TILES)]
cells = None
clock = None

mouse_x, mouse_y = 0, 0

# control flags
turn = CROSS
winner = None
play_with_ai = False


def check_winner(cells):
    x_len = len(cells[0])
    y_len = len(cells)
    for y in range(y_len):
        for x in range(x_len):
            # Horizontal check
            if abs(sum(cells[y][x:x + 5])) == 5:
                return -turn
            # Vertical check
            if y + 5 < y_len:
                y_sum = 0
                for i in range(y, y + 6):
                    y_sum += cells[i][x]
                if abs(y_sum) == 5:
                    return -turn
            # Up right
            ur_sum = 0
            for plus in range(5):
                if y - plus < 0 or x + plus >= x_len:
                    break
                ur_sum += cells[y - plus][x + plus]
            if abs(ur_sum) == 5:
                return -turn

            # Down right
            dr_sum = 0
            for plus in range(5):
                if y + plus >= y_len or x + plus >= x_len:
                    break
                dr_sum += cells[y + plus][x + plus]
            if abs(dr_sum) == 5:
                return -turn


def draw(screen):
    screen.fill(BLACK_COLOR)

    # cells
    for x in range(W_TILES):
        for y in range(H_TILES):
            if cells[y][x] == CROSS:
                # draw x
                x_screen = x * TILE
                y_screen = y * TILE
                x_screen_end = x * TILE + TILE
                y_screen_end = y * TILE + TILE
                pygame.draw.line(
                    screen, GREEN_COLOR,
                    (x_screen, y_screen), (x_screen_end, y_screen_end),
                    3
                )

                x_screen = x * TILE
                y_screen = y * TILE + TILE
                x_screen_end = x * TILE + TILE
                y_screen_end = y * TILE

                pygame.draw.line(
                    screen, GREEN_COLOR,
                    (x_screen, y_screen), (x_screen_end, y_screen_end),
                    3
                )
            elif cells[y][x] == ZERO:
                # draw o
                x_screen = x * TILE + TILE // 2
                y_screen = y * TILE + TILE // 2
                pygame.draw.circle(screen, BLUE_COLOR, (x_screen, y_screen), TILE // 2 - 2, 3)


    # vertical lines
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (x, 0), (x, HEIGHT))

    # horizontal lines
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (0, y), (WIDTH, y))

    turn_text = 'X' if turn == CROSS else 'O'
    if winner:
        winner_text = 'X' if winner == CROSS else 'O'
    else:
        winner_text = 'No one'
    # debug text
    text_surface = font.render(
        f"fps: {int(clock.get_fps())}, mouse: {mouse_x}, {mouse_y}, turn: {turn_text}, winner: {winner_text}, "
        f"AI: {play_with_ai}",
        1, WHITE_COLOR
    )
    screen.blit(text_surface, (5, 5))

    if winner == CROSS or winner == ZERO:
        text_surface = font.render(f"Победил {winner_text}!", 1, RED_COLOR)
        screen.blit(text_surface, (WIDTH // 2 - 40, HEIGHT // 2))
    else:
        # cursor
        x = mouse_x // TILE
        y = mouse_y // TILE

        x_screen = x * TILE
        y_screen = y * TILE

        if cells[y][x] != EMPTY:
            draw_color = RED_COLOR
        else:
            draw_color = GREEN_COLOR

        pygame.draw.rect(
            screen, draw_color,
            (x_screen, y_screen, TILE, TILE),
            3
        )

def ai_move():
    global cells, turn
    turn = CROSS
    x_len = len(cells[0]) - 1
    y_len = len(cells) - 1
    while 1:
        rand_y = randint(0, y_len)
        rand_x = randint(0, x_len)
        if cells[rand_y][rand_x] == EMPTY:
            cells[randint(0, y_len)][randint(0, x_len)] = ZERO
            return


def start():
    global winner, font, cells, clock, turn, mouse_x, mouse_y, play_with_ai
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    font = Font(None, 24)
    clock = pygame.time.Clock()
    cells = [[EMPTY for i in range(WIDTH // TILE)] for j in range(H_TILES)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  # Keyboard processing
                if event.key == pygame.K_r:
                    winner = None
                    cells = [[EMPTY for i in range(WIDTH // TILE)] for j in range(H_TILES)]
                    turn = CROSS
                elif event.key == pygame.K_a:
                    play_with_ai = not play_with_ai
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                x = mouse_x // TILE
                y = mouse_y // TILE

                if cells[y][x] == EMPTY:
                    if turn == CROSS:
                        cells[y][x] = CROSS
                        turn = ZERO
                    elif turn == ZERO:
                        cells[y][x] = ZERO
                        turn = CROSS

        draw(screen)
        winner = check_winner(cells)
        if play_with_ai and turn == ZERO:
            ai_move()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

start()