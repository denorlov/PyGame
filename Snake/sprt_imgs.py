import pygame

TILE = 50

bunny_image = pygame.image.load("bunny.png")
plant_image = pygame.image.load("plant.png")
ice_image = pygame.image.load("crystal.png")
rock_image = pygame.image.load("rock.png")

snake_grapichs = pygame.image.load("snake-graphics.png")

snake_head_up = snake_grapichs.subsurface((64 * 3, 0, 64, 64))
snake_head_up = pygame.transform.scale(snake_head_up, (TILE, TILE))

snake_head_down = snake_grapichs.subsurface((64 * 4, 64, 64, 64))
snake_head_down = pygame.transform.scale(snake_head_down, (TILE, TILE))

snake_head_right = snake_grapichs.subsurface((64 * 4, 0, 64, 64))
snake_head_right = pygame.transform.scale(snake_head_right, (TILE, TILE))

snake_head_left = snake_grapichs.subsurface((64 * 3, 64, 64, 64))
snake_head_left = pygame.transform.scale(snake_head_left, (TILE, TILE))


snake_tail_up = snake_grapichs.subsurface((64 * 4, 64 * 3, 64, 64))
snake_tail_up = pygame.transform.scale(snake_tail_up, (TILE, TILE))

snake_tail_down = snake_grapichs.subsurface((64 * 3, 64 * 2, 64, 64))
snake_tail_down = pygame.transform.scale(snake_tail_down, (TILE, TILE))

snake_tail_right = snake_grapichs.subsurface((64 * 3, 64 * 3, 64, 64))
snake_tail_right = pygame.transform.scale(snake_tail_right, (TILE, TILE))

snake_tail_left = snake_grapichs.subsurface((64 * 4, 64 * 2, 64, 64))
snake_tail_left = pygame.transform.scale(snake_tail_left, (TILE, TILE))
