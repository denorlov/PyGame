import pygame

TILE = 50

bunny_image = pygame.image.load("bunny.png")
plant_img = pygame.image.load("plant.png")
crystal_img = pygame.image.load("crystal.png")
rock_img = pygame.image.load("rock.png")


snake_img = pygame.image.load("snake-graphics.png")

snake_head_up_img = snake_img.subsurface((64 * 3, 0, 64, 64))
snake_head_up_img = pygame.transform.scale(snake_head_up_img, (TILE, TILE))

snake_head_right_img = snake_img.subsurface((64 * 4, 0, 64, 64))
snake_head_right_img = pygame.transform.scale(snake_head_right_img, (TILE, TILE))

snake_head_left_img = snake_img.subsurface((64 * 3, 64, 64, 64))
snake_head_left_img = pygame.transform.scale(snake_head_left_img, (TILE, TILE))

snake_head_down_img = snake_img.subsurface((64 * 4, 64, 64, 64))
snake_head_down_img = pygame.transform.scale(snake_head_down_img, (TILE, TILE))


snake_tail_up_img = snake_img.subsurface((64 * 3, 64 * 2, 64, 64))
snake_tail_up_img = pygame.transform.scale(snake_tail_up_img, (TILE, TILE))

snake_tail_right_img = snake_img.subsurface((64 * 4, 64 * 2, 64, 64))
snake_tail_right_img = pygame.transform.scale(snake_tail_right_img, (TILE, TILE))

snake_tail_left_img = snake_img.subsurface((64 * 3, 64 + 64 * 2, 64, 64))
snake_tail_left_img = pygame.transform.scale(snake_tail_left_img, (TILE, TILE))

snake_tail_down_img = snake_img.subsurface((64 * 4, 64 + 64 * 2, 64, 64))
snake_tail_down_img = pygame.transform.scale(snake_tail_down_img, (TILE, TILE))


snake_mid_bottom_right_img = snake_img.subsurface((0, 0, 64, 64))
snake_mid_bottom_right_img = pygame.transform.scale(snake_mid_bottom_right_img, (TILE, TILE))

snake_mid_bottom_left_img = snake_img.subsurface((2 * 64, 0, 64, 64))
snake_mid_bottom_left_img = pygame.transform.scale(snake_mid_bottom_left_img, (TILE, TILE))

snake_mid_top_right_img = snake_img.subsurface((0, 1 * 64, 64, 64))
snake_mid_top_right_img = pygame.transform.scale(snake_mid_top_right_img, (TILE, TILE))

snake_mid_top_left_img = snake_img.subsurface((2 * 64, 2 * 64, 64, 64))
snake_mid_top_left_img = pygame.transform.scale(snake_mid_top_left_img, (TILE, TILE))


snake_mid_horizontal_img = snake_img.subsurface((64 * 1, 0, 64, 64))
snake_mid_horizontal_img = pygame.transform.scale(snake_mid_horizontal_img, (TILE, TILE))

snake_mid_vertical_img = snake_img.subsurface((64 * 2, 64 * 1, 64, 64))
snake_mid_vertical_img = pygame.transform.scale(snake_mid_vertical_img, (TILE, TILE))

RABBIT_TILE = 32
rabbit_spritesheet = pygame.image.load("rabbit.png")

bunny_imgs = []  # a list for the bunny images
# the spritesheet has bunny phases, 64 x 64 pixels
for x in range(3):  # first line contains 8 pictures of bunny
    for y in range(4): # 8 lines
        subsurface = rabbit_spritesheet.subsurface(
            0 + RABBIT_TILE * x,
            6 + RABBIT_TILE * y,
            RABBIT_TILE, RABBIT_TILE
        )
        bunny_imgs.append(subsurface)

for n in range(len(bunny_imgs)):
    bunny_imgs[n].set_colorkey(pygame.color.Color("#78C380"))
    #bunny_imgs[n] = pygame.transform.scale(bunny_imgs[n], (TILE, TILE))

bunny_animation_phases = [0, 4, 8,  5, 5, 5, 8, 0, 4, 6, 6, 6, 3, 3, 3, 5, 5, 5]