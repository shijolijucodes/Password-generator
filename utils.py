def copy_to_clipboard(root, text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()


def mask_password(password):
    if not password:
        return ""
    return "*" * len(password)
