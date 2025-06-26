import random
import string

from models.password_options import PasswordOptions

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = string.punctuation


def generate_password(options: PasswordOptions) -> str:
    characters = ""

    if options.include_uppercase_letters:
        characters += UPPERCASE
    if options.include_lowercase_letters:
        characters += LOWERCASE
    if options.include_numbers:
        characters += NUMBERS
    if options.include_symbols:
        characters += SYMBOLS

    if not characters:
        raise ValueError("No character types selected for password generation.")

    return "".join(random.choice(characters) for i in range(options.length))
