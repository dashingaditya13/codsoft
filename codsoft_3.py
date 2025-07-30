import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        ptype = password_type.get()

        if length <= 0:
            raise ValueError("Length must be positive")

        if ptype == "Easy":
            chars = string.ascii_lowercase
        elif ptype == "Medium":
            chars = string.ascii_letters + string.digits
        elif ptype == "Hard":
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters

        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text="🔐 " + password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length")

# GUI Setup
root = tk.Tk()
root.title("  Password Generator")
root.geometry("600x400")  
root.configure(bg="#f0f8ff") 

# Title Label
title_label = tk.Label(root, text=" 🔒 Password Generator", font=("Helvetica", 20, "bold"), fg="#4b0082", bg="#f0f8ff")
title_label.pack(pady=20)

# Password Length
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f0f8ff", fg="#333").pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Password Type
tk.Label(root, text="Select Password Strength:", font=("Arial", 12), bg="#f0f8ff", fg="#333").pack(pady=5)
password_type = tk.StringVar(value="Easy")

radio_frame = tk.Frame(root, bg="#f0f8ff")
radio_frame.pack()
tk.Radiobutton(radio_frame, text="Easy", variable=password_type, value="Easy", font=("Arial", 11), bg="#f0f8ff", fg="green").pack(side="left", padx=10)
tk.Radiobutton(radio_frame, text="Medium", variable=password_type, value="Medium", font=("Arial", 11), bg="#f0f8ff", fg="orange").pack(side="left", padx=10)
tk.Radiobutton(radio_frame, text="Hard", variable=password_type, value="Hard", font=("Arial", 11), bg="#f0f8ff", fg="red").pack(side="left", padx=10)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password,
          font=("Arial", 13, "bold"), bg="#4b0082", fg="white", padx=10, pady=5).pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#006400", wraplength=500)
result_label.pack(pady=10)

root.mainloop()
