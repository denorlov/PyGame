import pygame
from random import randint

class Ball:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def move(self, d_y):
        if self.y <= height - self.radius:
            self.y += d_y
        
    def draw(self, scr):
        pygame.draw.circle(scr, self.color, (self.x, self.y), self.radius)


pygame.init()

size = width, height = 400, 300
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 50

running = True
key_pressed = False

balls = []

# real velocity = fps * ball_velocity
ball_velocity = 2
ball_radius = 10

screen2 = pygame.Surface(screen.get_size())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            balls.append(Ball(x, y, (randint(0, 255), randint(0, 255), randint(0, 255)), ball_radius))

    screen2.fill(pygame.Color("black"))
    for ball in balls:
        ball.draw(screen2)
    screen.blit(screen2, (0, 0))

    pygame.display.flip()

    for ball in balls:      
        ball.move(ball_velocity)

    clock.tick(fps)

pygame.quit()