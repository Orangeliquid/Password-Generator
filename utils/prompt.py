from models.password_options import PasswordOptions


def prompt_user_options():
    try:
        length = int(input("Password length(default: 12): "))
        include_numbers = input("Include numbers? (y/n default: y): ").lower() != "n"
        include_symbols = input("Include symbols? (y/n, default: y): ").lower() != "n"

        options = PasswordOptions(
            length=length,
            include_numbers=include_numbers,
            include_symbols=include_symbols
        )

        print("Options selected:", options)
        return options
    except ValueError as e:
        print("Invalid input: ", e)
        return None
