import pygame as pgame
import math
from random import randint

vec = pgame.math.Vector2

WIDTH = 1152
HEIGHT = 648

TILESIZE = 32
GRIDSIZE = 32

FPS = 60

MOB_SIZE = 10
NUM_MOBS = 150

# define colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_LIGHTGREY = (40, 40, 40)

# initialize pg and create window
pgame.init()
screen = pgame.display.set_mode((WIDTH, HEIGHT))
pgame.display.set_caption("Collision detection playground")
clock = pgame.time.Clock()


def draw_text(text, size, color, x, y):
    font_name = pgame.font.match_font('hack')
    font = pgame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


def draw_grid():
    for x in range(0, WIDTH, GRIDSIZE):
        pgame.draw.line(screen, COLOR_LIGHTGREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRIDSIZE):
        pgame.draw.line(screen, COLOR_LIGHTGREY, (0, y), (WIDTH, y))


def draw_mobs(screen, mobs):
    for mob in mobs:
        rect = pgame.Rect(mob["pos"], (MOB_SIZE, MOB_SIZE))
        color = COLOR_RED if mob["collisions"] else COLOR_GREEN
        pgame.draw.rect(screen, color, rect, 2)


def from_screen_to_cells(screen_x, screen_y):
    x_cell = int(screen_x // GRIDSIZE)  # X_GRIDSIZE
    y_cell = int(screen_y // GRIDSIZE)  # Y_GRIDSIZE
    #print(f"{screen_x}, {screen_y} -> {x_cell}, {y_cell}")
    return x_cell, y_cell

uniform_grid = []
for i in range(math.ceil(HEIGHT / GRIDSIZE)):
    row = []
    uniform_grid.append(row)
    for j in range(math.ceil(WIDTH / GRIDSIZE)):
        row.append([])


def update_mobs(mobs):
    # creating grid
    global uniform_grid

    for row in uniform_grid:
        for cell in row:
            cell.clear()

    for n, mob in enumerate(mobs):
        position, velocity = mob["pos"], mob["vel"]

        new_position = position + velocity

        new_velocity = velocity
        if new_position.x > WIDTH or new_position.x < 0:
            new_velocity.x *= -1
        if new_position.y < 0 or new_position.y > HEIGHT:
            new_velocity.y *= -1
        mobs[n]["vel"] = new_velocity

        new_position = position + new_velocity

        mobs[n]["pos"] = new_position

        # update  uniform_grid
        x_cell_mob, y_cell_mob = from_screen_to_cells(new_position.x, new_position.y)
        uniform_grid[y_cell_mob][x_cell_mob].append(mob)


def check_collisions(mobs):
    for mob in mobs:  # 100
        mob["collisions"].clear()

        x_cell, y_cell = from_screen_to_cells(mob["pos"].x, mob["pos"].y)
        grid_mobs = uniform_grid[y_cell][x_cell]
        for n, other_mob in enumerate(grid_mobs):  # 99
            if mob == other_mob:
                continue

            rec1 = pgame.Rect(mob["pos"], (MOB_SIZE, MOB_SIZE))
            rec2 = pgame.Rect(other_mob["pos"], (MOB_SIZE, MOB_SIZE))
            if rec1.colliderect(rec2):
                mob["collisions"].append(n)


# position, velocity
mobs = [
    {
        "pos": vec(randint(0, WIDTH), randint(0, HEIGHT)),
        "vel": vec(2, 0).rotate(randint(0, 360)),
        "collisions": []
    } for n in range(NUM_MOBS)
]

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pgame.event.get():
        if event.type == pgame.QUIT:
            running = False

    # Update
    update_mobs(mobs)
    check_collisions(mobs)

    # Draw / render
    screen.fill(COLOR_BLACK)
    draw_grid()
    draw_mobs(screen, mobs)
    draw_text(f"fps: {int(clock.get_fps())}", 18, COLOR_WHITE, 5, 5)
    draw_text(f"mobs: {len(mobs)}", 18, COLOR_WHITE, 5, 22)
    pgame.display.flip()

pgame.quit()
