import csv
import math

import pygame as pygame

from tiled.spritesheet import Spritesheet
from tiled.tilemap import Tilemap

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

SCREEN_SIZE = WIDTH, HEIGHT = 1096, 616

def draw_text(text, size, color, x, y):
    font_name = pygame.font.match_font('hack')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(SCREEN_SIZE)
#screen = pygame.display.set_mode(SCREEN_SIZE, flags=pygame.FULLSCREEN)

clock = pygame.time.Clock()

level1_map = []
with open("assets/5.csv") as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        ints_row = [int(i) for i in row]
        level1_map.append(ints_row)

spritesheet = Spritesheet(
    "assets/tileset3b.png",
    tile_width=24, tile_height=24,
    colorkey=pygame.Color(255, 0, 255)
)

start_x = (screen.get_width() - len(level1_map[0]) * 24) // 2
start_y = (screen.get_height() - len(level1_map) * 24) // 2

class Hero:
    def __init__(self, x, y, width, height):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.acceleration_const = pygame.Vector2(0.2, 0.2)

        self.width = width
        self.height = height

    def draw(self, surface_to_draw):
        pygame.draw.rect(
            surface_to_draw,
            GREEN_COLOR,
            (self.position.x, self.position.y, self.width, self.height)
        )

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                print('space pressed')
                self.acceleration_const.x += 0.4
                self.acceleration_const.y += 0.4
            elif e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                print('space unpressed')
                self.acceleration_const.x -= 0.4
                self.acceleration_const.y -= 0.4

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print('left')
            self.acceleration.x = -self.acceleration_const.x
        if keys[pygame.K_RIGHT]:
            print('right')
            self.acceleration.x = self.acceleration_const.x
        if keys[pygame.K_UP]:
            print('up')
            self.acceleration.y = -self.acceleration_const.y
        if keys[pygame.K_DOWN]:
            print('down')
            self.acceleration.y = self.acceleration_const.y

        self.acceleration = self.acceleration - self.velocity * 0.01
        self.velocity = self.velocity + self.acceleration
        temp_position = self.position + self.velocity + 0.5 * self.acceleration

        is_on_screen = True
        if temp_position.x < 0:
            self.position.x = 0
            self.velocity.x = 0
            is_on_screen = False
        if temp_position.y < 0:
            self.position.y = 0
            self.velocity.y = 0
            is_on_screen = False
        if is_on_screen:
            self.position = temp_position


map_height_px = len(level1_map) * 24
hero = Hero(screen.get_width() // 2, start_y + map_height_px - 24 * 2 , 24, 24)

is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    screen.fill(BLACK_COLOR)

    for c, row in enumerate(level1_map):
        for r, item_code in enumerate(row):
            if item_code != -1:
                rect = pygame.Rect(
                    start_x + r * spritesheet.tile_width,
                    start_y + c * spritesheet.tile_height,
                    spritesheet.tile_width,
                    spritesheet.tile_height
                )

                tile_col = item_code % 20
                tile_row = item_code // 20
                tile_img = spritesheet.image_at(
                    tile_col=tile_col, tile_row=tile_row
                )
                screen.blit(tile_img, rect.topleft)

    hero.update(events)
    hero.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()