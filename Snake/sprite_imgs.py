import pygame

TILE = 50

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


snake_mid_horizontal_img = snake_img.subsurface((64 * 1, 0, 64, 64))
snake_mid_horizontal_img = pygame.transform.scale(snake_mid_horizontal_img, (TILE, TILE))

snake_mid_vertical_img = snake_img.subsurface((64 * 2, 64 * 1, 64, 64))
snake_mid_vertical_img = pygame.transform.scale(snake_mid_vertical_img, (TILE, TILE))
