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

# Generating a four-digit number with unique digits, do not start with zero
def generate_unique_four_digit_number():
    while True:
        digits = random.sample(range(0, 10), 4)
        if digits[0] != 0:
            return digits, int("".join(map(str, digits)))

# Generování čísla
digits, number = generate_unique_four_digit_number()
print(f"Vygenerované číslo: {number}{digits}")
    
        
# Listing the introductory text
print(
    "Hi there!", 
    45 * "-", 
    "I've generated a random 4 digit number for you.", 
    "Let's play a bulls and cows game.", 
    45 * "-", 
    sep="\n"
    )

