import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box for input/output
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=3, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Function to handle button click
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                  command=calculate, bg="#4CAF50", fg="white").grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                  command=lambda val=text: click(val)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text='C', width=23, height=2, font=('Arial', 16),
          command=clear, bg="#f44336", fg="white").grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the app
root.mainloop()
