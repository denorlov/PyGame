import pygame as pg
import pygame.display

WIDTH = 1000
HEIGHT = 800
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# initialize pg and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Movement Example")
clock = pg.time.Clock()

class Player:
    def __init__(self, center_x, center_y, width, height):
        self.image = pg.Surface((width, height))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.vx, self.vy = 0, 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vy = -5
        if keystate[pg.K_DOWN]:
            self.vy = 5
        if keystate[pg.K_LEFT]:
            self.vx = -2
        if keystate[pg.K_RIGHT]:
            self.vx = 1
        if self.vx != 0 and self.vy != 0:
            self.vx /= 1.414
            self.vy /= 1.414
        self.rect.x += self.vx
        self.rect.y += self.vy

player = Player(WIDTH // 2, HEIGHT // 2, 64, 64)

# Game loop
running = True
while running:
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
    # Update
    player.update()
    # Draw / render
    screen.fill(BLACK)
    player.draw(screen)
    pg.display.flip()

pg.quit()
