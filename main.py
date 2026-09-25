tasks = [
    {"due date": "9/25/26", "task": "do dishes"},
    {"due date": "9/26/26", "task": "take out trash"},
    {"due date": "9/27/26", "task": "walk the dog"},
]


def add_task():
    """Add a task to the task list."""
    task = input("Enter task: ").strip()
    due_date = input("Enter due date: ").strip()

    if not task or not due_date:
        print("Task and due date are required.")
        return

    tasks.append({"due date": due_date, "task": task})
    print(f"Task added: {task} (Due: {due_date})")


def search_task():
    """Find tasks whose descriptions contain the search term."""
    search_term = input("Enter task to search for: ").strip().lower()
    results = [item for item in tasks if search_term in item["task"].lower()]

    if results:
        for item in results:
            print(f"Found task: {item['task']} (Due: {item['due date']})")
    else:
        print("No tasks found.")


def mark_task_completed():
    """Remove the first task matching the user's search term."""
    search_term = input("Enter task to mark as completed: ").strip().lower()

    for index, item in enumerate(tasks):
        if search_term in item["task"].lower():
            completed_task = tasks.pop(index)
            print(f"Task marked as completed: {completed_task['task']}")
            return

    print("Task not found.")


def display_tasks():
    """Display all current tasks."""
    if not tasks:
        print("No tasks available.")
        return

    for item in tasks:
        print(f"Task: {item['task']} (Due: {item['due date']})")


def main():
    """Run the interactive task manager menu."""
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Search Task")
        print("3. Mark Task Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            search_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
