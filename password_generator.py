import tkinter as tk
import random
import string

def evaluate_password_strength(password):
    """Evaluate the strength of the generated password."""
    strength_levels = ['Weak', 'Moderate', 'Strong', 'Very Strong']
    score = 0

    if len(password) >= minpasslen:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    return strength_levels[score]

def generate_password():
    """Generate and display a random password based on user inputs."""
    try:
        passlen = int(entry_passlen.get())
    except ValueError:
        label_result.config(text='Please enter a valid number for password length.')
        return

    if passlen < minpasslen or passlen > maxpasslen:
        label_result.config(text=f'Password length must be between {minpasslen} and {maxpasslen}.')
        return

    char_sets = [string.ascii_lowercase]
    if var_spaces.get():
        char_sets.append(' ')
    if var_numbers.get():
        char_sets.append(string.digits)
    if var_special.get():
        char_sets.append(string.punctuation)
    if var_uppercase.get():
        char_sets.append(string.ascii_uppercase)

    all_chars = ''.join(char_sets)
    password = ''.join(random.choices(all_chars, k=passlen))
    strength = evaluate_password_strength(password)

    label_result.config(text=f'Generated Password: {password}\nStrength: {strength}')

# Constants for password length
minpasslen = 8
maxpasslen = 30

# Main window setup
root = tk.Tk()
root.title("Random Password Generator")

# Password length input
tk.Label(root, text="Password Length:").pack()
entry_passlen = tk.Entry(root)
entry_passlen.pack()

# Checkboxes for password options
var_spaces = tk.BooleanVar()
tk.Checkbutton(root, text="Include Spaces", variable=var_spaces).pack()

var_numbers = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack()

var_special = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).pack()

var_uppercase = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack()

# Label for displaying result
label_result = tk.Label(root, text="")
label_result.pack()

# Start the GUI event loop
root.mainloop()
