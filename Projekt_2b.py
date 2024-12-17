#==================================================================================
# Header
#==================================================================================

print(60 * "-")
print("""
projekt_2b.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Dlouha
email: Barbora-Dlouha@seznam.cz
""")
print(60 * "-")

#==================================================================================
# Constants:
#==================================================================================

GRID_SIZE = 9          
EMPTY_CELL = " "       
PLAYER_X = "x"         
PLAYER_O = "o"    
WELCOME_TEXT = f"""
Welcome to Tic Tac Toe
=============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
- Horizontal row
- Vertical row
- Diagonal row
=============================================
Here is the initial game grid with positions numbered 1-9:
"""     

#==================================================================================
# Function definitions:
#==================================================================================

def print_welcome_and_rules() -> None:
    """
    Print the welcome message, game rules, and the initial numbered grid for Tic Tac Toe.
    The grid shows positions numbered from 1 to 9 where players can place their marks.
    """
    print(WELCOME_TEXT)
    print_grid([str(i + 1) for i in range(GRID_SIZE)])
    print("\nLet's start the game!")


def print_grid(grid: list[str]) -> None:
    """
    Print the Tic Tac Toe grid.

    Args:
    - grid (list[str]): A list of 9 elements representing the grid cells.
    """
    print(f"""
+-----------+
| {grid[0]} | {grid[1]} | {grid[2]} |
|---+---+---|
| {grid[3]} | {grid[4]} | {grid[5]} |
|---+---+---|
| {grid[6]} | {grid[7]} | {grid[8]} |
+-----------+
""".strip())  

def validate_player_input(input_str: str, grid: list[str]) -> tuple[bool, list[str]]:
    """
    Validate the player's input for Tic Tac Toe.

    Args:
    - input_str (str): The player's input as a string.
    - grid (list[str]): The current game grid.

    Returns:
    - tuple[bool, list[str]]: A tuple where the first value is True if the input is valid,
                              and the second is a list of error messages if invalid.
    """
    errors = []  # List to collect error messages

    # Check if the input is numeric
    if not input_str.isdigit():
        errors.append("The input must be a number between 1 and 9.")
    else:
        move = int(input_str)
        # Check if the number is within the valid range
        if move < 1 or move > GRID_SIZE:
            errors.append("The number must be in the range of 1 to 9.")
        # Check if the position is already occupied
        elif grid[move - 1] != EMPTY_CELL:
            errors.append("The chosen position is already taken. Please choose another spot.")

    # Return True if there are no errors, otherwise return False and the error list
    return (len(errors) == 0, errors)

def get_validated_move(grid: list[str], player: str) -> int:
    """
    Prompt the player to enter a valid move and validate it.

    Args:
    - grid (list[str]): The current game grid.
    - player (str): The current player's symbol ('o' or 'x').

    Returns:
    - int: The valid position chosen by the player (0-8).
    """
    while True:
        move_input = input(f'Player "{player}" | Please, enter your move number (1-9): ')
        is_valid, errors = validate_player_input(move_input, grid)

        if is_valid:
            return int(move_input) - 1 
        else:
            for error in errors:
                print(f"Error: {error}")

def check_winner(grid: list[str], player: str) -> bool:
    """
    Check if the current player has won the game.

    Args:
    - grid (list[str]): The current game grid.
    - player (str): The current player's symbol ('o' or 'x').

    Returns:
    - bool: True if the player has won, otherwise False.
    """
    win_conditions = [
        [0, 1, 2],  # Horizontal lines
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Vertical columns
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonal line
        [2, 4, 6]
    ]
    for condition in win_conditions:
        if grid[condition[0]] == grid[condition[1]] == grid[condition[2]] == player:
            return True
    return False

def main_game_loop():
    """
    Main game loop for Tic Tac Toe.
    Players 'o' and 'x' take turns to make moves until there is a winner or the grid is full.
   """

while True:    
    # Prints rules and a numbered grid
    print_welcome_and_rules()

    # Initial empty grid and the starting player 'o'
    grid = [EMPTY_CELL] * GRID_SIZE
    current_player = PLAYER_O

    # Game loop
    for turn in range(GRID_SIZE):  
        print_grid(grid)  
        move = get_validated_move(grid, current_player)
        grid[move] = current_player  

        # Winner check
        if check_winner(grid, current_player):
            print_grid(grid)  
            print(f'Congratulations! Player "{current_player}" wins!')
            break

        # Substitution of players
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O
    else:
        # if the game ends in a draw
        print_grid(grid)
        print("It's a draw! No one wins.")

    # Ask for restart
    choice = input("\nWould you like to play again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing! Goodbye!")
        break

#==================================================================================
# Main Program
#==================================================================================

if __name__ == "__main__":
    main_game_loop()