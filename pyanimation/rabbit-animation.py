from pyanimation import Animation
import pygame

TILE = 32
FPS = 60

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

rabbit = Animation("images/rabbit.png")
rabbit.sprite_sheet.set_colorkey("#78C380")
rabbit.sprite_sheet.convert()
rabbit.create_animation(0, 6, TILE, TILE, "down", duration=120, cols=3, rows=1)
rabbit.create_animation(0, 6 + 2 * TILE, TILE, TILE, "left_right", duration=120, cols=3, rows=1)
rabbit.create_animation(0, 6 + 3 * TILE, TILE, TILE, "up", duration=120, cols=3, rows=1)

rabbit.run("down")
is_in_pause = True

is_running = True
while is_running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

            if event.key == pygame.K_LEFT:
                rabbit.run("left_right")
                rabbit.facing_right = False
                is_in_pause = False
            elif event.key == pygame.K_RIGHT:
                rabbit.run("left_right")
                rabbit.facing_right = True
                is_in_pause = False
            elif event.key == pygame.K_UP:
                rabbit.run("up")
                is_in_pause = False
            elif event.key == pygame.K_DOWN:
                rabbit.run("down")
                is_in_pause = False
            elif event.key == pygame.K_SPACE:
                is_in_pause = not is_in_pause

    if not is_in_pause:
        if rabbit.action_name == "up":
            rabbit.y -= 1
        elif rabbit.action_name == "down":
            rabbit.y += 1
        elif rabbit.action_name == "left_right":
            if rabbit.facing_right:
                rabbit.x += 1
            else:
                rabbit.x -= 1

    screen.fill((0, 0, 0))
    screen.blit(rabbit.update_surface(), (rabbit.x, rabbit.y))
    pygame.display.flip()
    pygame.display.set_caption(f"[FPS]: {clock.get_fps()}")

pygame.quit()