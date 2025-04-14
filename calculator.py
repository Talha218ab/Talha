import tkinter as tk
from tkinter import messagebox
import math

# Functions for operations
def Add(a, b):
    return a + b

def Substract(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def Modulas(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Cannot perform modulas with ZERO!"

def Power(a, b):
    return a ** b

def Square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Invalid input for square root"

# Main function to handle calculation
def calculate():
    try:
        if operation.get() == "Square Root":
            num = float(entry1.get())
            result = Square_root(num)
        else:
            num1 = float(entry1.get())
            num2 = float(entry2.get())

            op = operation.get()
            if op == "Add":
                result = Add(num1, num2)
            elif op == "Substract":
                result = Substract(num1, num2)
            elif op == "Multiply":
                result = Multiply(num1, num2)
            elif op == "Divide":
                result = Divide(num1, num2)
            elif op == "Modulas":
                result = Modulas(num1, num2)
            elif op == "Power":
                result = Power(num1, num2)
            else:
                result = "Select a valid operation"
       
        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x350")
root.resizable(False, False)

tk.Label(root, text="Simple Calculator", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

operation = tk.StringVar(root)
operation.set("Add")  # default value
options = ["Add", "Substract", "Multiply", "Divide", "Modulas", "Power", "Square Root"]

tk.OptionMenu(root, operation, *options).pack(pady=10)

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()