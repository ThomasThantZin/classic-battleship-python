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

# Initialize the player and computer boards
player_board = Board(BOARD_SIZE)
computer_board = Board(BOARD_SIZE)

# Place ships on the computer board randomly
def place_computer_ships(board):
    for _ in range(NUM_SHIPS):
        x, y = randint(0, BOARD_SIZE - 1), randint(0, BOARD_SIZE - 1)
        board.place_ship(x, y)

# Function to randomly place the player's ships
def place_player_ships(board):
    print("\nRandomly placing your ships:")
    for _ in range(NUM_SHIPS):
        while True:
            x = randint(0, BOARD_SIZE - 1)
            y = randint(0, BOARD_SIZE - 1)
            if board.board[x][y] != board.ship_char:
                board.place_ship(x, y)
                break

# Check if the player's guess is valid
def is_valid_guess(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

# Display the game boards 
def display_boards(player_name):
    print(f"\n{player_name}'s Board:")  
    for row in player_board.board:
        print(" ".join(row).replace(computer_board.ship_char, player_board.water_char)) 

    print("\nComputer's Board:")
    for row in computer_board.board:
        print(" ".join(row))


# Main game 
def play_game():
  
    print("                     Welcome to 'Classic Battleship Game'")
    
    print("                                  ____________")
    print("                              _  |____________|  _")
    print("                       _=====| | |            | | |==== _")
    print("                 =====| |.---------------------------. | |==== ")
    print("   <--------------------'   .  .  .  .  .  .  .  .   '--------------/")
    print("     \\                                                             /")
    print("      \\_______________________________________________WWS_________/")
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f" Board Size: {BOARD_SIZE}. Number of ships: {NUM_SHIPS}")
    print(" Top left corner is row: 0, col: 0")
    print("-----------------------------------")

    player_name = input("Please enter your Ingame Name: ")
    print(f"\nWelcome, {player_name}!")

play_game()
