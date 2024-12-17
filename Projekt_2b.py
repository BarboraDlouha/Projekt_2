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
# Import libraries and modules
#==================================================================================

#==================================================================================
# Function definitions:
#==================================================================================

def print_welcome_and_rules() -> None:
    """
    Print the welcome message, game rules, and the initial numbered grid for Tic Tac Toe.

    The grid shows positions numbered from 1 to 9 where players can place their marks.
    """
    print("""
Welcome to Tic Tac Toe
=============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* Horizontal row,
* Vertical row, or
* Diagonal row.
=============================================

Here is the initial game grid with positions numbered 1-9:
""")
    print_grid(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("Let's start the game!")


def print_grid(grid: list[str]) -> None:
    """
    Print the Tic Tac Toe grid with borders and a surrounding frame.

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
""".strip())  # .strip() odstraní prázdné řádky na začátku a konci

#==================================================================================
# Main Program
#==================================================================================

if __name__ == "__main__":
    print_welcome_and_rules()