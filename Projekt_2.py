#==================================================================================
# Header
#==================================================================================

print(60 * "-")
print("""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Dlouha
email: Barbora-Dlouha@seznam.cz
""")
print(60 * "-")

#==================================================================================
# Import libraries and modules
#==================================================================================
import random
from typing import List, Tuple, Union
import time

#==================================================================================
# Global variables and constants
#==================================================================================

game_statistics = [] # List to store the number of attempts per game
game_times = [] # List to store the time (in seconds) for each game

#==================================================================================
# Function definitions:
#==================================================================================
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

def calculate_statistics(attempts: List[int], times: List[float]) -> Tuple[int, float, float, float]:
    """
    Calculate game statistics: best score, average attempts, best time, average time
    """
    if not attempts or not times:
        return (0, 0.0, 0.0, 0.0)

    best_score = min(attempts) 
    average_attempts = sum(attempts) / len(attempts) 
    best_time = min(times)    
    average_time = sum(times) / len(times) 

    return best_score, average_attempts, best_time, average_time
          
# Listing the introductory text
print(f"""
Hi there!
{'-' * 45}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{'-' * 45}
""")

# Main game loop: can restart the game when the player chooses to play again.
while True:
    # Generating a four-digit number with unique digits that does not start with zero
    generated_digits, generated_number_as_int, generated_number_as_str = generate_unique_number()
    # Start measuring time
    start_time = time.time()
    # Initial value for the number of attempts
    attempts = 0
    
    # Guessing loop:  finds out the status of player's guesses until the number is correctly guessed
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
                print(f"Congratulations! You've guessed the number in {attempts} attempt(s)!")
                print(f"It took you {int(elapsed_time // 60)} minute(s) and {int(elapsed_time % 60)} second(s).")

                # completing the sheets of attempts and times
                game_statistics.append(attempts)
                game_times.append(elapsed_time)
                break

        # Listing of non-compliant conditions
        else:
            print(f"Your input did not meet the following conditions:\n{validation_result}")

    # Calculating statistics after the game ends
    best_score, avg_attempts, best_time, avg_time = calculate_statistics(game_statistics, game_times)

    print("\nGame Statistics:")
    print(f"Games played: {len(game_statistics)}")
    print(f"Best score (fewest attempts): {best_score}")
    print(f"Average attempts per game: {avg_attempts:.2f}")
    print(f"Best time: {int(best_time // 60)} minute(s) and {int(best_time % 60)} second(s)")
    print(f"Average time per game: {int(avg_time // 60)} minute(s) and {int(avg_time % 60)} second(s)")

    # Asking the user to play again
    choice = input("\nWould you like to play again? (y/n): ")
    if choice.lower() != "y":
        print("Thank you for playing! Goodbye!")
        break

    

