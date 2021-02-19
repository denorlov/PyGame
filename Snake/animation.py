import pygame

pygame.init()
screen = pygame.display.set_mode((800, 480))

spritesheet = pygame.image.load("rabbit.png")
spritesheet.convert()  # convert only works afteer display_setmode is set.

background = pygame.Surface((screen.get_size()))
background.fill((255, 255, 255))  # fill white
background = background.convert()

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
animation_phases = [0, 4, 8,  5,  3, 7, 11, 3, 7, 11,  6]
clock = pygame.time.Clock()  # create pygame clock object
FPS = 60

playtime = 0
cycletime = 0

interval = .15  # how long one single images should be displayed in seconds
pic_num = 0

is_running = True
while is_running:
    milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0  # seconds passed since last frame (float)
    playtime += seconds
    cycletime += seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    if cycletime > interval:
        pic = bunny[animation_phases[pic_num]]  ##
        screen.blit(background.subsurface((300, 300, TILE, TILE)), (300, 300))  ##
        screen.blit(pic, (300, 300))
        pic_num += 1
        if pic_num >= len(animation_phases):
            pic_num = 0
        cycletime = 0

        pygame.display.flip()

    pygame.display.set_caption("[FPS]: %.2f picture: %i" % (clock.get_fps(), pic_num))
