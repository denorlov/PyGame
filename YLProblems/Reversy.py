import pygame, random

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[random.choice([0, 1]) for i in range(width)] for _ in range(height)]
        print(self.board)
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.n = 0

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
                if self.board[y][x] == 0:
                    pygame.draw.ellipse(screen, pygame.Color(0, 0, 255), (
                        x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 2,
                        self.cell_size - 2, self.cell_size - 2))

                elif self.board[y][x] == 1:
                    pygame.draw.ellipse(screen, pygame.Color(255, 0, 0), (
                        x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 2,
                        self.cell_size - 2, self.cell_size - 2))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell_coords):
        for i in range(self.height):
            self.board[i][cell_coords[1]] = self.board[cell_coords[0]][cell_coords[1]]

        for i in range(self.width):
            self.board[cell_coords[0]][i] = self.board[cell_coords[0]][cell_coords[1]]

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[1] < self.left + self.height * self.cell_size and self.top <= \
                mouse_pos[0] < self.top + self.width * self.cell_size:
            return (int((mouse_pos[1] - self.left) / self.cell_size),
                    int((mouse_pos[0] - self.top) / self.cell_size))
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)


board = Board(5, 7)
board.set_view(100, 100, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
