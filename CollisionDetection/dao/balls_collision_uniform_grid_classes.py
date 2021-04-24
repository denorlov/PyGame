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

class UniformGrid:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.clear()

    def clear(self):
        x_cells = int(self.screen_width / self.cell_size) + 1
        y_cells = int(self.screen_height / self.cell_size) + 1
        self.grid = [[[]] * x_cells for _ in range(y_cells)]

    def add_mob(self, mob):
        x_cell = int(mob.position.x / self.cell_size)
        y_cell = int(mob.position.y / self.cell_size)
        mobs = self.grid[y_cell][x_cell]
        if mobs:
            mobs.append(mob)
        else:
            self.grid[y_cell][x_cell] = [mob]


    def get_mobs(self, mob):
        x_cell = int(mob.position.x / self.cell_size)
        y_cell = int(mob.position.y / self.cell_size)
        return self.grid[y_cell][x_cell]

    def draw(self):
        for x in range(0, self.screen_width, self.cell_size):
            pgame.draw.line(screen, LIGHTGREY, (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, self.cell_size):
            pgame.draw.line(screen, LIGHTGREY, (0, y), (self.screen_width, y))


uniform_grid = UniformGrid(WIDTH, HEIGHT, GRIDSIZE)

class Mob:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.collisions = []

    def draw(self, screen):
        color = RED if self.collisions else GREEN
        pgame.draw.rect(screen, color, (self.position, (MOB_SIZE, MOB_SIZE)), 2)

    def update_position(self):
        new_position = self.position + self.velocity

        new_velocity = self.velocity
        if new_position.x > WIDTH or new_position.x < 0:
            new_velocity.x *= -1
        if new_position.y < 0 or new_position.y > HEIGHT:
            new_velocity.y *= -1

        new_position = self.position + self.velocity

        self.velocity = new_velocity
        self.position = new_position


def update_mobs(mobs):
    global uniform_grid

    uniform_grid.clear()

    for mob in mobs:
        mob.update_position()
        uniform_grid.add_mob(mob)

# про оценку сложности uniform grid
#
# 100mob
# ?

# 200mob
# ?

# 1000mob
# ?

def check_collisions(mobs):
    for mob in mobs: #1000
        mob.collisions.clear()
        position = mob.position

        cell_mobs = uniform_grid.get_mobs(mob) #1000

        for other_mob in cell_mobs:
            if mob == other_mob: # 999
                continue

            rec1 = pgame.Rect(position, (MOB_SIZE, MOB_SIZE))
            rec2 = pgame.Rect(other_mob.position, (MOB_SIZE, MOB_SIZE))
            if rec1.colliderect(rec2):
                mob.collisions.append(other_mob)


# position, velocity
mobs = [
    Mob(
        position=vec(randint(0, WIDTH), randint(0, HEIGHT)),
        velocity=vec(2, 0).rotate(randint(0, 360))
    ) for n in range(NUM_MOBS)
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
    uniform_grid.draw()
    for mob in mobs:
        mob.draw(screen)
    draw_text(f"fps: {int(clock.get_fps())}", 24, WHITE, 5, 5)
    draw_text(f"mobs: {len(mobs)}", 24, WHITE, 5, 22)
    pgame.display.flip()

pgame.quit()
