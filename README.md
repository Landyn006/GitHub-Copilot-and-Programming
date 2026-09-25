# Task Manager

A simple command-line task management application built in Python for organizing daily responsibilities and tracking due dates. This project allows users to add tasks, search for tasks by name, mark tasks as completed, and display all current tasks in a clean menu-driven interface.

## Features

- Add new tasks with a due date
- Search for a task by keyword
- Mark a task as completed
- Display all current tasks
- Easy-to-use command-line menu
- Lightweight, beginner-friendly Python project

## Project Overview

This task manager is designed to help users keep track of chores, reminders, and personal responsibilities. It stores tasks in memory while the program is running, making it a simple and effective tool for daily planning.

## Installation

1. Make sure Python is installed on your computer.
2. Download or clone this project to your local machine.
3. Open a terminal or command prompt in the project folder.
4. Run the following command:

```bash
python main.py
```

If `python` does not work, try:

```bash
python3 main.py
```

## Usage

Once the program starts, you will see a menu like this:

```text
Task Manager
1. Add Task
2. Search Task
3. Mark Task Completed
4. Display Tasks
5. Exit
```

### 1. Add Task
Select option `1` to add a task.

You will be prompted to enter:
- the task name
- the due date

Example:

```text
Enter task: do dishes
Enter due date: 9/25/26
```

### 2. Search Task
Select option `2` to look up a task by keyword.

Example:

```text
Enter task to search for: dishes
```

The program will print any matching tasks and their due dates.

### 3. Mark Task Completed
Select option `3` to remove a task after it is finished.

Example:

```text
Enter task to mark as completed: dishes
```

If the task exists, it will be removed from the list and marked as completed.

### 4. Display Tasks
Select option `4` to view all tasks currently in the list.

### 5. Exit
Select option `5` to close the program.

## Example Workflow

```text
Task Manager
1. Add Task
2. Search Task
3. Mark Task Completed
4. Display Tasks
5. Exit
Enter your choice: 1
Enter task: walk the dog
Enter due date: 9/27/26

Task Manager
Enter your choice: 4
Task: walk the dog (Due: 9/27/26)
```

## Requirements

- Python 3.x

## License

This project is intended for educational and personal use.

## Author

Created as a simple Python task manager project for learning basic programming concepts such as lists, dictionaries, functions, loops, and user input.
