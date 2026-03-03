Task Manager GUI
================

Overview
--------

Task Manager GUI is a desktop application built using Python and Tkinter.
It follows a layered architecture separating UI, business logic, and storage.

Architecture
------------

The application is structured into the following layers:

UI Layer
    Handles all graphical interface components and event bindings.

Services Layer
    Contains business logic for task management.

Storage Layer
    Responsible for reading and writing data to a JSON file.

Data Flow
---------

UI -> Services -> Storage

Modules
-------

main.py
    Entry point of the application.
    Initializes the Tkinter root window and launches the UI.

ui.py
    Defines the TaskManagerUI class.
    Handles layout, event bindings, and UI refresh logic.

models.py
    Contains the Task class.
    Provides serialization and deserialization methods.

storage.py
    Manages JSON persistence.

    Functions:
        - load_tasks()
        - save_tasks()

services.py
    Implements business operations:
        - add_task()
        - list_tasks()
        - complete_task()
        - delete_task()

Data Model
----------

Task Object Structure:

- title (str)
- description (str)
- completed (bool)

Stored as JSON in:

tasks.json

Example:

::

    {
        "title": "Learn Python",
        "description": "Practice GUI design",
        "completed": false
    }

Extensibility
-------------

Possible enhancements:

- Replace JSON with SQLite
- Add task editing capability
- Implement task filtering
- Introduce logging
- Add unit tests
- Refactor into MVC pattern

Design Considerations
---------------------

- Separation of concerns
- Minimal coupling
- High cohesion
- Persistent storage abstraction