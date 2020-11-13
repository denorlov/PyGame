import random
import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 512, 390

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

running = True

x_mid_pos_shift = 0
x_big_pos_shift = 0
x_small_pos_shift = 0

v_big = 30  # пикселей в секунду
v_mid = 20  # пикселей в секунду
v_small = 10  # пикселей в секунду

FPS = 60

small_stars = []
medium_stars = []
big_stars = []

STARS_COUNT = 30
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

def init():
    for i in range(STARS_COUNT):
        small_stars.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        medium_stars.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        big_stars.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))


def star_coords(x, y, x_offset = 0, y_offset = 0):
    return (x + x_offset if x + x_offset < WIDTH else (x + x_offset) - WIDTH,
            y + y_offset if y + y_offset < HEIGHT else (y + y_offset) - HEIGHT)

def new_x_offset(x, velocity = 0):
    x += velocity / FPS
    if x > WIDTH:
        x = 0
    return x


def draw(screen):
    global x_small_pos_shift, x_mid_pos_shift, x_big_pos_shift

    screen.fill((0, 0, 0))

    for i in range(STARS_COUNT):
        x, y = star_coords(*small_stars[i], x_offset=x_small_pos_shift)
        pygame.draw.circle(screen, WHITE_COLOR, (x, y), 1)

        x, y = star_coords(*medium_stars[i], x_offset=x_mid_pos_shift)
        pygame.draw.circle(screen, WHITE_COLOR, (x, y), 3)

        x, y = star_coords(*big_stars[i], x_offset=x_big_pos_shift)
        pygame.draw.circle(screen, WHITE_COLOR, (x, y), 7)

    pygame.draw.circle(screen, WHITE_COLOR, (WIDTH // 2, HEIGHT // 2), 20, width = 2)

    x_big_pos_shift = new_x_offset(x_big_pos_shift, v_big)
    x_mid_pos_shift = new_x_offset(x_mid_pos_shift, v_mid)
    x_small_pos_shift = new_x_offset(x_small_pos_shift, v_small)


init()

while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                v_mid = v_mid * 2 if v_mid < 0 else -10
                v_small = v_mid * 2 if v_small < 0 else -20
                v_big = v_mid * 2 if v_small < 0 else -30
            elif event.key == pygame.K_RIGHT:
                v_mid = v_mid * 2 if v_mid > 0 else 10
                v_small = v_mid * 2 if v_small > 0 else 20
                v_big = v_mid * 2 if v_small > 0 else 30

    # отрисовка и изменение свойств объектов
    draw(screen)

    # пауза на 1 / fps cek
    clock.tick(FPS)

    # обновление экрана
    pygame.display.flip()

pygame.quit()