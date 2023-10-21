import re


def password_strength(password):
    # Check length
    length = len(password)
    if length > 8:
        length_strength = 1
    else:
        length_strength = 0

    # Check for uppercase and lowercase letters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    # Check for digits
    has_digit = any(char.isdigit() for char in password)

    # Check for special characters
    has_special = bool(re.search(r'[!@#$%^&*()_+]', password))

    # Calculate the overall strength
    strength_score = length_strength + has_upper + has_lower + has_digit + has_special

    if strength_score == 5:
        return "strong"
    elif strength_score >= 3:
        return "medium"
    else:
        return "weak"


# Example usage:
user_password = input("Enter your password: ")
strength = password_strength(user_password)
print(f"Password strength: {strength}")
