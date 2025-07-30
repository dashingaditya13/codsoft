import tkinter as tk
from tkinter import messagebox

contacts = {}

# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        messagebox.showinfo("✅ Success", f"Contact '{name}' added successfully.")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("⚠ Missing Info", "Name and Phone are required.")

# Display all contacts
def display_contacts():
    listbox.delete(0, tk.END)
    for name, info in contacts.items():
        listbox.insert(tk.END, f" {name} -  {info['Phone']}")

# Search contact
def search_contact():
    query = search_entry.get()
    listbox.delete(0, tk.END)
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['Phone']:
            listbox.insert(tk.END, f"🔍 {name} - {info['Phone']}")

# Delete contact
def delete_contact():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        name = selected.split(" - ")[0].replace("👤", "").replace("🔍", "").strip()
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("🗑 Deleted", f"Contact '{name}' deleted.")
            display_contacts()
        else:
            messagebox.showerror("❌ Error", "Contact not found.")

# Update contact
def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name] = {
            'Phone': phone_entry.get(),
            'Email': email_entry.get(),
            'Address': address_entry.get()
        }
        messagebox.showinfo("🔁 Updated", f"Contact '{name}' updated.")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("❗ Not Found", "Contact doesn't exist.")

# Clear entries
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("500x550")
root.configure(bg="#eef5f9")

# Title
tk.Label(root, text="📇 My Contact Book", font=("Arial Rounded MT Bold", 20), bg="#eef5f9", fg="#2c3e50").pack(pady=10)

# Fields
def create_label(text):
    tk.Label(root, text=text, font=("Arial", 12, "bold"), bg="#eef5f9", anchor="w").pack(pady=2)

create_label("Name")
name_entry = tk.Entry(root, font=("Arial", 11), width=40)
name_entry.pack()

create_label(" Phone")
phone_entry = tk.Entry(root, font=("Arial", 11), width=40)
phone_entry.pack()

create_label("Email")
email_entry = tk.Entry(root, font=("Arial", 11), width=40)
email_entry.pack()

create_label(" Address")
address_entry = tk.Entry(root, font=("Arial", 11), width=40)
address_entry.pack()

# Buttons
btn_style = {"font": ("Arial", 10, "bold"), "width": 25, "pady": 5}

tk.Button(root, text="➕ Add Contact", bg="#27ae60", fg="white", command=add_contact, **btn_style).pack(pady=5)
tk.Button(root, text="✏ Update Contact", bg="#f39c12", fg="white", command=update_contact, **btn_style).pack(pady=5)
tk.Button(root, text="🗑 Delete Selected", bg="#e74c3c", fg="white", command=delete_contact, **btn_style).pack(pady=5)

create_label("🔍 Search (Name or Phone)")
search_entry = tk.Entry(root, font=("Arial", 11), width=40)
search_entry.pack()

tk.Button(root, text="🔍 Search Contact", bg="#2980b9", fg="white", command=search_contact, **btn_style).pack(pady=5)
tk.Button(root, text="📃 Show All Contacts", bg="#34495e", fg="white", command=display_contacts, **btn_style).pack(pady=5)

# Listbox
tk.Label(root, text="📜 Contact List", font=("Arial", 12, "bold"), bg="#eef5f9").pack(pady=(10, 2))
listbox = tk.Listbox(root, font=("Courier New", 11), width=60, height=8, bg="white", fg="black", selectbackground="#d1f2eb")
listbox.pack(pady=10)

root.mainloop()
