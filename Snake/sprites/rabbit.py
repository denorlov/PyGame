from random import randint
import pyanimation

TILE = 50
RABBIT_TILE = 32

class Rabbit:
    def __init__(self, tiles_in_row, tiles_in_col):
        self.x = randint(0, tiles_in_row)
        self.y = randint(0, tiles_in_col)

        self.scr_x = (self.x * TILE) + (TILE - RABBIT_TILE) // 2
        self.scr_y = (self.y * TILE) + (TILE - RABBIT_TILE) // 2
        self.scr_x1 = self.scr_x
        self.scr_y1 = self.scr_y
        self.dx = 0
        self.dy = 0
        self.sit_on_same_place = True

        self.animations = pyanimation.Animation("images/rabbit.png")
        self.animations.sprite_sheet.set_colorkey("#78C380")
        self.animations.sprite_sheet.convert()
        self.animations.create_animation(0, 6, RABBIT_TILE, RABBIT_TILE, "down", duration=80, cols=3, rows=1)
        self.animations.create_animation(0, 6 + RABBIT_TILE, RABBIT_TILE, RABBIT_TILE, "left", duration=80, cols=3, rows=1)
        self.animations.create_animation(0, 6 + RABBIT_TILE * 2, RABBIT_TILE, RABBIT_TILE, "right", duration=80, cols=3, rows=1)
        self.animations.create_animation(0, 6 + RABBIT_TILE * 3, RABBIT_TILE, RABBIT_TILE, "up", duration=80, cols=3,rows=1)

        self.animations.run("down")

    def update(self):
        if self.sit_on_same_place:
            dice = randint(0, 50)
            # start move to sibling cell
            if dice == 0:
                self.sit_on_same_place = False

                self.dx = randint(-1, 1)
                if self.dx == 0:
                    self.dy = randint(-1, 1)
                    if self.dy == -1:
                        self.animations.run("up")
                    else:
                        self.animations.run("down")
                else:
                    self.dy = 0
                    if self.dx == -1:
                        self.animations.run("left")
                    else:
                        self.animations.run("right")

                self.scr_x1 = self.scr_x + self.dx * TILE
                self.scr_y1 = self.scr_y + self.dy * TILE

        if self.sit_on_same_place:
            return

        if self.scr_x == self.scr_x1 and self.scr_y == self.scr_y1:
            self.x += self.dx
            self.y += self.dy
            print(f"scr: {self.scr_x}, {self.scr_y}, cell: {self.x}, {self.y}")
            self.sit_on_same_place = True
            self.animations.run("down")
        else:
            self.scr_x += self.dx * 10
            self.scr_y += self.dy * 10

    def draw(self, screen):
        surface = self.animations.update_surface()
        screen.blit(surface, (self.scr_x, self.scr_y))
