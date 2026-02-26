TASK MANAGER GUI - USER GUIDE
=============================

OVERVIEW
--------
Task Manager is a desktop application that allows you to manage daily tasks
through a simple graphical interface.

STARTING THE APPLICATION
------------------------
1. Open a terminal in the project folder.
2. Run:

   python main.py

3. The application window will appear.

ADDING A TASK
-------------
1. Enter the task title in the first input field.
2. Enter a description in the second field (optional).
3. Click "Add Task".
4. The task will appear in the list.

VIEWING A DESCRIPTION
---------------------
1. Click on any task in the list.
2. The description will appear below the list.

MARKING A TASK COMPLETE
-----------------------
1. Select a task from the list.
2. Click "Complete Task".
3. The task status will change to completed.

DELETING A TASK
---------------
1. Select a task.
2. Click "Delete Task".
3. The task will be removed permanently.

DATA STORAGE
------------
All tasks are stored in a file called:

tasks.json

This file is created automatically when the first task is added.

TROUBLESHOOTING
---------------
If the app does not start:
- Ensure Python 3.8+ is installed.
- Make sure you are running the command inside the project folder.