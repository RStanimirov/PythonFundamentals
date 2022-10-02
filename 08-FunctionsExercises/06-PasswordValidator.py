def is_password_length_valid(password: str):
    if 6 <= len(password) <= 10:
        return True
    else:
        return False


def is_password_alphanumeric(password: str):
    if password.isalnum():
        return True
    else:
        return False


def at_least_two_digits(password: str):
    digits_count = 0
    for ch in password:
        if ch.isdigit():
            digits_count += 1

    if digits_count >= 2:
        return True
    else:
        return False


def validate_password(password: str):
    is_valid = True

    if not is_password_length_valid(password):
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not is_password_alphanumeric(password):
        print("Password must consist only of letters and digits")
        is_valid = False
    if not at_least_two_digits(password):
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")

password_input = input()

validate_password(password_input)
