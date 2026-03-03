📄 1️⃣ README.md (Markdown Format)
# Task Manager GUI

A simple desktop Task Manager application built with Python and Tkinter.

This application allows users to:
- Add tasks with descriptions
- View tasks in a list
- Mark tasks as completed
- Delete tasks
- View task descriptions dynamically

---

## 📦 Project Structure

task_manager_gui/
│
├── main.py          # Application entry point
├── ui.py            # GUI layout and event handling
├── models.py        # Task data model
├── storage.py       # JSON file handling
└── services.py      # Business logic layer

---

## 🚀 Installation

### Requirements
- Python 3.8+

No external libraries are required.

### Setup

Navigate into the project folder:

    cd task_manager_gui


---

## ▶️ Running the Application

    python main.py

The GUI window will open.

---

## 🧠 Architecture Overview

The application follows a layered architecture:

    UI Layer (Tkinter)
    ↓
    Services Layer (Business Logic)
    ↓
    Storage Layer (JSON Persistence)


This ensures:
- Separation of concerns  
- Maintainability  
- Scalability  

---

## 📂 Data Storage

Tasks are stored in:

tasks.json

Each task is saved in the following format:
    
    {
    "title": "Example",
    "description": "Sample description",
    "completed": false
    }

---

## ✨ Features

- Add new tasks
- Delete tasks
- Mark tasks as complete
- View descriptions on selection
- Persistent storage using JSON

---

## 🔮 Future Improvements

- Due dates
- Priority levels
- Search functionality
- SQLite database support
- Dark theme
- Editable task descriptions

---

## 📜 License

Free to use for learning purposes.