import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        # поле 5 на 7
        board = Board(5, 7)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            board.render(screen)
            pygame.display.flip()

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Клетчатое поле')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    b = Board(50, 50)

    running = True
    x_pos = 0
    y_pos = 0
    v = 100  # пикселей в секунду
    clock = pygame.time.Clock()
    b.render(screen)
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                b.get_click(event.pos)
        b.render(screen)
        pygame.display.flip()
    pygame.quit()
