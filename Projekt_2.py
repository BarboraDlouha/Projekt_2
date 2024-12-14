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

# Defining functions:

# 1. Function for generating a unique four-digit number that does not start with zero
def generate_unique_number() -> Tuple[List[int], int]:
    """
    Generate a 4-digit number with unique digits that does not start with zero.
    """
    while True:
        digits = random.sample(range(0, 10), 4)
        if digits[0] != 0:
            return digits, int("".join(map(str, digits)))
        
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
generated_digits, generated_number = generate_unique_number()
print(f"Vygenerované číslo: {generated_digits} {generated_number}")
            
# Listing the introductory text
print(f"""
Hi there!
{'-' * 45}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{'-' * 45}
""")

# Inputting the guessed number


# User input verification

# Game loop
while True:
    guessed_number = input("Enter a four-digit number: ")

    # Validate user input
    validation_result = validate_guess_number(guessed_number)
    if validation_result == "OK":
        # Convert guessed_number to a list of integers
        guessed_number_list = [int(digit) for digit in guessed_number]

        # Calculate bulls and cows
        bulls, cows = calculate_bulls_and_cows(generated_digits, guessed_number_list)

        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"

        print(f"{bulls} {bull_word}, {cows} {cow_word}")

        # Check for win condition
        if bulls == 4:
            print("Congratulations! You've guessed the number!")
            break
    else:
        print(f"Your input did not meet the following conditions:\n{validation_result}")

