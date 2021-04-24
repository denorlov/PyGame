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
NUM_MOBS = 1000

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


def from_screen_to_cell(screen_x, screen_y):
    k = int(WIDTH / GRIDSIZE)
    #print(screen_x, screen_y, math.floor(screen_x / GRIDSIZE), math.floor(screen_y / GRIDSIZE))
    cell = math.floor(screen_x / GRIDSIZE) + (math.floor(screen_y / GRIDSIZE) * k)
    return cell

hash_grid = []
for i in range(math.ceil(WIDTH / GRIDSIZE) * math.ceil(HEIGHT / GRIDSIZE)):
    hash_grid.append([])

class Mob:
    def __init__(self, position, velocity):
        self.pos = position
        self.vel = velocity
        self.collisions = []

    def draw(self, screen):
        rect = pgame.Rect(self.pos, (MOB_SIZE, MOB_SIZE))
        color = COLOR_RED if self.collisions else COLOR_GREEN
        pgame.draw.rect(screen, color, rect, 2)

    def check_collisions(self):
        self.collisions.clear()

        cell = from_screen_to_cell(self.pos.x, self.pos.y)
        grid_mobs = hash_grid[cell]
        for n, other_mob in enumerate(grid_mobs):  # 99
            if mob == other_mob:
                continue

            rec1 = pgame.Rect(self.pos, (MOB_SIZE, MOB_SIZE))
            rec2 = pgame.Rect(other_mob.pos, (MOB_SIZE, MOB_SIZE))
            if rec1.colliderect(rec2):
                self.collisions.append(n)

    def update(self):
        new_position = self.pos + self.vel

        new_velocity = self.vel
        if new_position.x > WIDTH or new_position.x < 0:
            new_velocity.x *= -1
        if new_position.y < 0 or new_position.y > HEIGHT:
            new_velocity.y *= -1
        self.vel = new_velocity

        new_position = self.pos + new_velocity
        self.pos = new_position

mobs = [
    Mob(
        position=vec(randint(0, WIDTH), randint(0, HEIGHT)),
        velocity=vec(2, 0).rotate(randint(0, 360))
    ) for n in range(NUM_MOBS)
]

def update_mobs(mobs):
    # creating grid
    global hash_grid

    for cell in hash_grid:
        cell.clear()

    for mob in mobs:
        mob.update()

        # update  uniform_grid
        cell = from_screen_to_cell(mob.pos.x, mob.pos.y)
        hash_grid[cell].append(mob)


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
    for mob in mobs:
        mob.check_collisions()

    # Draw / render
    screen.fill(COLOR_BLACK)
    draw_grid()

    for mob in mobs:
        mob.draw(screen)

    draw_text(f"fps: {int(clock.get_fps())}", 18, COLOR_WHITE, 5, 5)
    draw_text(f"mobs: {len(mobs)}", 18, COLOR_WHITE, 5, 22)
    pgame.display.flip()

pgame.quit()
