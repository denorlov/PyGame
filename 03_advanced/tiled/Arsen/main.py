import pygame as pygame

from tiled.spritesheet import Spritesheet

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(SCREEN_SIZE)


def draw_text(text, size, color, x, y):
    font_name = pygame.font.match_font('hack')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


level1_map = [
    [202, 202, 202, 202, 202, 202, 202, 202, 202, 202, -1, -1, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202,
     202, 202, 202, 202, 202, 202, 202],
    [202, -1, -1, -1, -1, -1, -1, -1, -1, 202, 202, 202, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, 262],
    [202, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, 262],
    [202, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, 262],
    [261, -1, -1, -1, -1, -1, 133, 223, 223, 223, 223, 223, 223, 223, 223, -1, -1, -1, -1, -1, -1, -1, -1, 202, 202,
     202, 202, 202, 202, 202],
    [261, -1, -1, -1, -1, -1, 133, -1, -1, -1, -1, 223, 223, 223, 223, 132, 132, 223, 202, 202, 202, 202, 202, 202, 202,
     -1, -1, -1, -1, 262],
    [261, -1, -1, -1, -1, -1, 133, -1, -1, -1, -1, -1, -1, -1, -1, 132, 132, 112, 112, 112, 112, 112, 112, 112, 112,
     112, 132, -1, -1, 262],
    [261, -1, -1, -1, -1, -1, 133, -1, -1, -1, -1, -1, -1, -1, -1, 132, 132, -1, -1, -1, -1, -1, -1, -1, -1, -1, 132,
     -1, -1, 262],
    [261, -1, -1, -1, -1, -1, 133, -1, -1, -1, -1, -1, -1, -1, -1, 132, 132, -1, -1, -1, -1, -1, -1, -1, -1, -1, 202,
     202, 202, 202],
    [261, -1, -1, -1, -1, -1, 133, -1, -1, -1, -1, -1, -1, -1, -1, 132, -1, -1, -1, -1, -1, 202, 202, 202, 202, 202,
     202, -1, 202, 202],
    [72, 72, 72, 72, 72, 72, 72, -1, -1, -1, -1, -1, -1, -1, -1, 132, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, 262],
    [261, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 223, 223, 223, 223, 223, 223, 223, 223, 133, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, 262],
    [261, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 133, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, 262],
    [261, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 133, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, 262],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

clock = pygame.time.Clock()

ss = Spritesheet(
    '../assets/tileset3b.png', 24, 24, colorkey=pygame.Color(255, 0, 255)
)

tile_id_to_image = {
    1: ss.image_at(tile_col=1, tile_row=0),
    72: ss.image_at(tile_col=12, tile_row=3)
}

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 255))
    # sprite_sheet.blit_tile(screen, 2, 3, 0, 0)
    for y in range(len(level1_map)):
        for x in range(len(level1_map[0])):
            if level1_map[y][x] == -1:
                continue
            num = level1_map[y][x]
            w, h = num // ss.tile_width, num % ss.tile_height
            color = (0, 255, 255)

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
