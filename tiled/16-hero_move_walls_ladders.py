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

SCREEN_SIZE = WIDTH, HEIGHT = 850, 550


def draw_text(x, y, text, size=20, color=WHITE_COLOR):
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
with open("assets/4.csv") as f:
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

wall_codes = [1, 72, 166, 171, 172, 201, 202, 203, 220, 223, 226, 307, 340, 342, 344]
ladder_codes = [132, 133]
rope = [112]

def collide_with(sprite_rect, level_map, tile_codes_to_check):
    for r, row in enumerate(level_map):
        for c, item_code in enumerate(row):
            if item_code in tile_codes_to_check:
                rect = pygame.Rect(
                    start_x + c * spritesheet.tile_width,
                    start_y + r * spritesheet.tile_height,
                    spritesheet.tile_width,
                    spritesheet.tile_height
                )

                if sprite_rect.colliderect(rect):
                    #print(f"sprite:{sprite_rect} collides with: {rect},
                    # row: {r}, col: {c}, item_code: {item_code}")
                    return True

    return False


class Hero:
    def __init__(self, x, y, width, height):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        self.width = width
        self.height = height

    def draw(self, surface_to_draw):
        collide_with_wall = collide_with(self.get_hit_box(self.position), level1_map, wall_codes)

        if collide_with_wall:
            color = RED_COLOR
        else:
            color = GREEN_COLOR

        pygame.draw.rect(surface_to_draw, color, self.get_bbox(), 2)

    def get_bbox(self, position=None): # -> pygame.Rect
        if position is None:
            return pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        else:
            return pygame.Rect(position.x, position.y, self.width, self.height)

    def get_hit_box(self, position=None): # -> pygame.Rect
        if position is None:
            return pygame.Rect(self.position.x + 2, self.position.y + 2, self.width - 4, self.height - 4)
        else:
            return pygame.Rect(position.x + 2, position.y + 2, self.width - 4, self.height - 4)

    def update(self, events):
        acceleration = pygame.Vector2(0, 0.4)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print('left')
            acceleration.x = -0.1
        if keys[pygame.K_RIGHT]:
            print('right')
            acceleration.x = 0.1

        if collide_with(self.get_bbox(), level1_map, ladder_codes):
            if keys[pygame.K_UP]:
                print('up on ladder')
                self.velocity.y = -1
                acceleration.y = 0
                self.velocity.x = 0
                acceleration.x = 0
            elif keys[pygame.K_DOWN]:
                print('down on ladder')
                self.velocity.y = 1
                acceleration.y = 0
                self.velocity.x = 0
                acceleration.x = 0
            else:
                print('stay on ladder')
                self.velocity.y = 0
                acceleration.y = 0

        acceleration.x = acceleration.x - self.velocity.x * 0.05
        self.velocity = self.velocity + acceleration
        pos_delta = self.velocity + 0.5 * acceleration

        new_pos_dx = pygame.Vector2(self.position.x + pos_delta.x, self.position.y)
        new_pos_dy = pygame.Vector2(self.position.x, self.position.y + pos_delta.y)
        collide_with_wall_by_x = collide_with(self.get_hit_box(new_pos_dx), level1_map, wall_codes)
        collide_with_wall_by_y = collide_with(self.get_hit_box(new_pos_dy), level1_map, wall_codes)

        if collide_with_wall_by_x and collide_with_wall_by_y:
            print("hit to wall by x and y")
            self.velocity.y = 0
            self.velocity.x = 0
        elif collide_with_wall_by_x:
            print("hit to wall by x")
            self.position.y += pos_delta.y
            self.velocity.x = 0
        elif collide_with_wall_by_y:
            print("hit to wall by y")
            self.position.x += pos_delta.x
            self.velocity.y = 0
        else:
            self.position += pos_delta


    def __str__(self):
        return f"pos: {self.position}, vel: {self.velocity}"


map_height_px = len(level1_map) * 24
#hero = Hero(screen.get_width() // 2, start_y + map_height_px - 24 * 2 , 24, 24)
hero = Hero(screen.get_width() // 2, start_y + 24 * 3, 24, 24)

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
    draw_text(1, 1, str(hero))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()