# starter_app.py
# Run this in terminal: python starter_app.py add "Buy milk"

import sys

tasks = []

def main():
    if len(sys.argv) < 2:
        print("Usage: python starter_app.py [add <task> | list | delete <task#>]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task to add.")
            return
        task = " ".join(sys.argv[2:])
        tasks.append(task)
        print(f'Added task: "{task}"')
    elif command == "list":
        if not tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide the task number to delete.")
            return
        try:
            task_num = int(sys.argv[2])
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f'Deleted task: "{removed}"')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Task number must be an integer.")
    else:
        print("Unknown command. Use add, list, or delete.")

if __name__ == "__main__":
    main()