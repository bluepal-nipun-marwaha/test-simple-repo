from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake database
tasks = []

class Task(BaseModel):
    id: int
    title: str
    description: str


@app.get("/")
def read_root():
    return {"message": "Task Manager API Running"}


# GET all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# GET task by id
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# CREATE task
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.dict())
    return {"message": "Task created", "task": task}


# UPDATE task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task.dict()
            return {"message": "Task updated", "task": updated_task}

    raise HTTPException(status_code=404, detail="Task not found")


# DELETE task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(index)
            return {"message": "Task deleted", "task": deleted}

    raise HTTPException(status_code=404, detail="Task not found")