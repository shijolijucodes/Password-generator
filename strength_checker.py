import string


def check_strength(password):
    """Return a simple password-strength score from 0 to 5."""
    if not password:
        return {"score": 0, "label": "Very Weak"}

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(ch.islower() for ch in password):
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch in string.punctuation for ch in password):
        score += 1

    score = min(score, 5)

    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong",
    }

    return {"score": score, "label": labels[score]}
