import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Display
display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)
display.pack(fill="both", padx=10, pady=10, ipady=10)


# Functions
def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
]


# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        tk.Button(
            frame,
            text=button,
            font=("Arial", 20),
            command=lambda x=button: click(x)
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=3,
            pady=3
        )


# Clear and equal buttons
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

tk.Button(
    frame,
    text="C",
    font=("Arial", 20),
    command=clear
).pack(
    side="left",
    expand=True,
    fill="both",
    padx=3,
    pady=3
)

tk.Button(
    frame,
    text="=",
    font=("Arial", 20),
    command=calculate
).pack(
    side="left",
    expand=True,
    fill="both",
    padx=3,
    pady=3
)


# Start the calculator
root.mainloop()
