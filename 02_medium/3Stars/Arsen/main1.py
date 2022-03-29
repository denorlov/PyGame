from math import cos, sin, sqrt
from random import random, randint
import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

BASE_COLOR = pygame.color.Color(255, 255, 0)
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
FPS = 50

stars_positions = []
old_stars_positions = []

draw_clock = pygame.time.Clock()


def init():
    global FONT

    pygame.init()
    FONT = pygame.font.Font(None, 22)

    for i in range(2000):
        x, y, z = randint(-WORLD_SIZE, WORLD_SIZE), \
                  randint(-WORLD_SIZE, WORLD_SIZE), \
                  randint(1, WORLD_SIZE)
        stars_positions.append((x, y, z))
        old_stars_positions.append((x, y, z))

    pygame.mixer.init()
    pygame.mixer.music.load('eduard-artemev-polet.mp3')
    pygame.mixer.music.play()


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
    global delta_time

    screen.fill((0, 0, 0))

    for i in range(len(stars_positions)):
        star_xyz = stars_positions[i]

        color = pygame.color.Color(0, 0, 0)
        v = 100 * (1 - (star_xyz[2] / WORLD_SIZE))
        v = 100 if v > 100 else v
        v = 0 if v < 0 else v
        color.hsva = BASE_COLOR_H, BASE_COLOR_S, v, BASE_COLOR_A

        star_screen_x, star_screen_y = to_center(*perspective_transform(*star_xyz))
        pygame.draw.circle(screen, color, (int(star_screen_x), int(star_screen_y)), 2)
        old_star_screen_x, old_star_screen_y = to_center(*perspective_transform(*old_stars_positions[i]))

        if abs(old_stars_positions[i][2] - stars_positions[i][2]) < 30:
            pygame.draw.line(screen, color, (old_star_screen_x, old_star_screen_y), (star_screen_x, star_screen_y), 2)

    # Crosshair
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

    for i in range(len(stars_positions)):
        old_stars_positions[i] = stars_positions[i]
        x, y, z = stars_positions[i]

        x, y = rotation(x, y, angle)
        z -= speed

        if z < 1:
            z = WORLD_SIZE

        if z > WORLD_SIZE:
            z = 1

        stars_positions[i] = x, y, z


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
            if event.key == pygame.K_UP:
                # Change color
                BASE_COLOR = pygame.color.Color(randint(0, 255), randint(0, 255),
                                                randint(0, 255))
                BASE_COLOR_H, BASE_COLOR_S, BASE_COLOR_V, BASE_COLOR_A = BASE_COLOR.hsva
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
