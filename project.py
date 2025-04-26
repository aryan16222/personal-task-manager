# project.py

def main():
    tasks = load_tasks("tasks.txt")

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            try:
                index = int(input("Enter the task number to complete: ")) - 1
                complete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            save_tasks(tasks, "tasks.txt")
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def add_task(tasks, task):
    tasks.append(task)

def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Invalid task number.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks!")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks(filename):
    try:
        with open(filename) as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    main()
