from random import random, randint
import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

BASE_COLOR = pygame.color.Color(0, 255, 0)
BASE_COLOR_H, BASE_COLOR_S, BASE_COLOR_V, BASE_COLOR_A = BASE_COLOR.hsva

WORLD_SIZE = 1000
DISTANCE_TO_VIEWING_PLANE = 100

FONT = None

mouse_x, mouse_y = (0, 0)
speed = 2

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

FPS = 60

stars = []


def init():
    global FONT

    pygame.init()
    FONT = pygame.font.Font(None, 18)

    for i in range(1000):
        x, y, z = randint(-WORLD_SIZE, WORLD_SIZE), \
                  randint(-WORLD_SIZE, WORLD_SIZE), \
                  randint(1, WORLD_SIZE)
        stars.append((x, y, z))


def perspective_transform(x, y, z):
    x_plane = 0 if z * x == 0 else DISTANCE_TO_VIEWING_PLANE / z * x
    y_plane = 0 if z * x == 0 else DISTANCE_TO_VIEWING_PLANE / z * y
    return x_plane, y_plane


def to_center(x, y):
    return x + WIDTH // 2, y + HEIGHT // 2
20

def draw(screen):
    screen.fill((0, 0, 0))

    for star_xyz in stars:
        color = pygame.color.Color(0, 0, 0)
        v = 100 * (1 - (star_xyz[2] / WORLD_SIZE))
        v = 100 if v > 100 else v
        v = 0 if v < 0 else v
        color.hsva = BASE_COLOR_H, BASE_COLOR_S, v, BASE_COLOR_A
        pygame.draw.circle(screen, color, to_center(*perspective_transform(*star_xyz)), 2)

    pygame.draw.circle(screen, (255, 255, 255), to_center(0, 0), 20, 2)
    pygame.draw.line(screen, (255, 255, 255), to_center(0, -30), to_center(0, +30), 2)
    pygame.draw.line(screen, (255, 255, 255), to_center(-30, 0), to_center(+30, 0), 2)

    debug_text = FONT.render(f'spd: {speed}', 1, (255, 255, 255))
    screen.blit(debug_text, (5, 5))


def update():
    global speed
    speed = ((HEIGHT // 2) - mouse_y) // 20

    for i in range(len(stars)):
        x, y, z = stars[i]
        z = z - speed
        stars[i] = x, y, WORLD_SIZE if z < 1 else z

def on_key_left():
    pass

def on_key_right():
    pass

def on_key_down():
    pass

def on_key_up():
    pass


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
            if event.key == pygame.K_LEFT:
                #нажата влево
                on_key_left()
            if event.key == pygame.K_RIGHT:
                # нажата вправо
                on_key_right()
            if event.key == pygame.K_DOWN:
                # нажата вниз
                on_key_down()
            if event.key == pygame.K_UP:
                # нажата вверх
                on_key_up()

    # отрисовка объектов
    draw(screen)

    # изменение свойств объектов
    update()

    # пауза на 1 / FPS cek
    clock.tick(FPS)

    # обновление экрана
    pygame.display.flip()

pygame.quit()