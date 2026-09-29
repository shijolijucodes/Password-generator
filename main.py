import tkinter as tk
from tkinter import messagebox
from generator import generate_password
from strength_checker import check_strength
from history_manager import save_password
from utils import copy_to_clipboard


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("620x520")
        self.root.resizable(False, False)

        title = tk.Label(
            root, text="Password Generator",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            root, text="Create a strong and random password",
            font=("Segoe UI", 10)
        )
        subtitle.pack(pady=(0, 20))

        options = tk.Frame(root)
        options.pack()

        tk.Label(options, text="Password length:").grid(row=0, column=0, padx=8, pady=8)
        self.length_var = tk.IntVar(value=12)
        tk.Spinbox(
            options, from_=4, to=64, textvariable=self.length_var,
            width=8
        ).grid(row=0, column=1, padx=8, pady=8)

        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)

        tk.Checkbutton(options, text="Lowercase", variable=self.lower_var).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(options, text="Uppercase", variable=self.upper_var).grid(row=1, column=1, sticky="w")
        tk.Checkbutton(options, text="Numbers", variable=self.digit_var).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(options, text="Symbols", variable=self.symbol_var).grid(row=2, column=1, sticky="w")

        self.password_var = tk.StringVar()
        password_box = tk.Entry(
            root, textvariable=self.password_var,
            font=("Consolas", 15), justify="center", width=42
        )
        password_box.pack(pady=22)

        self.strength_var = tk.StringVar(value="Strength: -")
        tk.Label(
            root, textvariable=self.strength_var,
            font=("Segoe UI", 12, "bold")
        ).pack(pady=5)

        buttons = tk.Frame(root)
        buttons.pack(pady=15)

        tk.Button(
            buttons, text="Generate", width=14,
            command=self.generate
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            buttons, text="Copy", width=14,
            command=self.copy
        ).grid(row=0, column=1, padx=6)

        tk.Button(
            buttons, text="Save to History", width=14,
            command=self.save
        ).grid(row=0, column=2, padx=6)

        tk.Label(
            root,
            text="Tip: Use long passwords with a mix of letters, numbers and symbols.",
            wraplength=520
        ).pack(pady=18)

    def generate(self):
        try:
            password = generate_password(
                self.length_var.get(),
                self.lower_var.get(),
                self.upper_var.get(),
                self.digit_var.get(),
                self.symbol_var.get()
            )
            self.password_var.set(password)
            result = check_strength(password)
            self.strength_var.set(f"Strength: {result['label']} | Score: {result['score']}/5")
        except ValueError as error:
            messagebox.showerror("Invalid options", str(error))

    def copy(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Nothing to copy", "Generate a password first.")
            return
        copy_to_clipboard(self.root, password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

    def save(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Nothing to save", "Generate a password first.")
            return
        save_password(password)
        messagebox.showinfo("Saved", "Password added to history.")


if __name__ == "__main__":
    app_root = tk.Tk()
    PasswordGeneratorApp(app_root)
    app_root.mainloop()
