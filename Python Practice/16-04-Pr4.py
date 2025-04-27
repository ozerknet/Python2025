import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to check if the number is odd or even
def check_odd_even():
    number = simpledialog.askinteger("Input", "Enter a number:")
    if number is not None:
        if number % 2 == 0:
            messagebox.showinfo("Result", f"The number {number} is Even.")
        else:
            messagebox.showinfo("Result", f"The number {number} is Odd.")

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Call the function
check_odd_even()
