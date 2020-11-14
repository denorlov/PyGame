from random import random, randint
import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

FPS = 60

velocity = 30 # points / sec

velocity_small = velocity # points / sec
velocity_mid = velocity * 1.5 # points / sec
velocity_big = velocity * 2 # points / sec

x_offset_small = 0
x_offset_mid = 0
x_offset_big = 0

big_stars = []
medium_stars = []
small_stars = []


def coords(x_y, x_offset=0, y_offset=0):
    x, y = x_y

    if x_y[0] + x_offset > WIDTH:
        x = x + x_offset - WIDTH
    else:
        x = x_y[0] + x_offset

    if y > HEIGHT:
        y = y + y_offset - HEIGHT
    else:
        y = x_y[1] + y_offset

    return x, y


def change_offset(x_offset, velocity):
    x_offset = x_offset + (velocity / FPS)
    if x_offset > WIDTH:
        x_offset = 0
    return x_offset



def init():
    pygame.init()

    for i in range(100):
        big_star_x_y = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
        big_stars.append(big_star_x_y)
        med_stars_x_y = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
        medium_stars.append(med_stars_x_y)
    for i in range(300):
        small_stars.append((randint(0, WIDTH - 1), randint(0, HEIGHT - 1)))


def draw(screen):
    global x_offset_small, x_offset_mid, x_offset_big

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (WIDTH // 2, HEIGHT // 2), 30, 2)

    x_offset_big = change_offset(x_offset_big, velocity_big)
    x_offset_mid = change_offset(x_offset_mid, velocity_mid)
    x_offset_small = change_offset(x_offset_small, velocity_small)

    for star_xy in big_stars:
        pygame.draw.circle(screen, (255, 255, 255), coords(star_xy, x_offset_big), 7)

    for star_xy in medium_stars:
        pygame.draw.circle(screen, (255, 255, 255), coords(star_xy, x_offset_mid), 3)

    for star_xy in small_stars:
        pygame.draw.circle(screen, (255, 255, 255), coords(star_xy, x_offset_small), 1)



init()

running = True


def on_key_left():
    global velocity_big, velocity_small, velocity_mid

    velocity_big = -(velocity * 2) if velocity_big > 0 else velocity_big * 2

    if velocity_mid > 0:
        velocity_mid = -(velocity * 1.5)
    else:
        velocity_mid *= 2

    if velocity_small > 0:
        velocity_small = -(velocity * 1)
    else:
        velocity_small *= 2


def on_key_right():
    global velocity_big, velocity_small, velocity_mid
    velocity_big *= 2
    velocity_small *=2
    velocity_mid *=2



def on_key_down():
    pass

def on_key_up():
    pass


while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    events = pygame.event.get()
    for event in events:
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
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

    # отрисовка и изменение свойств объектов
    draw(screen)

    # пауза на 1 / FPS cek
    clock.tick(FPS)

    # обновление экрана
    pygame.display.flip()

pygame.quit()