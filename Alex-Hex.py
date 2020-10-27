import pygame as pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 40, 255)
RED = (255, 0, 0)


def draw(screen):
    screen.fill(BLUE)
    pygame.draw.polygon(screen, WHITE, [[225, 600], [275, 600], [300, 650], [275, 700], [225, 700], [200, 650]])
    pygame.draw.polygon(screen, WHITE, [[325, 600], [375, 600], [400, 650], [375, 700], [325, 700], [300, 650]])
    pygame.draw.polygon(screen, WHITE, [[425, 600], [475, 600], [500, 650], [475, 700], [425, 700], [400, 650]])
    pygame.draw.polygon(screen, WHITE, [[525, 600], [575, 600], [600, 650], [575, 700], [525, 700], [500, 650]])

    pygame.draw.polygon(screen, WHITE, [[175, 500], [225, 500], [250, 550], [225, 600], [175, 600], [150, 550]])
    pygame.draw.polygon(screen, WHITE, [[275, 500], [325, 500], [350, 550], [325, 600], [275, 600], [250, 550]])
    pygame.draw.polygon(screen, WHITE, [[375, 500], [425, 500], [450, 550], [425, 600], [375, 600], [350, 550]])
    pygame.draw.polygon(screen, WHITE, [[475, 500], [525, 500], [550, 550], [525, 600], [475, 600], [450, 550]])
    pygame.draw.polygon(screen, WHITE, [[575, 500], [625, 500], [650, 550], [625, 600], [575, 600], [550, 550]])

    pygame.draw.polygon(screen, WHITE, [[225, 400], [275, 400], [300, 450], [275, 500], [225, 500], [200, 450]])
    pygame.draw.polygon(screen, WHITE, [[325, 400], [375, 400], [400, 450], [375, 500], [325, 500], [300, 450]])
    pygame.draw.polygon(screen, WHITE, [[425, 400], [475, 400], [500, 450], [475, 500], [425, 500], [400, 450]])
    pygame.draw.polygon(screen, WHITE, [[525, 400], [575, 400], [600, 450], [575, 500], [525, 500], [500, 450]])

    pygame.draw.polygon(screen, WHITE, [[175, 300], [225, 300], [250, 350], [225, 400], [175, 400], [150, 350]])
    pygame.draw.polygon(screen, WHITE, [[275, 300], [325, 300], [350, 350], [325, 400], [275, 400], [250, 350]])
    pygame.draw.polygon(screen, WHITE, [[375, 300], [425, 300], [450, 350], [425, 400], [375, 400], [350, 350]])
    pygame.draw.polygon(screen, WHITE, [[475, 300], [525, 300], [550, 350], [525, 400], [475, 400], [450, 350]])
    pygame.draw.polygon(screen, WHITE, [[575, 300], [625, 300], [650, 350], [625, 400], [575, 400], [550, 350]])

    pygame.draw.polygon(screen, WHITE, [[225, 200], [275, 200], [300, 250], [275, 300], [225, 300], [200, 250]])
    pygame.draw.polygon(screen, WHITE, [[325, 200], [375, 200], [400, 250], [375, 300], [325, 300], [300, 250]])
    pygame.draw.polygon(screen, WHITE, [[425, 200], [475, 200], [500, 250], [475, 300], [425, 300], [400, 250]])
    pygame.draw.polygon(screen, WHITE, [[525, 200], [575, 200], [600, 250], [575, 300], [525, 300], [500, 250]])

    pygame.draw.polygon(screen, WHITE, [[175, 100], [225, 100], [250, 150], [225, 200], [175, 200], [150, 150]])
    pygame.draw.polygon(screen, WHITE, [[275, 100], [325, 100], [350, 150], [325, 200], [275, 200], [250, 150]])
    pygame.draw.polygon(screen, WHITE, [[375, 100], [425, 100], [450, 150], [425, 200], [375, 200], [350, 150]])
    pygame.draw.polygon(screen, WHITE, [[475, 100], [525, 100], [550, 150], [525, 200], [475, 200], [450, 150]])
    pygame.draw.polygon(screen, WHITE, [[575, 100], [625, 100], [650, 150], [625, 200], [575, 200], [550, 150]])

    pygame.draw.polygon(screen, WHITE, [[225, 0], [275, 0], [300, 50], [275, 100], [225, 100], [200, 50]])
    pygame.draw.polygon(screen, WHITE, [[325, 0], [375, 0], [400, 50], [375, 100], [325, 100], [300, 50]])
    pygame.draw.polygon(screen, WHITE, [[425, 0], [475, 0], [500, 50], [475, 100], [425, 100], [400, 50]])
    pygame.draw.polygon(screen, WHITE, [[525, 0], [575, 0], [600, 50], [575, 100], [525, 100], [500, 50]])

    pygame.draw.circle(screen, BLACK, (400, 350), 40)
    pygame.draw.circle(screen, RED, (250, 650), 40)
    pygame.draw.circle(screen, RED, (350, 650), 40)
    pygame.draw.circle(screen, RED, (450, 650), 40)
    pygame.draw.circle(screen, RED, (550, 650), 40)
    pygame.draw.circle(screen, RED, (400, 550), 40)



width, height = 800, 700
screen = pygame.display.set_mode((width, height))
draw(screen)

eventType = pygame.event.wait().type
draw(screen)
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    draw(screen)
    pygame.display.flip()
pygame.quit()