#!/usr/bin/env python3

import random

def read_names_and_verbs_from_files():
    try:
        with open("names.data", "r") as names_file:
            names = [line.strip() for line in names_file.readlines()]

        with open("verbs.data", "r") as verbs_file:
            verbs = [line.strip() for line in verbs_file.readlines()]

        return names, verbs
    except FileNotFoundError:
        print("Please ensure that 'names.data' and 'verbs.data' files exist.")
        exit(1)

def generate_password(combination):
    names, verbs = read_names_and_verbs_from_files()

    if combination == 2:
        name = random.choice(names)
        verb = random.choice(verbs)
        password = name + " " + verb
    elif combination == 3:
        name1 = random.choice(names)
        verb1 = random.choice(verbs)
        name2 = random.choice(names)
        verb2 = random.choice(verbs)
        password = name1 + " " + verb1 + " " + name2 + " " + verb2
    elif combination == 4:
        name1 = random.choice(names)
        verb1 = random.choice(verbs)
        name2 = random.choice(names)
        verb2 = random.choice(verbs)
        name3 = random.choice(names)
        verb3 = random.choice(verbs)
        password = name1 + " " + verb1 + " " + name2 + " " + verb2 + " " + name3 + " " + verb3
    else:
        print("Invalid combination specified.")
        return None

    # Remove leading and trailing spaces
    password = password.strip()

    return password

if __name__ == "__main__":
    # Generate and print 2-combination password
    # print("2-Combination Password:")
    password_2_combination = generate_password(2)
    print(password_2_combination)

    # Generate and print 3-combination password
    # print("\n3-Combination Password:")
    password_3_combination = generate_password(3)
    print(password_3_combination)

    # Generate and print 4-combination password
    # print("\n4-Combination Password:")
    password_4_combination = generate_password(4)
    print(password_4_combination)

