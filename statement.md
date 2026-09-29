# Project Statement

## Project Title
Password Generator

## Problem Statement
Weak and repeated passwords can make online accounts easier to compromise.
Users often create passwords that are short or predictable. The aim of this
project is to provide a small desktop application that can generate random
passwords with different character combinations and give the user a basic
indication of password strength.

## Objectives
1. Generate random passwords of user-selected length.
2. Allow the user to select lowercase letters, uppercase letters, numbers
   and symbols.
3. Check the approximate strength of a generated password.
4. Allow the password to be copied to the clipboard.
5. Maintain a simple local history of generated passwords.
6. Demonstrate modular Python programming and unit testing.

## Technologies Used
- Python
- Tkinter
- secrets
- string
- JSON
- datetime
- pytest

## Modules
- `main.py` - graphical user interface and application flow.
- `generator.py` - password generation logic.
- `strength_checker.py` - strength scoring.
- `history_manager.py` - local history storage.
- `utils.py` - helper functions.

## Expected Outcome
The final application should generate a random password according to the
selected settings, display its strength, and provide copy/save functionality
through a simple GUI.

## Limitations
The history file is intentionally simple for an academic project. It should
not be treated as secure password storage in a real-world application.
