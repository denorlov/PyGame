import pygame as pygame
import csv

from tiled.spritesheet import Spritesheet

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(SCREEN_SIZE, flags=pygame.FULLSCREEN)


def draw_text(text, size, color, x, y):
    font_name = pygame.font.match_font('hack')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


level1_map = []
with open('../assets/5.csv') as f:
    reader = csv.reader(f)
    for i in reader:
        level1_map.append([int(j) for j in i])

clock = pygame.time.Clock()

ss = Spritesheet(
    '../assets/tileset3b.png', 24, 24, colorkey=pygame.Color(255, 0, 255)
)

tile_id_to_image = {
}

indexes = set()
for i in level1_map:
    indexes = indexes.union(set(i))
print(indexes)
for i in indexes:
    if i not in tile_id_to_image:
        row = i // 20
        col = i % 20
        tile_id_to_image[i] = ss.image_at(tile_col=col, tile_row=row)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 0))
    # sprite_sheet.blit_tile(screen, 2, 3, 0, 0)
    for y in range(len(level1_map)):
        for x in range(len(level1_map[0])):
            if level1_map[y][x] == -1:
                continue
            num = level1_map[y][x]
            w, h = num // ss.tile_width, num % ss.tile_height
            color = (0, 0, 0)

            if num in tile_id_to_image:
                img = tile_id_to_image[num]
                screen.blit(
                    img,
                    (x * ss.tile_width, y * ss.tile_height, ss.tile_width, ss.tile_height)
                )
            else:
                pygame.draw.rect(
                    screen, color,
                    (x * ss.tile_width, y * ss.tile_height, ss.tile_width, 24),
                    1
                )

            draw_text(
                str(num), 20, (255, 255, 255),
                x * ss.tile_width, y * ss.tile_height
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()