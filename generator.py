import secrets
import string


def generate_password(length=12, use_lower=True, use_upper=True,
                      use_digits=True, use_symbols=True):
    """Generate a random password using Python's cryptographically secure RNG."""
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    groups = []
    if use_lower:
        groups.append(string.ascii_lowercase)
    if use_upper:
        groups.append(string.ascii_uppercase)
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append("!@#$%^&*()-_=+[]{}?")

    if not groups:
        raise ValueError("Select at least one character type.")

    if length < len(groups):
        raise ValueError(
            f"Length must be at least {len(groups)} for the selected options."
        )

    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # Shuffle without using the non-secure random module.
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)
