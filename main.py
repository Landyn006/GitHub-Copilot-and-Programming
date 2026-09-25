lists = [
    
    {"due date": "9/25/26",
     "tasks": "do dishes"},
    {"due date": "9/26/26",
     "tasks": "take out trash"},
    {"due date": "9/27/26",
     "tasks": "walk the dog"},
    {"due date": "9/25/26",
     "tasks": "do dishes"}
]
def add_task():
    task=input("Enter task: ")
    due_date=input("Enter due date: ")
    lists.append({"due date": due_date, "tasks": task})

def search_task():
    search_term = input("Enter task to search for: ")
    results = [item for item in lists if search_term in item["tasks"]]
    if results:
        for item in results:
            print(f"Found task: {item['tasks']} (Due: {item['due date']})")
    else:
        print("No tasks found.")

def mark_task_completed():
    search_term = input("Enter task to mark as completed: ")
    for item in lists:
        if search_term in item["tasks"]:
            lists.remove(item)
            print(f"Task marked as completed: {item['tasks']}")
            return
    print("Task not found.")

def display_tasks():
    if not lists:
        print("No tasks available.")
    else:
        for item in lists:
            print(f"Task: {item['tasks']} (Due: {item['due date']})")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Search Task")
        print("3. Mark Task Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

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
main()