import pygame

pygame.init()
screen = pygame.display.set_mode((800, 480))

spritesheet = pygame.image.load("../Snake/images/rabbit.png")
#spritesheet.convert()  # convert only works after display_setmode is set.

background = pygame.Surface((screen.get_size()))
background.fill((255, 255, 255))  # fill white

screen.blit(background, (0, 0))

TILE = 32

bunny = []  # a list for the bunny images
# the spritesheet has bunny phases, 64 x 64 pixels
for x in range(3):  # first line contains 8 pictures of bunny
    for y in range(4): # 8 lines
        bunny.append(spritesheet.subsurface(0 + TILE * x, 6 + TILE * y, TILE, TILE))

for n in range(len(bunny)):
    bunny[n].set_colorkey(pygame.color.Color("#78C380"))
    bunny[n] = bunny[n].convert_alpha()

for x in range(3):  # first line contains 8 pictures of bunny
    for y in range(4): # 8 lines
        screen.blit(bunny[x + y * 3], (x * 1.5 * TILE, y * 1.5 * TILE))

#animation_phases = [0, 4, 8,  5, 9, 1,  5, 9, 1]
#animation_phases = [0, 4, 8,  5, 9, 1,  6, 2, 10,  3, 7, 11]
#animation_phases = [0, 4, 8,  5,  3, 7, 11, 3, 7, 11,  6]
animation_phases = [0, 4, 8,  5, 5, 5, 8, 0, 4, 6, 6, 6, 3, 3, 3, 5, 5, 5]

FPS = 60
clock = pygame.time.Clock()  # create pygame clock object
cycletime = 0
interval = .5  # how long one single images should be displayed in seconds
animation_phase_num = 0

is_running = True
while is_running:
    milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0  # seconds passed since last frame (float)
    cycletime += seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    if cycletime > interval:
        pic = bunny[animation_phases[animation_phase_num]]
        screen.blit(background.subsurface((300, 300, TILE, TILE)), (300, 300))
        screen.blit(pic, (300, 300))

        animation_phase_num += 1
        if animation_phase_num >= len(animation_phases):
            animation_phase_num = 0
        cycletime = 0

        pygame.display.flip()

    pygame.display.set_caption("[FPS]: %.2f picture: %i" % (clock.get_fps(), animation_phase_num))
