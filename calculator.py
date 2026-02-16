import tkinter as tk

root = tk.Tk()
root.title("Custom Calculator")
root.geometry("350x500")
root.resizable(False, False)

# ---------------- Colors ----------------
BG_COLOR = "#1e1e1e"
DISPLAY_COLOR = "#252526"
BTN_COLOR = "#333333"
OPERATOR_COLOR = "#ff9500"
EQUAL_COLOR = "#28a745"
TEXT_COLOR = "white"

root.configure(bg=BG_COLOR)

# ---------------- Variables ----------------
expression = ""
current_input = ""

equation = tk.StringVar()
history_var = tk.StringVar()

# ---------------- History Label ----------------
history_label = tk.Label(
    root,
    textvariable=history_var,
    font=("Arial", 14),
    bg=BG_COLOR,
    fg="#888888",
    anchor="e"
)
history_label.pack(fill="both", padx=10, pady=(10, 0))

# ---------------- Display ----------------
display = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    bd=0,
    bg=DISPLAY_COLOR,
    fg=TEXT_COLOR,
    insertbackground="white",
    justify="right"
)
display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=5)

# ---------------- Functions ----------------

def press(key):
    global expression, current_input

    if key in "+-*/":
        if current_input == "":
            return  # Prevent double operators

        expression += current_input + key
        history_var.set(expression)
        current_input = ""
        equation.set("")
    else:
        current_input += str(key)
        equation.set(current_input)


def equalpress():
    global expression, current_input

    try:
        expression += current_input
        result = eval(expression)

        # Scientific notation for large numbers
        if abs(result) >= 1e9:
            formatted = "{:.6e}".format(result)
        else:
            formatted = str(result)

        equation.set(formatted)
        history_var.set("")
        expression = ""
        current_input = formatted

    except:
        equation.set("Error")
        expression = ""
        current_input = ""


def clear():
    global expression, current_input
    expression = ""
    current_input = ""
    equation.set("")
    history_var.set("")


# ---------------- Buttons ----------------

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:

    if text == "=":
        bg_color = EQUAL_COLOR
        action = equalpress
    elif text in "+-*/":
        bg_color = OPERATOR_COLOR
        action = lambda x=text: press(x)
    else:
        bg_color = BTN_COLOR
        action = lambda x=text: press(x)

    tk.Button(
        button_frame,
        text=text,
        width=5,
        height=2,
        font=("Arial", 18),
        bg=bg_color,
        fg=TEXT_COLOR,
        activebackground="#555555",
        activeforeground="white",
        bd=0,
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

# ---------------- Clear Button ----------------

tk.Button(
    button_frame,
    text="C",
    width=23,
    height=2,
    font=("Arial", 18),
    bg="#d9534f",
    fg="white",
    activebackground="#c9302c",
    bd=0,
    command=clear
).grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()