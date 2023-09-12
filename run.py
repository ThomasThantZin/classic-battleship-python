from random import randint

class Board:
    def __init__(self, size):
        self.size = size
        self.water_char = '~'  # Character for water cells
        self.hit_char = 'X'  # Character for hit cells
        self.miss_char = 'O'  # Character for miss cells
        self.ship_char = 'S'  # Character for ship cells
        self.board = [[self.water_char] * size for _ in range(size)]

    def place_ship(self, x, y):
        self.board[x][y] = self.ship_char

    def display(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_location(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size


# Add board size and ship num
BOARD_SIZE = 5
NUM_SHIPS = 4
TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 24

