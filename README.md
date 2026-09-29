# Password Generator Project

A simple Python desktop application that generates secure random passwords,
checks their strength, copies them to the clipboard, and stores generated
passwords in a local history file.

## Features

- Password length selection from 4 to 64 characters
- Lowercase, uppercase, numbers and symbols
- Secure generation using Python's `secrets` module
- Password strength checker
- Copy generated password to clipboard
- Save generated passwords with timestamps
- Simple Tkinter graphical user interface
- Unit tests using pytest
- Basic project documentation and diagrams

## Project Structure

```text
PasswordGeneratorProject/
├── main.py
├── generator.py
├── strength_checker.py
├── history_manager.py
├── utils.py
├── requirements.txt
├── README.md
├── statement.md
├── screenshots/
│   ├── home.png
│   └── generated.png
├── tests/
│   ├── test_generator.py
│   └── test_strength.py
└── docs/
    ├── usecase.png
    ├── classdiagram.png
    ├── sequence.png
    └── workflow.png
```

## Requirements

- Python 3.10 or later
- Tkinter (normally included with standard Python on Windows)

Install the optional testing package:

```bash
pip install -r requirements.txt
```

## Run

Open a terminal in the project folder and run:

```bash
python main.py
```

## Run Tests

```bash
pytest
```

## How It Works

1. The user selects password length and character types.
2. `generator.py` creates the password using `secrets`.
3. `strength_checker.py` calculates a simple strength score.
4. The generated password can be copied to the clipboard.
5. The user can save it to `password_history.json`.
6. `history_manager.py` manages the saved history.

## Security Note

This project is intended for academic demonstration. Password history is
stored locally in plain JSON for simplicity. A production password manager
should not store passwords this way and should use secure storage and
encryption.

## Author

Student Project - Password Generator
