import random
import string

def generator_password():
    length = random.randint(10, 14)
    num_digits = random.randint(3, 4)
    num_specials = 2
    num_letters = length - num_digits - num_specials

    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    specials = random.choices(string.punctuation, k=num_specials)

    # Ensure at least one uppercase letter
    if not any(c.isupper() for c in letters):
        letters[random.randint(0, num_letters - 1)] = random.choice(string.ascii_uppercase)

    password_list = letters + digits + specials
    random.shuffle(password_list)
    return ''.join(password_list)

