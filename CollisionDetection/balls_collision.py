import pygame as pgame
from random import randint

vec = pgame.math.Vector2

WIDTH = 1024
HEIGHT = 800
TILESIZE = 32
GRIDSIZE = 32

FPS = 60

MOB_SIZE = 10
NUM_MOBS = 100

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
    for position, velocity in mobs:
        rect = pgame.Rect(position[0], position[1], MOB_SIZE, MOB_SIZE)
        pgame.draw.rect(screen, RED, rect, 2)

def update_mobs(mobs):
    for n, position_velocity in enumerate(mobs):
        position, velocity = position_velocity
        new_position = position + velocity
        mobs[n][0] = new_position
        new_velocity = velocity
        if new_position.x > WIDTH or new_position.x < 0:
            new_velocity.x *= -1
        if new_position.y < 0 or new_position.y > HEIGHT:
            new_velocity.y *= -1
        mobs[n][1] = new_velocity

mobs = [[vec(randint(0, WIDTH), randint(0, HEIGHT)), vec(2, 0).rotate(randint(0, 360))] for n in range(NUM_MOBS)]

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
    # Draw / render
    screen.fill(BLACK)
    draw_grid()
    draw_mobs(screen, mobs)
    draw_text(f"fps: {int(clock.get_fps())}", 18, WHITE, 5, 5)
    draw_text(f"mobs: {len(mobs)}", 18, WHITE, 5, 22)
    pgame.display.flip()

pgame.quit()
