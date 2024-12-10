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

# Loading libraries
import random

# Function definition for generating a unique four-digit number, does not start with zero
def generate_unique_four_digit_number():
    while True:
        digits = random.sample(range(0, 10), 4)
        if digits[0] != 0:
            return digits, int("".join(map(str, digits)))

# Generating a four-digit number with unique digits, does not start with zero
generated_digits, generated_number = generate_unique_four_digit_number()
print(f"Vygenerované číslo: {generated_digits} {generated_number}")
            
# Listing the introductory text
print(f"""
Hi there!
{'-' * 45}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{'-' * 45}
""")

# Entering the guessed number
guessed_number = input("Enter a four-digit number: ")

# Function definition for validating correct input
def validate_guess_number(guess):
    # List to store all errors
    errors = [] 
    # Check length
    if len(guess) != 4:
        errors.append("The number must have exactly 4 digits.")
    # Check if it contains only digits
    if not guess.isdigit():
        errors.append("The number can only contain digits (0-9).")
    # Check if it starts with zero
    if len(guess) > 0 and guess[0] == '0':
        errors.append("The number cannot start with zero.")
    # Check for duplicate digits
    if len(set(guess)) != len(guess):
        errors.append("The number cannot contain duplicate digits.")
    # If there are errors, join and return them
    if errors:
        return "\n".join(errors)
    # Everything is valid
    return "OK"

# User input verification
while True:
    validation_result = validate_guess_number(guessed_number)
    if validation_result == "OK":
        break
    else:
        print(f"Errors:\n{validation_result}")
        break