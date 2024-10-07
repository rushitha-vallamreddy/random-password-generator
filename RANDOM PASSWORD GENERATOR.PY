import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate the password
def generate_password():
    length = int(length_entry.get())

    # Check if user selected at least one option
    if not (use_lower.get() or use_upper.get() or use_digits.get() or use_special.get()):
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return

    # Define possible characters based on user's choices
    characters = ""
    if use_lower.get():
        characters += string.ascii_lowercase
    if use_upper.get():
        characters += string.ascii_uppercase
    if use_digits.get():
        characters += string.digits
    if use_special.get():
        characters += string.punctuation

    # Ensure at least one character from each selected category
    password = []
    if use_lower.get():
        password.append(random.choice(string.ascii_lowercase))
    if use_upper.get():
        password.append(random.choice(string.ascii_uppercase))
    if use_digits.get():
        password.append(random.choice(string.digits))
    if use_special.get():
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password
    if len(password) < length:
        password.extend(random.choice(characters) for _ in range(length - len(password)))

    random.shuffle(password)  # Shuffle to avoid predictable patterns

    password = ''.join(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy the password to clipboard
def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main application window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")

# Password length label and entry
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")  # Default length
length_entry.pack()

# Options for password complexity
use_lower = tk.BooleanVar(value=True)
use_upper = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Lowercase", variable=use_lower).pack(anchor="w")
tk.Checkbutton(root, text="Include Uppercase", variable=use_upper).pack(anchor="w")
tk.Checkbutton(root, text="Include Digits", variable=use_digits).pack(anchor="w")
tk.Checkbutton(root, text="Include Special Characters", variable=use_special).pack(anchor="w")

# Entry to display the generated password
password_entry = tk.Entry(root, font=("Arial", 12), width=30)
password_entry.pack(pady=10)

# Generate password button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

# Copy to clipboard button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Run the application
root.mainloop()
