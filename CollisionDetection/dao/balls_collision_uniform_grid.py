import pygame as pgame
from random import randint

vec = pgame.math.Vector2

WIDTH = 1280
HEIGHT = 720

GRIDSIZE = 32

FPS = 60

MOB_SIZE = 10
NUM_MOBS = 600

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTGREY = (40, 40, 40)

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
        pgame.draw.line(screen, LIGHTGREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRIDSIZE):
        pgame.draw.line(screen, LIGHTGREY, (0, y), (WIDTH, y))

def draw_mobs(screen, mobs):
    for mob in mobs:
        color = RED if mob["collisions"] else GREEN
        pgame.draw.rect(screen, color, (mob["pos"], (MOB_SIZE, MOB_SIZE)), 2)

uniform_grid = []

def update_mobs(mobs):
    global uniform_grid

    uniform_grid = [[[]] * (WIDTH // GRIDSIZE + 1) for i in range(HEIGHT // GRIDSIZE + 1)]
    for n, mob in enumerate(mobs):
        position, velocity = mob["pos"], mob["vel"]

        new_position = position + velocity

        new_velocity = velocity
        if new_position.x > WIDTH or new_position.x < 0:
            new_velocity.x *= -1
        if new_position.y < 0 or new_position.y > HEIGHT:
            new_velocity.y *= -1

        new_position = position + velocity

        mobs[n]["vel"] = new_velocity
        mobs[n]["pos"] = new_position

        x_cell = int(new_position.x // GRIDSIZE)
        y_cell = int(new_position.y // GRIDSIZE)
        uniform_grid[y_cell][x_cell].append(mob)

# про оценку сложности uniform grid
#
# 100mob
# ?

# 200mob
# ?

# 1000mob
# ?

def check_collisions(mobs):
    for mob in mobs:
        mob["collisions"].clear()
        position = mob["pos"]

        x_cell = int(position.x // GRIDSIZE)
        y_cell = int(position.y // GRIDSIZE)
        cell_mobs = uniform_grid[y_cell][x_cell]

        for other_mob in cell_mobs:
            if mob == other_mob:
                continue

            rec1 = pgame.Rect(position, (MOB_SIZE, MOB_SIZE))
            rec2 = pgame.Rect(other_mob["pos"], (MOB_SIZE, MOB_SIZE))
            if rec1.colliderect(rec2):
                mob["collisions"].append(other_mob)


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
    screen.fill(BLACK)
    draw_grid()
    draw_mobs(screen, mobs)
    draw_text(f"fps: {int(clock.get_fps())}", 24, WHITE, 5, 5)
    draw_text(f"mobs: {len(mobs)}", 24, WHITE, 5, 22)
    pgame.display.flip()

pgame.quit()
