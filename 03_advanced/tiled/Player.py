from pyanimation import Animation
from consts import *

player_anim = Animation(image_path="./assets/player1m.png")
player_anim.create_animation(
    0, 0,
    sprite_width=24,
    sprite_height=192//8,
    action_name="run",
    duration=20,
    rows=2, cols=9
)


class Player:
    def __init__(self, x, y, widht, height):
        self.rect = pygame.Rect(x, y, widht, height)
        self.vx = 0
        self.vy = 0

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN_COLOR, self.rect)

    def update(self, events):
        self.vx = 0
        self.vy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vx = 5
        elif keys[pygame.K_LEFT]:
            self.vx = -5

        if keys[pygame.K_UP]:
            self.vy = -5
        elif keys[pygame.K_DOWN]:
            self.vy = 5

        self.rect.x = self.rect.x + self.vx
        self.rect.y = self.rect.y + self.vy

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Player({self.x}, {self.y}, {self.dx}, {self.dy})"
