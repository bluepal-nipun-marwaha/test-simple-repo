import json
from models import Task

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)