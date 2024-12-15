# Separator 
print(60 * "-")

# Header  
print("""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Dlouha
email: Barbora-Dlouha@seznam.cz
""")

# Separator
print(60 * "-")

# Loading libraries and modules
import random
from typing import List, Tuple, Union
import time

# Defining functions:

# 1. Function for generating a unique four-digit number that does not start with zero
def generate_unique_number() -> Tuple[List[int], int, str]:
    """
    Generate a 4-digit number with unique digits that does not start with zero.
    """
    while True:
        digits = random.sample(range(0, 10), 4)
        if digits[0] != 0:
            number_as_int = int("".join(map(str, digits)))  
            number_as_str = "".join(map(str, digits))  
            return digits, number_as_int, number_as_str
        
# 2. Function for validating correct input
def validate_guess_number(guessed_number: str) -> Union[str, str]:
    """ 
    validates user input (checks the number and correctness of characters, 
    duplicates and the starting digit, which must not be zero)
    """
    # List to store all errors
    errors = [] 
    # Check length
    if len(guessed_number) != 4:
        errors.append("The number must have exactly 4 digits.")
    # Check if it contains only digits
    if not guessed_number.isdigit():
        errors.append("The number can only contain digits (0-9).")
    # Check if it starts with zero
    if len(guessed_number) > 0 and guessed_number[0] == '0':
        errors.append("The number cannot start with zero.")
    # Check for duplicate digits
    if len(set(guessed_number)) != len(guessed_number):
        errors.append("The number cannot contain duplicate digits.")
    # If there are errors, join and return them
    if errors:
        return "\n".join(errors)
    # Everything is valid
    return "OK"

# 3. Function to calculate bulls and cows
def calculate_bulls_and_cows(secret_number: str, guessed_number: str) -> Tuple[int, int]:
    """
    Counts the number of 'bulls' and 'cows'.

    Bulls: Correct digit in the correct position.
    Cows: Correct digit in the wrong position.
    """
    bulls = 0
    cows = 0
    
    for i in range(len(secret_number)):
        if guessed_number[i] == secret_number[i]:
            bulls += 1
        elif guessed_number[i] in secret_number:
            cows += 1 

    return bulls, cows

# Generating a four-digit number with unique digits that does not start with zero
generated_digits, generated_number_as_int, generated_number_as_str = generate_unique_number()
          
# Listing the introductory text
print(f"""
Hi there!
{'-' * 45}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{'-' * 45}
""")

# Start measuring time
start_time = time.time()

 # List to store the number of attempts per game
game_statistics = []  

# Main game loop
attempts = 0

while True:
    # Inputting the guessed number
    guessed_number = input("Enter a four-digit number: ")

    # Inputting user verification
    validation_result = validate_guess_number(guessed_number)
    
    if validation_result == "OK":
        # Counting the number of attempts
        attempts += 1
        # Calculating bulls and cows
        bulls, cows = calculate_bulls_and_cows(generated_number_as_str, guessed_number)

        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"

        print(f"{bulls} {bull_word}, {cows} {cow_word}")

        # Checking for win condition
        if bulls == 4:
            # End measuring time
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You've guessed the number in {attempts} attempts!")
            print(f"It took you {int(elapsed_time // 60)} minutes and {int(elapsed_time % 60)} seconds.")
            # Saving attempts for this game
            game_statistics.append(attempts)
            break
    # Listing of non-compliant conditions
    else:
        print(f"Your input did not meet the following conditions:\n{validation_result}")

# Game options
print(f"You've completed {len(game_statistics)} game(s).")
if len(game_statistics) > 0:
    print(f"Average attempts per game: {sum(game_statistics) / len(game_statistics):.2f}")
    print(f"Attempts in each game: {game_statistics}")
    print(f"Best score (fewest attempts): {min(game_statistics)}")  # Display best score

# Asking if the user wants to play again
choice = input("\nWould you like to play again? (y/n): ")
if choice.lower() != "y":
    print("Thank you for playing! Goodbye!")
    

