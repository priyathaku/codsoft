# todo.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n=== To-Do List ===")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Enter a valid number!")

def todo_app():
    while True:
        print("\nOptions: 1. Show  2. Add  3. Remove  4. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    todo_app()
