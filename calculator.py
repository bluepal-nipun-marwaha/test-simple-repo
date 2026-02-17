import tkinter as tk

# ==============================
# Configuration
# ==============================

CONFIG = {
    "window": {
        "width": 350,
        "height": 550,
        "resizable": False,
        "background_color": "#1e1e1e"
    },
    "colors": {
        "display_background": "#2d2d2d",
        "button_default": "#3a3a3a",
        "button_operator": "#cc7000",
        "button_equals": "#1e7e34",
        "button_clear": "#d9534f",
        "button_blank": "#333333",
        "text": "white",
        "history_text": "#bbbbbb"
    },
    "formatting": {
        "scientific_threshold": 1e9,
        "scientific_precision": 10
    },
    "fonts": {
        "history": ("Arial", 14, "bold"),
        "display": ("Arial", 26, "bold"),
        "button": ("Arial", 18, "bold")
    }
}

# ==============================
# Application Setup
# ==============================

root = tk.Tk()
root.title("Custom Calculator")
root.geometry(f"{CONFIG['window']['width']}x{CONFIG['window']['height']}")
root.resizable(CONFIG['window']['resizable'], CONFIG['window']['resizable'])
root.configure(bg=CONFIG["window"]["background_color"])

expression = ""
current_input = ""

equation = tk.StringVar()
history_var = tk.StringVar()

# ==============================
# Display
# ==============================

history_label = tk.Label(
    root,
    textvariable=history_var,
    font=CONFIG["fonts"]["history"],
    bg=CONFIG["window"]["background_color"],
    fg=CONFIG["colors"]["history_text"],
    anchor="e"
)
history_label.grid(row=0, column=0, columnspan=4, sticky="we", padx=10, pady=(5,0))

display = tk.Entry(
    root,
    textvariable=equation,
    font=CONFIG["fonts"]["display"],
    bg=CONFIG["colors"]["display_background"],
    fg=CONFIG["colors"]["text"],
    bd=0,
    justify="right"
)
display.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# ==============================
# Button Handlers
# ==============================

def press(key):
    global expression, current_input

    if key.isdigit() or key == ".":
        current_input += key
        equation.set(current_input)

    elif key in "+-*/":
        if current_input == "":
            return
        expression += current_input + key
        history_var.set(current_input + key)
        current_input = ""
        equation.set("")

def equalpress():
    global expression, current_input

    try:
        expression += current_input
        result = eval(expression)

        if abs(result) >= CONFIG["formatting"]["scientific_threshold"]:
            result = format(result, f".{CONFIG['formatting']['scientific_precision']}e")

        equation.set(result)
        history_var.set("")
        expression = ""
        current_input = str(result)

    except Exception:
        equation.set("Error")
        history_var.set("")
        expression = ""
        current_input = ""

def clear():
    global expression, current_input
    expression = ""
    current_input = ""
    equation.set("")
    history_var.set("")

# ==============================
# Button Layout
# ==============================

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "(", ")", "!"]
]

for r, row in enumerate(buttons):
    for c, label in enumerate(row):

        if label == "":
            btn = tk.Button(
                root,
                text="",
                bg=CONFIG["colors"]["button_blank"],
                state="disabled",
                bd=0
            )

        elif label == "C":
            btn = tk.Button(
                root,
                text=label,
                font=CONFIG["fonts"]["button"],
                bg=CONFIG["colors"]["button_clear"],
                fg="white",
                command=clear
            )

        elif label == "=":
            btn = tk.Button(
                root,
                text=label,
                font=CONFIG["fonts"]["button"],
                bg=CONFIG["colors"]["button_equals"],
                fg=CONFIG["colors"]["text"],
                command=equalpress
            )

        elif label in "+-*/":
            btn = tk.Button(
                root,
                text=label,
                font=CONFIG["fonts"]["button"],
                bg=CONFIG["colors"]["button_operator"],
                fg=CONFIG["colors"]["text"],
                command=lambda x=label: press(x)
            )

        else:
            btn = tk.Button(
                root,
                text=label,
                font=CONFIG["fonts"]["button"],
                bg=CONFIG["colors"]["button_default"],
                fg=CONFIG["colors"]["text"],
                command=lambda x=label: press(x)
            )

        btn.grid(row=r + 2, column=c, sticky="nsew")

# ==============================
# Grid Configuration
# ==============================

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)

for i in range(len(buttons)):
    root.grid_rowconfigure(i + 2, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
