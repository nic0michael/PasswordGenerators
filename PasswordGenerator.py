#!/usr/bin/env python3

import random
import string

def generate_password():
    length = 25
    num_upper = int(length * 0.4)
    num_lower = int(length * 0.4)
    num_digits = int(length * 0.35)
    num_special = int(length * 0.2)
    num_spaces = int(length * 0.2)

    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:'\",.<>?`~"
    spaces = " "

    # Generate character groups
    upper_chars = [random.choice(uppercase_letters) for _ in range(num_upper)]
    lower_chars = [random.choice(lowercase_letters) for _ in range(num_lower)]
    digit_chars = [random.choice(digits) for _ in range(num_digits)]
    special_chars = [random.choice(special_characters) for _ in range(num_special)]
    space_chars = [random.choice(spaces) for _ in range(num_spaces)]

    # Combine all character groups
    all_chars = upper_chars + lower_chars + digit_chars + special_chars + space_chars

    # Shuffle the characters
    random.shuffle(all_chars)

    # Ensure the password doesn't start or end with a space
    while all_chars[0] == ' ' or all_chars[-1] == ' ':
        random.shuffle(all_chars)

    # Convert the list of characters to a string
    password = ''.join(all_chars)

    return password

if __name__ == "__main__":
    generated_password = generate_password()
    print(generated_password)

