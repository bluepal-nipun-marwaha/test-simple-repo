import tkinter as tk
from ui import TaskManagerUI

def main():
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()