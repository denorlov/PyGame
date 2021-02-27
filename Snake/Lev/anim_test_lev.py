import pygame

pygame.init()
screen = pygame.display.set_mode((800, 480))

FPS = 60
clock = pygame.time.Clock()  # create pygame clock object

sprite_sheet = pygame.image.load("../rabbit.png")

TILE = 32

rabbit_animations = []
animations_seq_left = [1, 5, 9]
animations_seq = [6, 6, 2, 10, 6, 6, 7, 7, 5, 5, 1, 9, 5, 5, 4, 4] #0, 4, 8,  5, 5, 5, 8, 0, 4, 6, 6, 6, 3, 3, 3, 5, 5, 5
current_phase = 0

for x in range(3):
    for y in range(4):
        rabit_sprite = sprite_sheet.subsurface(
            (0 + (x + 9) * TILE, 6 + y * TILE, TILE, TILE)
        )
        rabbit_animations.append(rabit_sprite)

phase_interval_sec = 0.2
cycle_time_sec = 0

is_running = True
while is_running:
    millis_since_prev_frame = clock.tick(FPS) # milliseconds passed since last frame
    secs_since_prev_frame = millis_since_prev_frame / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    screen.fill((0, 0, 0))

    for i, anim in enumerate(rabbit_animations):
        screen.blit(anim, (100 + i * (TILE + 10), 100))

    rabbit_phase_idx = animations_seq[current_phase]
    rabbit_phase = rabbit_animations[rabbit_phase_idx]
    screen.blit(rabbit_phase, (200, 200))

    cycle_time_sec += secs_since_prev_frame
    if cycle_time_sec > phase_interval_sec:
        current_phase += 1
        if current_phase >= len(animations_seq):
            current_phase = 0
        cycle_time_sec = 0

    pygame.display.flip()
    pygame.display.set_caption(f"[FPS]: {clock.get_fps()}")

pygame.quit()
