import pygame

def draw_square():
    color = pygame.Color(150, 150, 50)
    # рисуем "тень"
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva
    # увеличиваем параметр Value, который влияет на яркость
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    # рисуем сам объект
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()
draw_square()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()
