import string
import random

def password_generator():
    random_string = ""
    counter = 0
    while counter < 12:
        random_string += random.choice(string.ascii_lowercase)
        counter += 1
    return random_string
print(password_generator())