from math import cos, sin
from random import random, randint
import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

BASE_COLOR = pygame.color.Color(0, 255, 0)
BASE_COLOR_H, BASE_COLOR_S, BASE_COLOR_V, BASE_COLOR_A = BASE_COLOR.hsva

WORLD_SIZE = 1000
DISTANCE_TO_VIEWING_PLANE = 200

FONT = None

mouse_x, mouse_y = (0, 0)
is_space_pressed = False

speed = 2
angle = 0.01

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
FPS = 60

stars = []
stars_prev = []


def init():
    global FONT

    pygame.init()
    FONT = pygame.font.Font(None, 22)

    for i in range(2000):
        x, y, z = randint(-WORLD_SIZE, WORLD_SIZE), \
                  randint(-WORLD_SIZE, WORLD_SIZE), \
                  randint(1, WORLD_SIZE)
        stars.append((x, y, z))
        stars_prev.append((x, y, z))


def perspective_transform(x, y, z):
    x_plane = 0 if z * x == 0 else DISTANCE_TO_VIEWING_PLANE / z * x
    y_plane = 0 if z * x == 0 else DISTANCE_TO_VIEWING_PLANE / z * y
    return x_plane, y_plane


def to_center(x, y):
    return x + WIDTH // 2, y + HEIGHT // 2


def rotation(x, y, angle):
    x1 = x * cos(angle) - y * sin(angle)
    y1 = x * sin(angle) + y * cos(angle)
    return x1, y1


def draw(screen):
    screen.fill((0, 0, 0))

    for i in range(len(stars)):
        star_xyz = stars[i]
        prev_star_xyz = stars_prev[i]

        color = pygame.color.Color(0, 0, 0)
        v = 100 * (1 - (star_xyz[2] / WORLD_SIZE))
        v = 100 if v > 100 else v
        v = 0 if v < 0 else v
        color.hsva = BASE_COLOR_H, BASE_COLOR_S, v, BASE_COLOR_A

        star_screen_x, star_screen_y = to_center(*perspective_transform(*star_xyz))
        prev_star_screen_x, prev_star_screen_y = to_center(*perspective_transform(*prev_star_xyz))

        #pygame.draw.circle(screen, color, (int(star_screen_x), int(star_screen_y)), 2)
        pygame.draw.line(screen, color,
                         (int(star_screen_x), int(star_screen_y)),
                         (int(prev_star_screen_x), int(prev_star_screen_y)),
                         2)


    pygame.draw.circle(screen, (255, 255, 255), to_center(0, 0), 20, 2)
    pygame.draw.line(screen, (255, 255, 255), to_center(0, -30), to_center(0, +30), 2)
    pygame.draw.line(screen, (255, 255, 255), to_center(-30, 0), to_center(+30, 0), 2)

    debug_text = FONT.render(f'speed: {speed}, angle: {angle}', 1, (255, 255, 255))
    screen.blit(debug_text, (5, 5))


def update():
    global speed, angle
    speed = ((HEIGHT // 2) - mouse_y) // 20

    if is_space_pressed:
        speed = speed * 2

    angle = ((WIDTH // 2) - mouse_x) / 10000

    if is_space_pressed:
        angle = angle * 2


    for i in range(len(stars)):
        x, y, z = stars[i]

        stars_prev[i] = x, y, z

        x, y = rotation(x, y, angle)
        z = z - speed

        if z < 1:
            z = WORLD_SIZE
            stars_prev[i] = x, y, z

        if z > WORLD_SIZE:
            z = 1
            stars_prev[i] = x, y, z

        stars[i] = x, y, z


init()

running = True

while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    events = pygame.event.get()
    for event in events:
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_space_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_space_pressed = False

    # отрисовка объектов
    draw(screen)

    # изменение свойств объектов
    update()

    # пауза на 1 / FPS cek
    clock.tick(FPS)

    # обновление экрана
    pygame.display.flip()

pygame.quit()