from random import randint
import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600
WORLD_SIZE = 1000
SCR_CENTER_Y = HEIGHT // 2
SCR_CENTER_X = WIDTH // 2

FPS = 60

BASE_COLOR = pygame.color.Color(255, 255, 255)

BLACK_COLOR = pygame.color.Color(0, 0, 0)


screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

mouse_x, mouse_y = 0, 0

speed = 10
stars = []


def init():
    pygame.init()

    for i in range(2000):
        x = randint(-WORLD_SIZE, WORLD_SIZE)
        y = randint(-WORLD_SIZE, WORLD_SIZE)
        z = randint(1, WORLD_SIZE)
        stars.append((x, y, z))


def to_center(x, y):
    return x + SCR_CENTER_X, y + SCR_CENTER_Y


def draw(screen):
    screen.fill(BLACK_COLOR)

    for x, y, z in stars:
        screen_x, screen_y = to_center(150 / z * x, 150 / z * y)

        color = pygame.color.Color(0, 0, 0)
        v = 100 * (1 - (z / WORLD_SIZE))
        if 0 > v:
            v = 0
        if v > 100:
            v = 100
        base_color_hsva = list(BASE_COLOR.hsva)
        base_color_hsva[2] = v
        color.hsva = base_color_hsva

        pygame.draw.circle(screen, color, (int(screen_x), int(screen_y)), 2)

    pygame.draw.circle(screen, (255, 255, 255), to_center(0, 0), 20, 2)
    pygame.draw.line(screen, (255, 255, 255), to_center(0, -20), to_center(0, 20), 2)
    pygame.draw.line(screen, (255, 255, 255), to_center(-20, 0), to_center(20, 0), 2)

    # Show speed
    font = pygame.font.Font(None, 35)
    speed_label = font.render(f'Speed = {speed}', True, (255, 255, 255))
    screen.blit(speed_label, (10, 0))


def update():
    for i in range(len(stars)):
        x, y, z = stars[i]
        z -= speed
        if z < 1:
            z = WORLD_SIZE
        if z > WORLD_SIZE:
            z = 1
        stars[i] = x, y, z


init()

running = True
while running:
    # внутри игрового цикл еще один цикл приема и обработки сообщений
    events = pygame.event.get()
    for event in events:
        print(f"{event}")
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        elif event.type == pygame.MOUSEWHEEL:
            print(f"{event}, {event.y}")
            speed += event.y * 2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Change color
                BASE_COLOR = pygame.color.Color(randint(0, 255), randint(0, 255), randint(0, 255))
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