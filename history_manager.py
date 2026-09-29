import json
from datetime import datetime
from pathlib import Path


HISTORY_FILE = Path(__file__).resolve().parent / "password_history.json"


def _read_history():
    if not HISTORY_FILE.exists():
        return []

    try:
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_password(password):
    history = _read_history()
    history.append({
        "password": password,
        "created_at": datetime.now().isoformat(timespec="seconds")
    })

    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

    return True


def get_history():
    return _read_history()


def clear_history():
    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump([], file, indent=4)
