import tkinter as tk
from services import add_task, list_tasks, complete_task, delete_task

class TaskManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack(pady=5)

        self.desc_entry = tk.Entry(root, width=40)
        self.desc_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.listbox.bind("<<ListboxSelect>>", self.show_description)

        self.description_label = tk.Label(root, text="Description:", anchor="w")
        self.description_label.pack(fill="x")

        self.description_text = tk.Text(root, height=4, width=50, state="disabled")
        self.description_text.pack(pady=5)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.refresh_tasks()

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        tasks = list_tasks()
        for i, task in enumerate(tasks):
            status = "✔" if task.completed else "✘"
            self.listbox.insert(tk.END, f"{i}. [{status}] {task.title}")

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        if title:
            add_task(title, description)
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.refresh_tasks()

    def show_description(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            tasks = list_tasks()
            task = tasks[index]

            self.description_text.config(state="normal")
            self.description_text.delete("1.0", tk.END)
            self.description_text.insert(tk.END, task.description)
            self.description_text.config(state="disabled")

    def complete_task(self):
        selection = self.listbox.curselection()
        if selection:
            complete_task(selection[0])
            self.refresh_tasks()

    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            delete_task(selection[0])
            self.refresh_tasks()