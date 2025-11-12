import math


def is_even(number):
    return number % 2 == 0

def is_cool(name):
    return name in ["Joe", "John", "Stephen"]

def is_lunchtime(hour, is_am):
    return (hour == 11 and is_am) or (hour == 12 and not is_am)

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def interval_intersect(a, b, c, d):
    return not (b < c or d < a)

def name_and_age(name, age):
    if age < 0:
        return "Error: Invalid age"
    return f"{name} is {age} years old."

def print_digits(number):
    if number < 0 or number >= 100:
        print("Error: Input is not a two-digit number.")
    else:
        tens = number // 10
        ones = number % 10
        print(f"The tens digit is {tens}, and the ones digit is {ones}.")

def name_lookup(first_name):
    lookup = {
        "Joe": "Warren",
        "Scott": "Rixner",
        "John": "Greiner",
        "Stephen": "Wong"
    }
    return lookup.get(first_name, "Error: Not an instructor")

def pig_latin(word):
    if word[0] in 'aeiou':
        return word + "way"
    return word[1:] + word[0] + "ay"

def smaller_root(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("Error: No real solutions")
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return min(root1, root2)
