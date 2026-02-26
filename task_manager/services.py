from storage import load_tasks, save_tasks
from models import Task

def add_task(title, description=""):
    tasks = load_tasks()
    tasks.append(Task(title, description))
    save_tasks(tasks)

def list_tasks():
    return load_tasks()

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        save_tasks(tasks)
        return True
    return False

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        return True
    return False