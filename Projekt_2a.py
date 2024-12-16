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
    Validates user input (checks the number and correctness of characters, 
    duplicates and the starting digit, which must not be zero)
    """
    errors = [] 
    if len(guessed_number) != 4:
        errors.append("The number must have exactly 4 digits.")
    if not guessed_number.isdigit():
        errors.append("The number can only contain digits (0-9).")
    if len(guessed_number) > 0 and guessed_number[0] == '0':
        errors.append("The number cannot start with zero.")
    if len(set(guessed_number)) != len(guessed_number):
        errors.append("The number cannot contain duplicate digits.")
    if errors:
        return "\n".join(errors)
    return "OK"

def calculate_bulls_and_cows(secret_number: str, guessed_number: str) -> Tuple[int, int]:
    """
    Counts the number of 'bulls' and 'cows'.

    Bulls: Correct digit in the correct position.
    Cows: Correct digit in the wrong position.
    """
    bulls = sum(1 for i in range(len(secret_number)) if guessed_number[i] == secret_number[i])
    cows = sum(1 for digit in guessed_number if digit in secret_number) - bulls
    return bulls, cows

def calculate_statistics(attempts: List[int], times: List[float]) -> Tuple[int, float, float, float]:
    """
    Calculate game statistics: best score, average attempts, best time, average time
    """
    if not attempts or not times:
        return 0, 0.0, 0.0, 0.0
    best_score = min(attempts) 
    average_attempts = sum(attempts) / len(attempts) 
    best_time = min(times)    
    average_time = sum(times) / len(times) 
    return best_score, average_attempts, best_time, average_time

def print_statistics(attempts: List[int], times: List[float]):
    """Calculate and print game statistics."""
    best_score, avg_attempts, best_time, avg_time = calculate_statistics(attempts, times)
    print("\nGame Statistics:")
    print(f"Games played: {len(attempts)}")
    print(f"Best score (fewest attempts): {best_score}")
    print(f"Average attempts per game: {avg_attempts:.2f}")
    print(f"Best time: {int(best_time // 60)} minute(s) and {int(best_time % 60)} second(s)")
    print(f"Average time per game: {int(avg_time // 60)} minute(s) and {int(avg_time % 60)} second(s)")

def play_single_game() -> Tuple[int, float]:
    """Play a single game of Bulls and Cows."""
    generated_digits, generated_number_as_int, generated_number_as_str = generate_unique_number()
    attempts = 0
    start_time = time.time()
    while True:
        guessed_number = input("Enter a four-digit number: ")
        validation_result = validate_guess_number(guessed_number)
        if validation_result == "OK":
            attempts += 1
            bulls, cows = calculate_bulls_and_cows(generated_number_as_str, guessed_number)
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
            if bulls == 4:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Congratulations! You've guessed the number in {attempts} attempt(s)!")
                print(f"It took you {int(elapsed_time // 60)} minute(s) and {int(elapsed_time % 60)} second(s).")
                return attempts, elapsed_time
        else:
            print(f"Your input did not meet the following conditions:\n{validation_result}")

def main_game_loop():
    """Main game loop for Bulls and Cows."""
    game_statistics = []  
    game_times = []       
    while True:
        attempts, elapsed_time = play_single_game()
        game_statistics.append(attempts)
        game_times.append(elapsed_time)
        print_statistics(game_statistics, game_times)
        choice = input("\nWould you like to play again? (y/n): ")
        if choice.lower() != "y":
            print("Thank you for playing! Goodbye!")
            break

#==================================================================================
# Main Program
#==================================================================================
if __name__ == "__main__":
    main_game_loop()