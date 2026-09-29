from strength_checker import check_strength


def test_empty_password():
    result = check_strength("")
    assert result["score"] == 0


def test_weak_password():
    result = check_strength("abc")
    assert result["label"] == "Very Weak"


def test_long_mixed_password():
    result = check_strength("Abcd1234!xyz")
    assert result["score"] == 5
    assert result["label"] == "Very Strong"


def test_medium_password():
    result = check_strength("Password1")
    assert result["score"] >= 2
