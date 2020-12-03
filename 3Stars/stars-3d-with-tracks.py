from math import cos, sin
from random import randint
import pygame
from pygame.font import Font

WHITE = (255, 255, 255)

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720
WORLD_SIZE = 1000
SCR_CENTER_Y = HEIGHT // 2
SCR_CENTER_X = WIDTH // 2

FPS = 60

BASE_COLOR = pygame.color.Color(0, 255, 0)
BASE_COLOR_H, BASE_COLOR_S, BASE_COLOR_V, BASE_COLOR_A = BASE_COLOR.hsva

font = None

print(BASE_COLOR)
print(BASE_COLOR.hsva)
print(BASE_COLOR_H, BASE_COLOR_S, BASE_COLOR_V, BASE_COLOR_A)

BLACK_COLOR = pygame.color.Color(0, 0, 0)


screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

mouse_x, mouse_y = 0, 0

speed = 1
speed_of_roll = 0.01
# x, y, z
stars = []
# x, y, z
stars_prev = []

def init():
    global font, stars, stars_prev

    pygame.init()
    font = Font(None, 24)

    pygame.mixer.music.load('eduard-artemev-polet.mp3')
    #pygame.mixer.music.play()

    for i in range(7000):
        x = randint(-WORLD_SIZE, WORLD_SIZE)
        y = randint(-WORLD_SIZE, WORLD_SIZE)
        z = randint(1, WORLD_SIZE)
        stars.append((x, y, z))
        stars_prev.append((x, y, z))

def to_center(x, y):
    return x + SCR_CENTER_X, y + SCR_CENTER_Y

def projection(x, y, z):
    screen_x = 50 / z * x
    screen_y = 50 / z * y
    return screen_x, screen_y

def rotation(x, y, angel):
    x1 = x * cos(angel) - y * sin(angel)
    y1 = x * sin(angel) + y * cos(angel)
    return x1, y1


def draw(screen):
    screen.fill(BLACK_COLOR)

    for i in range(len(stars)):
        x, y, z = stars[i]
        screen_x, screen_y = to_center(*projection(x, y, z))

        x, y, z = stars_prev[i]
        prev_screen_x, prev_screen_y = to_center(*projection(x, y, z))

        color = pygame.color.Color(0, 0, 0)
        v = 100 * (1 - (z / WORLD_SIZE))
        if 0 > v:
            v = 0
        if v > 100:
            v = 100
        color.hsva = BASE_COLOR_H, BASE_COLOR_S, v, BASE_COLOR_A

        #pygame.draw.circle(screen, color, (screen_x, screen_y), 2)
        pygame.draw.line(screen, color, (screen_x, screen_y), (prev_screen_x, prev_screen_y), 2)

    pygame.draw.circle(screen, WHITE, to_center(0, 0), 25, 2)
    pygame.draw.line(screen, WHITE, to_center(0, -25), to_center(0, +25), 2)
    pygame.draw.line(screen, WHITE, to_center(-25, 0), to_center(+25, 0), 2)

    text_surf = font.render(f"speed: {speed}, speed_of_roll: {speed_of_roll}", 1, WHITE)
    screen.blit(text_surf, (5, 5))


def update():
    global speed
    global speed_of_roll

    speed = (SCR_CENTER_Y - mouse_y) / 50
    speed_of_roll = (SCR_CENTER_X - mouse_x) / 50000

    for i in range(len(stars)):
        x, y, z = stars[i]
        stars_prev[i] = x, y, z
        z = z - speed
        if z < 1:
            z = WORLD_SIZE
            stars_prev[i] = x, y, z
        x, y = rotation(x, y, speed_of_roll)
        stars[i] = x, y, z



init()

running = True
while running:
    # внутри игрового цикл еще один цикл приема и обработки сообщений
    events = pygame.event.get()
    for event in events:
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        elif event.type == pygame.KEYDOWN:
            # нажата влево
            if event.key == pygame.K_LEFT:
                pass
            # нажата вправо
            if event.key == pygame.K_RIGHT:
                pass
            # нажата вниз
            if event.key == pygame.K_DOWN:
                pass
            # нажата вверх
            if event.key == pygame.K_UP:
                pass

    # отрисовка объектов
    draw(screen)

    # изменение свойств объектов
    update()

    # пауза на 1 / FPS cek
    clock.tick(FPS)

    # обновление экрана
    pygame.display.flip()

pygame.quit()