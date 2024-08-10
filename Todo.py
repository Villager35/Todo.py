import sys

# In-memory storage for the to-do list
todo_list = []

def show_help():
    print("\nSimple To-Do List")
    print("Commands:")
    print("  add <task>          - Add a new task")
    print("  list                - List all tasks")
    print("  done <task number>  - Mark a task as completed")
    print("  remove <task number> - Remove a task")
    print("  help                - Show this help message")
    print("  exit                - Exit the program\n")

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f"Added task: {task}")

def list_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, item in enumerate(todo_list, start=1):
            status = "✓" if item["completed"] else "✗"
            print(f"{i}. {status} {item['task']}")

def mark_task_as_done(task_number):
    try:
        todo_list[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    except IndexError:
        print(f"Task {task_number} does not exist.")

def remove_task(task_number):
    try:
        removed_task = todo_list.pop(task_number - 1)
        print(f"Removed task: {removed_task['task']}")
    except IndexError:
        print(f"Task {task_number} does not exist.")

def main():
    show_help()
    while True:
        command = input("> ").strip().split(maxsplit=1)
        action = command[0].lower()

        if action == "add" and len(command) > 1:
            add_task(command[1])
        elif action == "list":
            list_tasks()
        elif action == "done" and len(command) > 1:
            try:
                mark_task_as_done(int(command[1]))
            except ValueError:
                print("Please enter a valid task number.")
        elif action == "remove" and len(command) > 1:
            try:
                remove_task(int(command[1]))
            except ValueError:
                print("Please enter a valid task number.")
        elif action == "help":
            show_help()
        elif action == "exit":
            print("Exiting the program.")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
