# REST API Application Documentation

## 1. Introduction

This project implements a **RESTful API for task management using Python**. The API allows users to perform basic **CRUD operations (Create, Read, Update, Delete)** on tasks.

The application follows **REST principles** using standard **HTTP methods** and returns responses in **JSON format**.

The API is implemented using the Python web framework **Flask**, which provides a lightweight environment for developing web services.

---

## 2. System Architecture

The application follows a simple architecture:

```
Client (Browser/Postman)
        |
        v
REST API Server (Flask)
        |
        v
In-Memory Data Storage (Python List)
```

- Client sends HTTP requests  
- Flask API Server processes the request  
- Server returns JSON responses  

---

## 3. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Data Format | JSON |
| API Testing Tool | Postman |
| Runtime Server | Flask Development Server |

---

## 4. Installation and Setup

### Step 1: Install Python
Ensure **Python 3.x** is installed on the system.

### Step 2: Install Dependencies

```bash
pip install flask
```

### Step 3: Run the Application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

# 5. API Endpoints

## 5.1 Get All Tasks

**Endpoint**

```
GET /tasks
```

**Description**

Retrieves all tasks from the system.

**Example Response**

```json
[
  {
    "id": 1,
    "title": "Study Python",
    "description": "Learn REST APIs"
  }
]
```

---

## 5.2 Create a Task

**Endpoint**

```
POST /tasks
```

**Description**

Creates a new task in the system.

**Request Body**

```json
{
  "id": 1,
  "title": "Study Python",
  "description": "Learn REST API development"
}
```

**Response**

```json
{
  "message": "Task created",
  "task": {
    "id": 1,
    "title": "Study Python",
    "description": "Learn REST API development"
  }
}
```

---

## 5.3 Get Task by ID

**Endpoint**

```
GET /tasks/{id}
```

**Example**

```
GET /tasks/1
```

**Response**

```json
{
  "id": 1,
  "title": "Study Python",
  "description": "Learn REST APIs"
}
```

---

## 5.4 Update Task

**Endpoint**

```
PUT /tasks/{id}
```

**Request Body**

```json
{
  "id": 1,
  "title": "Study Python Updated",
  "description": "Practice REST API development"
}
```

**Response**

```json
{
  "message": "Task updated"
}
```

---

## 5.5 Delete Task

**Endpoint**

```
DELETE /tasks/{id}
```

**Example**

```
DELETE /tasks/1
```

**Response**

```json
{
  "message": "Task deleted"
}
```

---

## 6. Data Model

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique task identifier |
| title | String | Task title |
| description | String | Task details |

---

## 7. Testing the API

The API can be tested using:

- Web browser (for **GET requests**)
- **Postman**
- Command-line tools like **curl**

Example:

```bash
curl http://127.0.0.1:5000/tasks
```

---

## 8. Limitations

- Data is stored **in memory** and will reset when the server restarts.
- No **authentication or authorization** is implemented.
- No **database integration**.

---

## 9. Future Improvements

Possible enhancements include:

- Database integration using **PostgreSQL**
- Authentication using **JWT**
- Pagination for large datasets
- Logging and error monitoring
- Deployment using **Docker**