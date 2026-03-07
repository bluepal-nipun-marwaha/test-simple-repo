# Task Manager API Tutorial (FastAPI)

## Introduction

This tutorial demonstrates how to build a simple REST API for managing tasks using FastAPI.

The API allows you to:

- Create tasks
- View tasks
- Update tasks
- Delete tasks

The data is stored in an **in-memory list**, meaning it resets when the server restarts.

---

# Task Model

```python
class Task(BaseModel):
    id: int
    title: str
    description: str
```

Example task:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Study API development"
}
```

---

# Running the API

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

Interactive docs:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Root Endpoint

GET `/`

Returns a message confirming the API is running.

Response:

```json
{
  "message": "Task Manager API Running"
}
```

---

# Get All Tasks

GET `/tasks`

Returns a list of all tasks.

Example response:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Study API development"
  }
]
```

---

# Get Task by ID

GET `/tasks/{task_id}`

Example request:

```
GET /tasks/1
```

Example response:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Study API development"
}
```

Error response:

```json
{
  "detail": "Task not found"
}
```

---

# Create Task

POST `/tasks`

Request body:

```json
{
  "id": 2,
  "title": "Build API",
  "description": "Create a task manager API"
}
```

Response:

```json
{
  "message": "Task created",
  "task": {
    "id": 2,
    "title": "Build API",
    "description": "Create a task manager API"
  }
}
```

---

# Update Task

PUT `/tasks/{task_id}`

Example request body:

```json
{
  "id": 1,
  "title": "Learn FastAPI Advanced",
  "description": "Deep dive into FastAPI"
}
```

Response:

```json
{
  "message": "Task updated",
  "task": {
    "id": 1,
    "title": "Learn FastAPI Advanced",
    "description": "Deep dive into FastAPI"
  }
}
```

---

# Delete Task

DELETE `/tasks/{task_id}`

Example request:

```
DELETE /tasks/1
```

Response:

```json
{
  "message": "Task deleted",
  "task": {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Study API development"
  }
}
```

---

# API Summary

| Method | Endpoint | Description |
|------|------|------|
| GET | / | API status |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task by id |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

---

# Notes

This project uses an **in-memory list**:

```python
tasks = []
```

Restarting the server will delete all tasks.

For production use, replace this with a database such as:

- PostgreSQL
- SQLite
- MongoDB

---

# Testing the API

You can test the API using:

- Postman
- Insomnia
- FastAPI Docs

```
http://127.0.0.1:8000/docs
```

---

# Possible Improvements

- Add database support
- Add authentication
- Add task status (completed / pending)
- Add pagination
- Add filtering
- Add user accounts