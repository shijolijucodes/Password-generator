from generator import generate_password


def test_password_length():
    password = generate_password(16)
    assert len(password) == 16


def test_selected_character_types():
    password = generate_password(
        12,
        use_lower=True,
        use_upper=False,
        use_digits=False,
        use_symbols=False
    )
    assert password.islower()
    assert len(password) == 12


def test_all_selected_types_are_present():
    password = generate_password(12, True, True, True, True)

    assert any(ch.islower() for ch in password)
    assert any(ch.isupper() for ch in password)
    assert any(ch.isdigit() for ch in password)
    assert any(not ch.isalnum() for ch in password)


def test_invalid_length():
    try:
        generate_password(3)
        assert False
    except ValueError:
        assert True


def test_no_character_type_selected():
    try:
        generate_password(12, False, False, False, False)
        assert False
    except ValueError:
        assert True
