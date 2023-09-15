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


# Constants
BOARD_SIZE = 5
NUM_SHIPS = 4

# Initialize the player and computer boards
player_board = Board(BOARD_SIZE)
computer_board = Board(BOARD_SIZE)


# Place ships on the computer board randomly
def place_computer_ships(board):
    placed_ships = 0
    while placed_ships < NUM_SHIPS:
        x, y = randint(0, BOARD_SIZE - 1), randint(0, BOARD_SIZE - 1)
        if board.board[x][y] != board.ship_char:
            board.place_ship(x, y)
            placed_ships += 1


# Function to randomly place the player's ships
def place_player_ships(board):
    print("\nRandomly placing your ships:")
    placed_ships = 0
    while placed_ships < NUM_SHIPS:
        x = randint(0, BOARD_SIZE - 1)
        y = randint(0, BOARD_SIZE - 1)
        if board.board[x][y] != board.ship_char:
            board.place_ship(x, y)
            placed_ships += 1


# Check if the player's guess is valid
def is_valid_guess(board, x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and \
           board.board[x][y] != board.hit_char and board.board[x][y] != board.miss_char


# Display the game boards
def display_boards(player_board, computer_board, player_name):
    print(f"\n{player_name}'s Board:")
    player_board.display()

    print("\nComputer's Board:")
    for row in computer_board.board:
        print(" ".join([cell if cell != computer_board.ship_char else computer_board.water_char for cell in row]))


# Function for the player's turn
def player_turn():
    print("\nYour turn:")
    while True:
        guess_x = input("Guess a row (0-4): ")
        guess_y = input("Guess a column (0-4): ")

        # Check if both inputs are numeric
        if guess_x.isnumeric() and guess_y.isnumeric():
            guess_x = int(guess_x)
            guess_y = int(guess_y)
            
            if is_valid_guess(computer_board, guess_x, guess_y):

                if (guess_x, guess_y) in previous_guesses:
                    print("You cannot enter the same guess twice. Try again.")
                    continue
                previous_guesses.add((guess_x, guess_y))
                
                if computer_board.board[guess_x][guess_y] == computer_board.ship_char:
                    print("Player got a hit!")
                    computer_board.board[guess_x][guess_y] = computer_board.hit_char
                    return True
                else:
                    print("Player missed this time.")
                    computer_board.board[guess_x][guess_y] = computer_board.miss_char
                    return False
            else:
                print("Invalid guess. Try again with numbers between 0 and 4.")
        else:
            print("Invalid input. Please enter numeric values for row and column.")


# Function for the computer's turn
def computer_turn():
    while True:
        comp_guess_x = randint(0, BOARD_SIZE - 1)
        comp_guess_y = randint(0, BOARD_SIZE - 1)

        if player_board.board[comp_guess_x][comp_guess_y] == player_board.hit_char or \
           player_board.board[comp_guess_x][comp_guess_y] == player_board.miss_char:
            # Computer has already guessed this location. Try again.
            continue

        if player_board.board[comp_guess_x][comp_guess_y] == player_board.ship_char:
            print("Computer got a hit!")
            player_board.board[comp_guess_x][comp_guess_y] = player_board.hit_char
            return True
        else:
            print("Computer missed this time.")
            player_board.board[comp_guess_x][comp_guess_y] = player_board.miss_char
            return False


# Main game
def play_game():
    print("           Welcome to 'Classic Battleship Game'")
    print("                     ____________")
    print("                  _ |___________| _  ")
    print("          _====| | |             | | |=== _")
    print("        ====| |.--------------------. | |=== ")
    print("    <---------'   .  .  .  .  .  .   '---------/")
    print("     \\                                       /")
    print("      \\_____________________________________/")
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f" Board Size: {BOARD_SIZE}. Number of ships: {NUM_SHIPS}")
    print(" Top left corner is row: 0, col: 0")
    print("-----------------------------------")

    player_name = input("Please enter your Ingame Name: ")
    print(f"\nWelcome, {player_name}!")

    # Initialize boards for a new game
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            player_board.board[i][j] = player_board.water_char
            computer_board.board[i][j] = computer_board.water_char

    place_player_ships(player_board)
    place_computer_ships(computer_board)
    display_boards(player_board, computer_board, player_name)

    player_score = 0
    computer_score = 0

    while True:
        # Player's turn
        player_hit = player_turn()
        if player_hit:
            player_score += 1

        # Computer's turn
        computer_hit = computer_turn()
        if computer_hit:
            computer_score += 1

        display_boards(player_board, computer_board, player_name)

        print("\nAfter this round, the scores are:")
        print(f"Player: {player_score}. Computer: {computer_score}")

        if player_score == NUM_SHIPS:
            print("Congratulations! You win!")
            play_again = input("Press Enter to continue or 'n' to start a new game: ")
            if play_again.lower() == 'n':
                play_game()  # Start a new game
            else:
                break
        elif computer_score == NUM_SHIPS:
            print("Computer has sunk all of your ships. Computer wins!")
            play_again = input("Press Enter to quit or write 'n' to start a new game: ")
            if play_again.lower() == 'n':
                play_game()  # Start a new game
            else:
                break
        else:
            play_again = input("Press Enter to continue or 'n' to start a new game: ")
            if play_again.lower() == 'n':
                play_game()  # Start a new game
            elif not play_again:
                continue  # Continue the current game
            else:
                break


if __name__ == "__main__":
    play_game()
