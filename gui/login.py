import tkinter as tk
from tkinter import messagebox
from models.user import load_customers, save_customers, Customer
from gui.dashboard import show_dashboard, show_admin_dashboard

def register(username, password, email):
    if not username or not password or not email:
        messagebox.showerror("Input Error", "All fields are required for registration.")
        return

    customers = load_customers()
    if username in customers:
        messagebox.showerror("Error", "Username already exists.")
    else:
        customers[username] = Customer(username, password, email)
        save_customers(customers)
        messagebox.showinfo("Success", "Registration successful!")

def login(username, password, root):
    if not username or not password:
        messagebox.showerror("Input Error", "Username and password are required.")
        return

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Admin Login", "Welcome Admin!")
        root.destroy()
        show_admin_dashboard()
        return

    customers = load_customers()
    if username in customers and customers[username].password == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        root.destroy()
        show_dashboard(customers[username])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def show_login():
    root = tk.Tk()
    root.title("Grand Prix Ticket Booking System - Login")

    tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(root, text="Email (for registration):").grid(row=2, column=0, padx=10, pady=5)

    entry_username = tk.Entry(root)
    entry_password = tk.Entry(root, show="*")
    entry_email = tk.Entry(root)

    entry_username.grid(row=0, column=1, padx=10, pady=5)
    entry_password.grid(row=1, column=1, padx=10, pady=5)
    entry_email.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(root, text="Register", width=15, command=lambda: register(
        entry_username.get().strip(), entry_password.get().strip(), entry_email.get().strip()
    )).grid(row=3, column=0, padx=10, pady=10)

    tk.Button(root, text="Login", width=15, command=lambda: login(
        entry_username.get().strip(), entry_password.get().strip(), root
    )).grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()
