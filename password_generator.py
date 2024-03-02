import random


def generate_random_password():
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "1234567890"
    symbols = "!@#$%^&*"

    password = []

    password_letters = [random.choice(letters) for num in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for num in range(random.randint(2, 4))]

    password = password_letters + password_symbols + password_numbers

    random.shuffle(password)
    final_password = "".join(password)

    return final_password
