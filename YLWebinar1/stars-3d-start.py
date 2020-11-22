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

speed = 0
stars = []

def init():
    global font

    pygame.init()
    font = Font(None, 24)


    for i in range(10000):
        x = randint(-WORLD_SIZE, WORLD_SIZE)
        y = randint(-WORLD_SIZE, WORLD_SIZE)
        z = randint(1, WORLD_SIZE)
        stars.append((x, y, z))


def to_center(x, y):
    return x + SCR_CENTER_X, y + SCR_CENTER_Y

def draw(screen):
    screen.fill(BLACK_COLOR)

    for star_xyz in stars:
        x, y, z = star_xyz
        screen_x, screen_y = to_center(100 / z * x, 100 / z * y)
        #screen_x, screen_y = to_center(x, y)

        color = pygame.color.Color(0, 0, 0)
        v = 100 * (1 - (z / WORLD_SIZE))
        if 0 > v:
            v = 0
        if v > 100:
            v = 100
        color.hsva = BASE_COLOR_H, BASE_COLOR_S, v, BASE_COLOR_A

        pygame.draw.circle(screen, color, (screen_x, screen_y), 2)

    pygame.draw.circle(screen, WHITE, to_center(0, 0), 20, 2)
    pygame.draw.line(screen, WHITE, to_center(0, -20), to_center(0, +20), 2)
    pygame.draw.line(screen, WHITE, to_center(-20, 0), to_center(+20, 0), 2)

    text_surf = font.render(f"speed: {speed}", 1, WHITE)
    screen.blit(text_surf, (5, 5))


def update():
    global speed

    speed = (SCR_CENTER_Y - mouse_y) / 50

    for i in range(len(stars)):
        x, y, z = stars[i]
        z = z - speed
        if z < 1:
            z = WORLD_SIZE
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